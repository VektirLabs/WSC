from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash

# Main app details --------------------------------------------------
app = Dash(__name__, 
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP]
           )

# Layout section ----------------------------------------------------
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
    ],
    brand="Navbar",
    brand_href="#",
    sticky="top",
)

sidebar = dbc.Col(
    [
        html.H2("Sidebar"),
        html.P("This is the content of the sidebar"),
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/page-1", id="page-1-link"),
                dbc.NavLink("Page 2", href="/page-2", id="page-2-link"),
                dbc.NavLink("Page 3", href="/page-3", id="page-3-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={'height': '100vh', 'position': 'fixed', 'padding': '20px', 'background': 'lightgray'}, 
    width=3
)

body = dbc.Col([
        html.H2("Body"),
        html.P("This is the content of the main body"),
        html.Div([html.Div(dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"]))
            for page in dash.page_registry.values()]),
    ])

app.layout = html.Div([
    navbar,
    sidebar,
    body,
	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)
