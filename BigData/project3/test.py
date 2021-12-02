import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import jupyterlab_dash

viewer = jupyterlab_dash.AppViewer()
df = px.data.gapminder()
df1 = pd.read_csv('data/sample.csv')

animations = {
    'Scatter': px.scatter(
        df, x="gdpPercap", y="lifeExp", animation_frame="year", 
        animation_group="country", size="pop", color="continent", 
        hover_name="country", log_x=True, size_max=55, 
        range_x=[100,100000], range_y=[25,90]),
    'Test' : px.scatter(df1, x="avg_salary", y="employee_num", animation_frame="time", 
        animation_group="name", size="price", color="type", 
        hover_name="name", log_x=True, size_max=55,
        range_x=[20000000,50000000], range_y=[-100,1000]),
    # 'Bar': px.bar(
    #     df, x="continent", y="pop", color="continent", 
    #     animation_frame="year", animation_group="country", 
    #     range_y=[0,4000000000]),
}

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.RadioItems(
        id='selection',
        options=[{'label': x, 'value': x} for x in animations],
        value='Scatter'
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("selection", "value")])
def display_animated_graph(s):
    return animations[s]

app.run_server(debug=True)