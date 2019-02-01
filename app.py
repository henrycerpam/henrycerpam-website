import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.UNITED])

header = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            label='Go to...',
            children=[
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if not page["path"].startswith("/app")]
        )],
    brand="HENRY ALBERT CERPA MARQUEZ",
    color="info",
    dark=True,
)

app.layout = dbc.Container([header, dash.page_container], fluid=False)

if __name__ == '__main__':
	app.run_server()