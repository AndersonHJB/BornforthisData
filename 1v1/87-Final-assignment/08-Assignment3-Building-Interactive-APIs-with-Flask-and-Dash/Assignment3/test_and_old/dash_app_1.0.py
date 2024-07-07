# import dash
# import pandas as pd
# from dash import dcc, html, dash_table
# from dash.dependencies import Input, Output
#
# app = dash.Dash(__name__)
# # JO35YR__AdRXP1Nr4KCy
# # Load data (assuming a CSV file from the Winnipeg Open Data Portal)
# df = pd.read_csv('static/City_of_Winnipeg_LRS_20240707.csv')  # Ensure you have a CSV file named 'data.csv'
#
# # 检查df是否为空，适当调整初始化Dropdown的value
# initial_value = df.columns[0] if not df.empty else None
#
# app.layout = html.Div([
#     html.H1("Data Display from Winnipeg Open Data Portal"),
#     dash_table.DataTable(
#         id='table',
#         columns=[{"name": i, "id": i} for i in df.columns],
#         data=df.to_dict('records'),
#     ),
#     dcc.Graph(id='graph'),
#     dcc.Dropdown(
#         id='dropdown',
#         options=[{'label': i, 'value': i} for i in df.columns if df[i].dtype in ['float64', 'int64']],
#         value=initial_value
#     )
# ])
#
#
# @app.callback(
#     Output('graph', 'figure'),
#     [Input('dropdown', 'value')]
# )
# def update_graph(column_name):
#     if column_name is not None:
#         return {
#             'data': [{'x': df.index, 'y': df[column_name], 'type': 'line'}],
#             'layout': {'title': f'Graph of {column_name}'}
#         }
#     return {}
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
# import dash
# import pandas as pd
# from dash import dcc, html, dash_table, Input, Output
# import plotly.graph_objs as go  # 使用 Plotly 的图形对象
#
# app = dash.Dash(__name__)
#
# # 加载数据
# df = pd.read_csv('static/City_of_Winnipeg_LRS_20240707.csv')  # 确保有一个名为'data.csv'的文件，并且路径正确
#
# # 检查数据集是否为空，并适当设置下拉菜单的初始值
# initial_value = df.columns[0] if not df.empty and df.columns.size > 0 else None
#
# app.layout = html.Div([
#     html.H1("数据展示"),
#     dash_table.DataTable(
#         id='table',
#         columns=[{"name": i, "id": i} for i in df.columns],
#         data=df.to_dict('records'),
#     ),
#     dcc.Graph(id='graph'),
#     dcc.Dropdown(
#         id='dropdown',
#         options=[{'label': i, 'value': i} for i in df.columns if df[i].dtype in ['float64', 'int64']],
#         value=initial_value
#     )
# ])
#
# @app.callback(
#     Output('graph', 'figure'),
#     [Input('dropdown', 'value')]
# )
# def update_graph(column_name):
#     if column_name:
#         return {
#             'data': [go.Scatter(x=df.index, y=df[column_name], mode='lines+markers')],
#             'layout': go.Layout(title=f'图表：{column_name}', xaxis={'title': 'Index'}, yaxis={'title': column_name})
#         }
#     else:
#         return go.Figure()  # 如果没有有效的列名，返回一个空的图表
#
# if __name__ == '__main__':
#     app.run_server(debug=True)


import dash
import pandas as pd
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import plotly.express as px  # 引入绘图库

app = dash.Dash(__name__)

# 加载数据
df = pd.read_csv('static/City_of_Winnipeg_LRS_20240707.csv')  # 确保数据文件存在

# 设定初始图表列，优先选择数值类型的列
initial_column = df.select_dtypes(include=['float64', 'int64']).columns[0] if not df.empty else None

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
        value=initial_column
    )
])


@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_column):
    if selected_column:
        # 使用 Plotly Express 创建图表
        fig = px.line(df, x=df.index, y=selected_column, title=f'图表：{selected_column}')
        return fig
    # 如果没有有效列，默认返回空图表
    return {}


if __name__ == '__main__':
    app.run_server(debug=True)
