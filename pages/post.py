import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2, name="Latest Post")

video_one = 'https://raw.githubusercontent.com/henrycerpa/database/main/datascience.png'
link_one = 'https://youtu.be/Jqu_P_-495I'
video_two = 'https://raw.githubusercontent.com/henrycerpa/database/main/chatgpt.png'
link_two = 'https://youtu.be/Eh04BJfshWY'

def layout():
    return html.Div([
    html.H2("Latest social media posts", style={'textAlign':'center'}, className='my-3'),
    html.Hr(style={'color':'#e27f04',}),


        dbc.Row([
            dbc.Col([
                dcc.Markdown('##### Data Science in Latin America for 2030'),
                dcc.Markdown('The growing demand for data science professionals in Latin America has led to a shortage of '
                         'talent in the field')
            ], width=2),
            dbc.Col([

                html.A(html.Img(src=video_one, style={'position': 'relative', 'width': '60%', 'left': '0px', 'top': '0px'}), href=link_one, target="_blank")

            ], width=5),
        ], justify='center'),

        html.Hr(style={'color': '#e27f04', }),

        dbc.Row([
            dbc.Col([
                dcc.Markdown('##### How to Use ChatGPT in Data Science'),
                dcc.Markdown(
                    'ChatGPT can be a valuable resource for you in several ways')
            ], width=2),
            dbc.Col([

                html.A(html.Img(src=video_two,
                                style={'position': 'relative', 'width': '60%', 'left': '0px', 'top': '0px'}),
                       href=link_two, target="_blank")

            ], width=5),
        ], justify='center'),
])
