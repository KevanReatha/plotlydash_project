# Plotly Dash Project 

"Plotly Dash Project" is a web-based dashboard application developed using Plotly Dash, a Python framework for building interactive dashboards. The purpose of the project is to provide an intuitive interface for exploring and analyzing the Consumer Price Index (CPI) data for Australia.

This project has been deployed using Heroku (https://www.heroku.com) and is live onto https://cpi-australia1-eacdb9f8ac3f.herokuapp.com/ (Username: Kevan; Password: dashapp112)

## Features

The main features and components of the project include:

- Data Loading: The project loads the CPI data from a CSV file ("CPI_21062023.csv") using the Pandas library. The data is parsed and processed, including converting the "Date" column to datetime format.

- User Authentication: The project implements basic authentication using the dash_auth module, allowing authorized users to access the dashboard. Usernames and passwords are defined in the USERNAME_PASSWORD_PAIRS variable.

- Dashboard Layout: The dashboard layout is defined using HTML and Dash components. The layout includes a title, category selector, date range picker, submit button, line graph, and a data table.

- Interactive Components: The dashboard includes interactive components such as dropdowns, date pickers, and buttons. Users can select categories of interest, choose a date range, and click the submit button to update the visualizations and table.

- Callback Functions: The update_graph function is a callback function triggered by changes in the input components. It filters the data based on the selected category and date range, updates the line graph, and returns the filtered data for display in the data table.

- Visualization: The line graph is generated using Plotly, which allows for interactive exploration of the CPI data. Each selected category is represented as a separate line in the graph, with markers indicating specific data points. The graph's layout is customizable, including the title, font, and background color.

- Data Table: The project uses the Dash DataTable component to display the filtered data in a tabular format. The table is interactive and supports features such as sorting, searching, and exporting to CSV format.

- Styling: The project applies CSS stylesheets to enhance the visual appearance of the dashboard. The stylesheets include Bootstrap for responsive design and the Lato font from Google Fonts.

## Dependencies

The dependencies required for running the "Plotly Dash Project" are as follows:

- dash: The core library for creating Dash applications.
- dash-core-components: Provides higher-level components for constructing the user interface.
- dash-html-components: Provides HTML components for building the layout of the dashboard.
- dash-table: Provides the DataTable component for displaying data in tabular format.
- dash-auth: Provides basic authentication functionality for securing the dashboard.
- pandas: A powerful data manipulation library used for loading and processing the CPI data.
- datetime: A module for working with dates and times in Python.
- dateutil: A library that provides various utilities for parsing and manipulating dates.
- plotly: A library for creating interactive and customizable visualizations, used for generating the line graph.
- dash-bootstrap-components: Provides additional Bootstrap-based components and styling options for the dashboard layout.

