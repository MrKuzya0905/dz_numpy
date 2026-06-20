# df = pd.DataFrame({
#     'Category': ['A', 'B', 'C', 'D'],
#     'Values': [23, 17, 35, 29]
# })
# fig = px.bar(df, x='Category', y='Values', title='Стовпчаста діаграма для поділу та публікації')
# fig.write_html("bar_chart.html")
# fig.write_image("bar_chart.png"



# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd

# app = dash.Dash(__name__)
# df = pd.DataFrame({
#     'Month': ['January', 'February', 'March', 'April'],
#     'Sales': [5000, 7000, 6000, 8000],
#     'Expenses': [3000, 4000, 3500, 4500]
# })
# app.layout = html.Div([
#     html.H1("Дашборд Продажів та Витрат"),
#     dcc.Dropdown(
#         id='department-dropdown',
#         options=[
#             {'label': 'Продажі', 'value': 'Sales'},
#             {'label': 'Витрати', 'value': 'Expenses'}
#         ],
#         value='Sales',
#         clearable=False
#     ),
#     dcc.Graph(id='bar-chart')
# ])

# @app.callback(
#     Output('bar-chart', 'figure'),
#     [Input('department-dropdown', 'value')]
# )
# def update_chart(selected_metric):
#     fig = px.bar(df, x='Month', y=selected_metric, title=f'{selected_metric} за Місяцями')
#     return fig

# if __name__ == '__main__':
#     app.run(debug=True)





# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output, State
# import plotly.express as px
# import pandas as pd
# import io
# import base64

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1("Дашборд з Завантаженням Даних"),
#     dcc.Upload(
#         id='upload-data',
#         children=html.Div([
#             'Перетягніть або ',
#             html.A('виберіть файли')
#         ]),
#         style={
#             'width': '100%',
#             'height': '60px',
#             'lineHeight': '60px',
#             'borderWidth': '1px',
#             'borderStyle': 'dashed',
#             'borderRadius': '5px',
#             'textAlign': 'center',
#             'margin': '10px'
#         },
#         multiple=False
#     ),
#     dcc.Graph(id='uploaded-graph')
# ])

# def parse_contents(contents, filename):
#     content_type, content_string = contents.split(',')
#     decoded = base64.b64decode(content_string)
#     try:
#         if 'csv' in filename:
#             df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
#         elif 'xls' in filename:
#             df = pd.read_excel(io.BytesIO(decoded))
#         else:
#             return None
#     except Exception:
#         return None
#     return df

# @app.callback(
#     Output('uploaded-graph', 'figure'),
#     [Input('upload-data', 'contents')],
#     [State('upload-data', 'filename')]
# )
# def update_output(contents, filename):
#     if contents is not None:
#         df = parse_contents(contents, filename)
#         if df is not None and 'X' in df.columns and 'Y' in df.columns:
#             fig = px.scatter(df, x='X', y='Y', title='Завантажений Графік')
#             return fig
#     return {}

# if __name__ == '__main__':
#     app.run(debug=True)