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
