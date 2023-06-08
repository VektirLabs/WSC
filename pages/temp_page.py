# page2.py
import dash
from dash import html, dcc

dash.register_page(__name__, path='/temp_page')

layout = html.Div(children=[
    html.H1(children='This is our Temp page'),

    html.Div(children='''
        This is our Temp page content.
    '''),

])
