# page2.py

import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Template Page"),
            html.P("This is the content of Page 2.")
        ])
    ])
])

def register_callbacks(app):
    pass

