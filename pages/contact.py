import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3, name="Email & Contact")

green_text = {'color':'green'}

email = 'https://raw.githubusercontent.com/henrycerpa/database/main/email.png'
telegram = 'https://raw.githubusercontent.com/henrycerpa/database/main/telegram.png'
linkedin = 'https://raw.githubusercontent.com/henrycerpa/database/main/linkedin.png'
github = 'https://raw.githubusercontent.com/henrycerpa/database/main/github.png'
youtube = 'https://raw.githubusercontent.com/henrycerpa/database/main/youtube.png'

def layout():
    return html.Div([
        html.H2("Email & Contact Info", style={'textAlign': 'center'}, className='my-3'),
        html.Hr(style={'color': '#e27f04', }),

        dbc.Row([
            dbc.Col([
                html.Img(src=email,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[henrycerpa@gmail.com](mailto:henrycerpa@gmail.com)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=linkedin,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Go to my LinkedIn user](https://www.linkedin.com/in/henry-cerpa/)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=github,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Go to my GitHub repositories](https://github.com/henrycerpa)', link_target='_blank'),

            ], width=3),
        ], justify='center'),

        dbc.Row([
            dbc.Col([
                html.Img(src=youtube,
                                style={'position': 'relative', 'width': '20%', 'left': '0px', 'top': '0px'}),

            ], width=2),
            dbc.Col([

                dcc.Markdown('[Go to my YouTube channel](https://www.youtube.com/@datahenry)', link_target='_blank'),

            ], width=3),
        ], justify='center'),




    ])
