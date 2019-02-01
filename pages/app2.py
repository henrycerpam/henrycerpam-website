import dash
from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from .side_bar import sidebar
from sklearn.linear_model import LogisticRegression
import plotly.graph_objects as go

dash.register_page(__name__, name="Cannabis Legal Market", title='Cannabis Legal Market')

df = pd.read_csv('https://raw.githubusercontent.com/henrycerpa/database/main/CannabisSalesByCounty.csv')
data = pd.read_csv('https://raw.githubusercontent.com/henrycerpa/database/main/midwestern_hemp.csv')
data = data.sort_index()

# Calculate high THC failures (0 for pass, 1 for failure).
data['fail'] = (data['total_thc'] >= 0.3).astype(int)

# Create dummy variables for categorical features.
X = pd.get_dummies(data[['state', 'county', 'sample_date']])

# Target variable
y = data['fail']

# Train the logistic regression model
logreg = LogisticRegression()
logreg.fit(X, y)


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
                                'Understanding market trends and sales is crucial in legal cannabis market. In this case, being aware of market trends and sales data allows businesses to identify consumer preferences, anticipate demand and adjust their production and distribution accordingly.'],
                                style={'color': 'BLACK', 'font-size': '15px'})
                        ], style={'width': '180%'}),
                    ], className='footer', style={'display': 'flex'}),

                    html.Div([
                        html.H3("Select a County"),

                        dcc.Dropdown(
                            id='county-dropdown',
                            options=[{'label': county, 'value': county} for county in df['County'].unique()],
                            value=df['County'].unique()[0]
                        ),
                        dcc.Graph(id='sales-graph')
                    ],className='box', style={'padding-bottom': '15px'}),

                    html.Div([
                        html.Div([
                            html.P([
                                'Introducing the "Hemp Failure Rate Prediction" tool: This allows you to predict the failure rate of hemp samples based on state, county, and sample date information. Simply enter the relevant details and click the button to get the predicted failure rate.'],
                                style={'color': 'BLACK', 'font-size': '15px'})
                        ], style={'width': '180%'}),
                    ], className='footer', style={'display': 'flex'}),


                    html.Div([
                        html.Div([
                            html.Label("Select a State"),
                            dcc.Dropdown(
                                id='state-dropdown',
                                options=[{'label': state, 'value': state} for state in data['state'].unique()],
                                value='Wisconsin'
                            ),
                        ]),
                        dcc.Graph(id='prediction-graph')
                    ],className='box', style={'padding-bottom': '15px'})

                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])


@callback(
    dash.dependencies.Output('sales-graph', 'figure'),
    [dash.dependencies.Input('county-dropdown', 'value')]
)
def update_graph(selected_county):
    filtered_data = df[df['County'] == selected_county]
    filtered_data['YearQuarter'] = filtered_data['Calendar Year'].astype(str) + ' Q' + filtered_data['Quarter'].astype(
        str)
    filtered_data = filtered_data.sort_values('YearQuarter')  # Ordenar los valores en el eje X
    fig = px.line(filtered_data, x='YearQuarter', y='Per Capita Sales', color='County')
    fig.update_layout(
        title='Per Capita Cannabis Sales by County in California',
        yaxis={'title': 'Per Capita Sales'},
        xaxis={'type': 'category'}  # Especificar que los valores en el eje X sean tratados como categorías
    )
    return fig

@callback(
    dash.dependencies.Output('prediction-graph', 'figure'),
    [dash.dependencies.Input('state-dropdown', 'value')]
)
def update_prediction_graph(state):
    if state:
        county_predictions = []
        for county in data[data['state'] == state]['county'].unique():
            input_data = pd.DataFrame({'state': [state], 'county': [county]})
            input_data = pd.get_dummies(input_data)  # Create dummy variables
            input_data = input_data.reindex(columns=X.columns, fill_value=0)  # Align columns with training data
            prediction = logreg.predict_proba(input_data)[:, 1]  # Probability of failure (class 1)
            county_predictions.append({'county': county, 'prediction': prediction[0]})

        county_predictions_df = pd.DataFrame(county_predictions)

        fig = go.Figure(data=go.Bar(x=county_predictions_df['county'], y=county_predictions_df['prediction']))
        fig.update_layout(
            title=f"Hemp Failure Rate Predictions by County - State: {state}",
            xaxis_title=f"{state}",
            yaxis_title="Failure Rate",
        )

        return fig
