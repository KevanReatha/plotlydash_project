import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash.dash_table.Format import Group
from dash import dash_table
import dash_auth

import pandas as pd
from datetime import datetime
from dateutil import parser

# Create logins
USERNAME_PASSWORD_PAIRS = [["username", "password"], ["Kevan", "dashapp112"]]

# Define CSS styles
external_stylesheets = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css",
    {
        "href": "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

# Load data
raw = pd.read_csv("CPI_21062023.csv", parse_dates=["Date"], dayfirst=True)
category_list = [
    {"label": category, "value": category} for category in raw["Attribute"].unique()
]

# Create app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD_PAIRS)
server = app.server


# cpi_definition = '''

# What is a Consumer Price Index (CPI)?
# A CPI is a measure of the average change over time in the prices paid by households for a fixed basket of goods and services.

# Source : https://www.abs.gov.au/'''

# html.Div(
#     [
#         dcc.Markdown(children=cpi_definition)
#     ]),


app.layout = html.Div(
    className="container",
    children=[
        html.H1(
            "Consumer Price Index, Australia",
            className="header mb-4 text-center",
            style={"font-family": "Lato, sans-serif", },
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H6(
                            "Category",
                            className="selector-label",
                            style={"font-family": "Lato, sans-serif"},
                        ),
                        dcc.Dropdown(
                            id="my_category_picker",
                            options=category_list,
                            value=["Health"],
                            multi=True,
                        ),
                    ],
                    style={"width": "45%", "padding": 10},
                ),
                html.Div(
                    children=[
                        html.H6(
                            "Date Range",
                            className="selector-label",
                            style={"font-family": "Lato, sans-serif"},
                        ),
                        dcc.DatePickerRange(
                            id="my_date_picker",
                            min_date_allowed=datetime(1949, 1, 1),
                            max_date_allowed=datetime(2023, 3, 1),
                            start_date=datetime(2019, 1, 1),
                            end_date=datetime(2023, 3, 1),
                        ),
                    ],
                    style={"width": "45%", "padding": 10},
                ),
            ],
            style={"padding": 10},
        ),
        html.Div(
            # className="row",
            children=[
                html.Div(
                    className="col-md-12",
                    children=[
                        html.Button(
                            id="submit-button",
                            n_clicks=0,
                            children="Submit",
                            className="btn btn-primary",
                            style={"font-family": "Lato, sans-serif"},
                        )
                    ],
                ),
            ],
        ),
        html.Div(
            # className="row",
            children=[
                html.Div(
                    className="col-lg-12",
                    children=[
                        dcc.Graph(
                            id="my_graph",
                            className="mt-4",
                            style={"height": "50vh"},
                        )
                    ],
                ),
            ],
            style={"padding": 20},
        ),
        html.Div(
            # className="row",
            children=[
                html.Div(
                    className="col-lg-12",
                    children=[
                        dash_table.DataTable(
                            id="table",
                            columns=[{"name": i, "id": i} for i in raw.columns],
                            data=raw.to_dict("records"),
                            export_format="csv",
                            style_as_list_view=True,
                            style_cell={
                                "fontFamily": "Lato, sans-serif",
                                "padding": "5px",
                            },
                            style_cell_conditional=[
                                {"if": {"column_id": c}, "textAlign": "left"}
                                for c in ["Date", "Attribute"]
                            ],
                            style_header={
                                "backgroundColor": "white",
                                "fontWeight": "bold",
                            },
                            style_table={"overflowX": "auto"},
                        )
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(
    [Output("my_graph", "figure"), Output("table", "data")],
    [
        Input("submit-button", "n_clicks"),
        State("my_category_picker", "value"),
        State("my_date_picker", "start_date"),
        State("my_date_picker", "end_date"),
    ],
)
def update_graph(n_clicks, category_picker, start_date, end_date):
    start = datetime.strptime(start_date[:10], "%Y-%m-%d")
    end = datetime.strptime(end_date[:10], "%Y-%m-%d")

    traces = []
    filtered_data = pd.DataFrame()
    for cat in category_picker:
        df = raw[
            (raw["Attribute"] == cat) & (raw["Date"] >= start) & (raw["Date"] <= end)
        ]
        traces.append(
            {
                "x": df["Date"],
                "y": df["Value"],
                "name": cat,
                "mode": "lines+markers",
                "marker": {"size": 8},
            }
        )
        df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
        filtered_data = pd.concat([filtered_data, df])

    fig = {
        "data": traces,
        "layout": {
            "title": ", ".join(category_picker) + " CPI",
            "font": {"family": "Lato, sans-serif"},
            "plot_bgcolor": "#f8f8f8",
            "paper_bgcolor": "#f8f8f8",
        },
    }

    return fig, filtered_data.to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)
