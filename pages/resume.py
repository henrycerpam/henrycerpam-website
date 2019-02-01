import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0, name="Resume")

image_path = 'https://raw.githubusercontent.com/henrycerpa/database/main/profile.png'
logo_one = 'https://raw.githubusercontent.com/henrycerpa/database/main/glare.png'
logo_two = 'https://raw.githubusercontent.com/henrycerpa/database/main/monkum.png'
logo_three = 'https://raw.githubusercontent.com/henrycerpa/database/main/mercedes.png'
logo_four = 'https://raw.githubusercontent.com/henrycerpa/database/main/zara.png'

layout = html.Div([




    dbc.Row(
        [
            dbc.Col(html.Img(src=image_path,
                    style={'position': 'center', 'width': '10%', 'left': '50px', 'top': '50px'}), style={'textAlign': 'center'}, width=0),
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('An Industrial Engineer, bringing experience in data wrangling, statistical analysis and reporting to the table. \n '
                                'My expertise in numerical simulation, utilizing various techniques and Python libraries, \n '
                                'coupled with my proficiency in data visualization tools make me a valuable asset.\n'
                                'My passion for artificial intelligence developments drives my desire \n'
                                'to stay current with industry trends and advancements.\n', style={'textAlign': 'center', 'white-space': 'pre'},
                             className='ms-3'), width=0)
        ]),

        dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'left'}), width=4),
            dbc.Col(dcc.Markdown('## Experience', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [   dbc.Col(html.Img(src=logo_two),
                    style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
            dbc.Col(dcc.Markdown('### Data Specialist \n'
                             '##### Monkum Group \n'
                             'Since Nov/21\n', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('Develops a data analysis tool for modeling brucellosis disease behavior and predictions,\n'
                                'optimizing vaccine inventory to critical points. Also, successfully led a data visualization\n'
                                'tool migration, resulting in an 81% reduction in client costs. \n'
                                 'TECHNOLOGIES: \n'
                                 '◾Programming Languages: Python\n'
                                 '◾Declarative Language: SQL\n'
                                 '◾Spreadsheet Applications: Excel, Google Sheets\n'
                                 '◾Libraries: Pandas, Numpy, GeoJson, Dash, Plotly, Scipy , Matplotlib, Scikit-Learn\n'
                                 '◾Data visualization: Dash - Plotly, PowerBi\n'
                                 '◾Models used: Inventory management models, Discrete event simulation, Agent-based modeling\n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),

    dbc.Row(
        [   dbc.Col(html.Img(src=logo_two),
                    style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
            dbc.Col(dcc.Markdown('### Data Analyst \n'
                                 '##### Monkum Group \n'
                                 'May/19 - Oct/21 \n', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('Automated processes and distribution in a hard discount store, from warehouses to\n'
                                'physical stores and the end customer. Achieved through cross-referencing and analyzing\n'
                                'database files (Excel, CSV) using Python, resulting in a significant reduction \n'
                                'of delivery time from days to hours\n'
                                 'TECHNOLOGIES: \n'
                                 '◾Programming Languages: Python\n'
                                 '◾Spreadsheet Applications: Excel, Google Sheets\n'
                                 '◾Libraries: Pandas, Numpy, Matplotlib, Scikit-Learn\n'
                                 '◾Data visualization: Tableu \n'
                                 '◾Models used: Asset-liability management\n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),

    dbc.Row(
        [dbc.Col(html.Img(src=logo_two),
                 style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
         dbc.Col(dcc.Markdown('### Digital Forensic Auditor \n'
                              '##### Monkum Group \n'
                              'Mar/16 - Apr/19 \n', style={'textAlign': 'right'}), width=2),
         dbc.Col(dcc.Markdown('Recovery of $912 million COP from the analysis of transactional data. \n'
                              'TECHNOLOGIES: \n'
                              '◾Data Processing App: SAP \n'
                              '◾Spreadsheet Applications: Excel\n'
                              '◾Data visualization: Dashboard in Excel \n'
                              '◾Models used: Monte Carlo simulation\n'
                              '---------------------------------------- \n', style={'white-space': 'pre'},
                              className='ms-3'), width=7)
         ]),

    dbc.Row(
        [dbc.Col(html.Img(src=logo_three),
                 style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
         dbc.Col(dcc.Markdown('### Audit Coordinator \n'
                              '##### Daimler Colombia \n'
                              'Oct/14 - Dec/15 \n', style={'textAlign': 'right'}), width=2),
         dbc.Col(dcc.Markdown('Reduced inventory shrinkage from 8% to 1.4% in the imported parts warehouse \n'
                              'for Mercedes Benz vehicles through the implementation of controls and monitoring \n'
                              'TECHNOLOGIES: \n'
                              '◾Data Processing App: SAP \n'
                              '◾Spreadsheet Applications: Excel\n'
                              '◾Data visualization: Dashboard in Excel \n'
                              '---------------------------------------- \n', style={'white-space': 'pre'},
                              className='ms-3'), width=7)
         ]),

    dbc.Row(
        [dbc.Col(html.Img(src=logo_four),
                 style={'position': 'relative', 'width': '10%', 'left': '0px', 'top': '0px'}, width=2),
         dbc.Col(dcc.Markdown('### Auditor \n'
                              '##### Texmoda \n'
                              'Jun/11 - Nov/13 \n', style={'textAlign': 'right'}), width=2),
         dbc.Col(dcc.Markdown('Reduced shrinkage from 4.3% to 0.6% in physical stores through implemented controls \n'
                              'and cross-referencing temporary transaction movements between 47 warehouses located \n'
                              'in Colombia, Peru and Ecuador.\n'
                              'TECHNOLOGIES: \n'
                              '◾Spreadsheet Applications: Excel\n'
                              '◾Data visualization: Dashboard in Excel \n', style={'white-space': 'pre'},
                              className='ms-3'), width=7)
         ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
            dbc.Col(dcc.Markdown('## Certifications', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'white-space': 'pre'},
                                 className='ms-3'), width=2),
            dbc.Col(html.Div('Jul/22', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Data Science \n'
                                 'Correlation One \n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),


    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'white-space': 'pre'},
                                 className='ms-3'), width=2),
            dbc.Col(html.Div('Jun/22', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Computing and Machine Learning in the Cloud with AWS \n'
                                 'Platzi \n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'white-space': 'pre'},
                                 className='ms-3'), width=2),
            dbc.Col(html.Div('May/22', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Deep Learning with Python \n'
                                 'Platzi \n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),




    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'white-space': 'pre'},
                                 className='ms-3'), width=2),
            dbc.Col(html.Div('Dec/21', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Programming Skills on Web Apps \n'
                                 'Universidad del Norte \n', style={'white-space': 'pre'},
                                 className='ms-3'),
                    width=7)
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
            dbc.Col(dcc.Markdown('## Skills', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [

            dbc.Col([dcc.Markdown('''
                * Python
                * SQL
                * ETL Process
                * Predictive Modeling
                ''')], ),
            dbc.Col([dcc.Markdown('''
                * Power Bi
                * Dash
                * Tableu
                * Excel
                ''')], ),
            dbc.Col([dcc.Markdown('''
                * Attention to Detail
                * Statistical Knowledge
                * Communication Skills
                * Time management
                ''')], ),

        ]
    ),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
            dbc.Col(dcc.Markdown('## Education', style={'color':'#e27f04', 'textAlign': 'center', 'white-space': 'pre'},
                                 className='ms-3')),
            dbc.Col(dcc.Markdown('----------------------------------------', style={'color':'#e27f04', 'textAlign': 'right'}), width=4),
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'textAlign': 'left'}), width=2),
            dbc.Col(html.Div('Dec/04', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Industrial Engineer \n'
                                 'Universidad del Atlantico (Barranquilla - CO)\n'
                                 '---------------------------------------- \n', style={'white-space': 'pre'},
                                 className='ms-3'), width=7)
        ]),

    dbc.Row(
        [
            dbc.Col(dcc.Markdown('', style={'textAlign': 'left'}), width=2),
            dbc.Col(html.Div('Mar/16', style={'textAlign': 'right'}), width=2),
            dbc.Col(dcc.Markdown('##### Internal Control \n'
                                 'Universidad Militar Nueva Granada (Bogota - CO)\n', style={'white-space': 'pre'},
                                 className='ms-3'),
                    width=7)
        ]),

])
