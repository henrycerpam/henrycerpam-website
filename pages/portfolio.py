import dash
import pandas as pd
import plotly.graph_objs as go
from dash import html, dcc, Input, Output, State, callback
from .side_bar import sidebar
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__, title='ICA', order=1, name="Portfolio")

top_samples = pd.read_csv("https://raw.githubusercontent.com/henrycerpa/database/main/top_cases.csv")
top_three = pd.read_csv("https://raw.githubusercontent.com/henrycerpa/database/main/top_three.csv")
df = pd.read_csv('https://raw.githubusercontent.com/henrycerpa/database/main/map.csv')
data = pd.read_csv('https://raw.githubusercontent.com/henrycerpa/database/main/final_modelo.csv')

top_negative = top_samples[top_samples.result == 'negative'].sort_values("cases")[-10:]
top_positive = top_samples[top_samples.result == 'positive'].sort_values("cases")[-10:]

sample_number = dbc.RadioItems(
    id='sample_choose',
    className='radio',
    options=[dict(label='Positive', value=0), dict(label='Negative', value=1)],
    value=0,
    inline=True
)

dict_ = {'ANTIOQUIA': 'ANTIOQUIA', 'BOLIVAR': 'BOLIVAR', 'BOYACA': 'BOYACA', 'CALDAS': 'CALDAS', 'CAQUETA': 'CAQUETA',
         'CASANARE': 'CASANARE',
         'CAUCA': 'CAUCA', 'CESAR': 'CESAR', 'CORDOBA': 'CORDOBA', 'CUNDINAMARCA': 'CUNDINAMARCA',
         'MAGDALENA': 'MAGDALENA', 'META': 'META', 'NARINO': 'NARINO',
         'NORTE DE SANTANDER': 'NORTE DE SANTANDER', 'QUINDIO': 'QUINDIO', 'RISARALDA': 'RISARALDA',
         'SANTANDER': 'SANTANDER', 'SUCRE': 'SUCRE', 'TOLIMA': 'TOLIMA',
         'VALLE DEL CAUCA': 'VALLE DEL CAUCA'}

departamentos = ['AMAZONAS', 'ANTIOQUIA', 'ARAUCA', 'ATLANTICO', 'BOGOTA', 'BOLIVAR', 'BOYACA', 'CALDAS', 'CAQUETA',
                 'CASANARE', 'CAUCA', 'CESAR', 'CHOCO', 'CORDOBA', 'CUNDINAMARCA', 'GUAINIA', 'GUAJIRA', 'GUAVIARE',
                 'HUILA', 'MAGDALENA', 'META', 'NARINO', 'NORTE DE SANTANDER', 'PUTUMAYO', 'QUINDIO', 'RISARALDA',
                 'SANTANDER', 'SUCRE', 'TOLIMA', 'VALLE DEL CAUCA', 'VAUPES', 'VICHADA', 'PAIS']
departamentos.sort()

options_neg = [dict(label=key, value=dict_[key]) for key in top_negative['state'].tolist()[::-1] if key in dict_.keys()]
options_pos = [dict(label=val, value=val) for val in top_positive["state"].tolist()[::-1]]

bar_colors = ['#ebb36a', '#6dbf9c']
bar_options = [top_positive, top_negative]

drop_map = dcc.Dropdown(
    id='drop_map',
    clearable=False,
    searchable=False,
    style={'margin': '4px', 'box-shadow': '0px 0px #ebb36a', 'border-color': '#ebb36a'}
)

max_size = 50
size_scale = max_size / df['positive'].max()

# Create a scattermapbox showing the towns with the number of positive and negative cases
fig = go.Figure(go.Scattermapbox(
    lat=df['latitude'],
    lon=df['longitude'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=df['positive'] * size_scale,
        color=df['positive'],
        colorscale='jet',
        opacity=1.0
    ),
    text=df.apply(lambda x: '{} - {}'.format(x['code'], x['name']), axis=1),
    hoverinfo='text',
    customdata=df[['positive']],
    name='Towns'
))

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=5,
    mapbox_center={"lat": 4.5709, "lon": -74.2973},
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    coloraxis=dict(colorscale='jet', colorbar=dict(title='Positive Cases', ticksuffix=' cases'))
)

years = data['year'].unique()
locations = data['departamento'].unique()

# Define the options for the dropdown menu
departamento_options = [{'label': departamento, 'value': departamento} for departamento in data['departamento'].unique()]

def layout():
    return html.Div([

        dbc.Row(
            [
                dbc.Col(
                    [
                        sidebar()
                    ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                dbc.Col(
                    [
                        html.Div([
                            html.Div([
                                html.P([
                                    'Contributing to the sustainable development of the agriculture, fisheries and aquaculture sectors, to control the brucellosis is fundamental due the profound effect not only on animal health but the production as well. In order to implement public measures, it is necessary to know the conditions that affect the onset and spread of brucellosis.'],
                                    style={'color': 'BLACK', 'font-size': '15px'})
                            ], style={'width': '180%'}),
                        ], className='footer', style={'display': 'flex'}),

                        html.Div([
                            html.Label("Choose the sample result:"),
                            html.Br(),
                            sample_number
                        ],  className='box', style={'margin': '10px', 'padding-top': '15px', 'padding-bottom': '15px'}),

                        html.Div([
                            html.Div([

                                html.Div([
                                    html.Label(id='title_bar'),
                                    dcc.Graph(id='bar_fig'),
                                    html.Div([
                                        html.P(id='comment')
                                    ], className='box_comment'),
                                ], className='box', style={'padding-bottom': '15px'}),

                                html.Div([
                                    html.Img(
                                        src='https://raw.githubusercontent.com/henrycerpa/database/main/vaca.png',
                                        style={'width': '60%', 'display': 'block', 'margin': 'auto', 'opacity': '80%'}),
                                ], style={'text-align': 'center'}),

                            ], style={'width': '40%'}),

                            html.Div([

                                html.Div([
                                    html.Label(id='choose_state', style={'margin': '10px'}),
                                    drop_map,
                                ], className='box'),

                                html.Div([
                                    html.Div([
                                        html.Div([
                                            html.Div([
                                                html.H4(id='city_one', style={'font-weight': 'normal'}),
                                                html.H3(id='pos_one')
                                            ], className='box_emissions'),
                                            html.Br(),
                                            html.Div([
                                                html.H4(id='city_two', style={'font-weight': 'normal'}),
                                                html.H3(id='pos_two')
                                            ], className='box_emissions'),
                                            html.Br(),
                                            html.Div([
                                                html.H4(id='city_three', style={'font-weight': 'normal'}),
                                                html.H3(id='pos_three')
                                            ], className='box_emissions'),

                                        ], style={'display': 'flex'}),

                                    ], className='box', style={'heigth': '10%'}),

                                    html.Div([
                                        html.Div([

                                            dcc.Graph(id='map', figure=fig)], style={'position': 'relative', 'top': '0px'}),

                                    ], className='box', style={'padding-bottom': '0px'}),
                                ]),
                            ], style={'width': '60%'}),
                        ], className='row'),

                        html.Div([
                            html.Br(),
                            html.Br(),
                            html.Label([
                                '3. Choose a State that represents the relationship between the number of vaccinated animals and the number of undetected infectious animals '
                                '(V/I ratio) over the years affected by brucellosis disease. The V/I ratio is a critical indicator for monitoring the effectiveness of'
                                'vaccination programs and disease control efforts, providing insights into the disease transmission dynamics and the overall health '
                                'status of the animal population in each State. This graph is analyzed using epidemiological models. In this case, the model used in '
                                'is the Susceptible-Infectious-Recovered (SIR) model.'],
                                style={"text-align": "center"}),

                        ], className='one column'),

                        dcc.Dropdown(
                            id='departamento-dropdown',
                            options=departamento_options,
                            value=data['departamento'].iloc[0]
                            # Set the default value to the first departamento in the dataset
                        ),
                        dcc.Graph(id='vaccination-graph'),


                    ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
            ]
        )
    ])

@callback(
    [
        Output('title_bar', 'children'),
        Output('bar_fig', 'figure'),
        Output('comment', 'children'),
        Output('drop_map', 'options'),
        Output('drop_map', 'value'),
        Output('choose_state', 'children')
    ],
    [
        Input('sample_choose', 'value')
    ],
)
def bar_chart(top10_select):
    ################## Top10 Plot ##################
    title = '1. Top #10 cases in 2021:'
    df = bar_options[top10_select]

    if top10_select == 2:
        bar_fig = dict(type='bar',
                       x=df.cases,
                       y=df["state"],
                       orientation='h',
                       marker_color=['#ebb36a' if x == 'Animal' else '#6dbf9c' for x in df.result])
    else:
        bar_fig = dict(type='bar',
                       x=df.cases,
                       y=df["state"],
                       orientation='h',
                       marker_color=bar_colors[top10_select])

    ################## Dropdown Bar ##################
    if top10_select == 0:
        options_return = options_pos
        state_chosen = "2. Choose a state for top #3 of towns with cases in 2021:"
        comment = ["3 out of 4 positive cases are from Antioquia, Cundinamarca and Nariño. The most critical: SANTA ROSA DE OSOS"]
    elif top10_select == 1:
        options_return = options_neg
        state_chosen = "2. Choose a state for top #3 of towns with cases in 2021:"
        comment = [
            "Comparing with the positives, 5 of 100 samples in Nariño are positive, the highest percentage among the states"]

    return title, \
           go.Figure(data=bar_fig, layout=dict(height=300, font_color='#363535', paper_bgcolor='rgba(0,0,0,0)',
                                               plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=20, r=20, t=30, b=20),
                                               margin_pad=10)), \
           comment, \
           options_return, \
           options_return[0]['value'], \
           state_chosen


@callback(
    [
        Output('pos_one', 'children'),
        Output('pos_two', 'children'),
        Output('pos_three', 'children'),
        Output('city_one', 'children'),
        Output('city_two', 'children'),
        Output('city_three', 'children'),
    ],
    [
        Input('drop_map', 'value'),

    ],
    [State("drop_map", "options")]
)
def update_map(drop_map_value, opt):
    ################## Top Three datset ##################

    the_label = [x['label'] for x in opt if x['value'] == drop_map_value]

    state_option_chosen = top_three[top_three["state"] == the_label[0]]
    pos_one_str = str(state_option_chosen["pos_one"].values[0])
    pos_two_str = str(state_option_chosen["pos_two"].values[0])
    pos_three_str = str(state_option_chosen["pos_three"].values[0])
    city_one_str = str(state_option_chosen["city_one"].values[0])
    city_two_str = str(state_option_chosen["city_two"].values[0])
    city_three_str = str(state_option_chosen["city_three"].values[0])

    return pos_one_str, \
           pos_two_str, \
           pos_three_str, \
           city_one_str, \
           city_two_str, \
           city_three_str\

@callback(
    Output('vaccination-graph', 'figure'), [Input('departamento-dropdown', 'value')])
def update_graph(selected_departamento):
    # Filter the data based on the selected department
    filtered_df = data[data['departamento'] == selected_departamento]

    # Calculate the V/I ratio for each year
    filtered_df['V/I'] = filtered_df['v'] / filtered_df['I']

    # Calculate the average V/I ratio for each year
    avg_v_i_ratio_by_year = filtered_df.groupby('year')['V/I'].mean().reset_index()

    # Create the line graph
    fig = px.line(avg_v_i_ratio_by_year, x='year', y='V/I', color_discrete_sequence=['blue'],
                  labels={'year': 'Year', 'V/I': 'Average V/I Ratio'})

    return fig
