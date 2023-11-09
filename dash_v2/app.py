# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from plotly import graph_objects as go
from loader import Loader



# Incorporate data
dataset = Loader()

# Ingest and separate datasets
dataset.read('dashv2.csv')

# Figures


# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
    html.Div(className='row', children='My First App with Data, Graph, and Controls',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'}, style_cell={'align-items': 'center'})
        ]),

        html.Div(className='six columns', children=[
            dcc.Graph(figure = go.Figure(go.Funnel(
                y = ["Leads", "Calls", "Pitches", "Deals"],
                x = [dataset.leads_count, dataset.calls_count, dataset.pitches_count, dataset.deals_count],
                textinfo = "value+percent initial"
                ))
            )
        ]),
    ]),

    html.Div(className='row', children=[
    dcc.RadioItems(options=['leads', 'calls', 'pitches', 'deals'],
                    value='leads',
                    inline=True,
                    id='my-radio-buttons-final')
    ]),

    html.Div(className='row', children=[
        dcc.Graph(figure={}, id='histo-chart-final')
    ])
])

# Add controls to build the interaction
@callback(
    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='date', y=col_chosen, histfunc='sum')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
