import dash
import pandas as pd
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
# JO35YR__AdRXP1Nr4KCy
# Load data (assuming a CSV file from the Winnipeg Open Data Portal)
df = pd.read_csv('static/City_of_Winnipeg_LRS_20240707.csv')  # Ensure you have a CSV file named 'data.csv'

# 检查df是否为空，适当调整初始化Dropdown的value
initial_value = df.columns[0] if not df.empty else None

app.layout = html.Div([
    html.H1("Data Display from Winnipeg Open Data Portal"),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    dcc.Graph(id='graph'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df.columns if df[i].dtype in ['float64', 'int64']],
        value=initial_value
    )
])


@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(column_name):
    if column_name is not None:
        return {
            'data': [{'x': df.index, 'y': df[column_name], 'type': 'line'}],
            'layout': {'title': f'Graph of {column_name}'}
        }
    return {}


if __name__ == '__main__':
    app.run_server(debug=True)
