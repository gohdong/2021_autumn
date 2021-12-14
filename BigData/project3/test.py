import dash
from dash import dcc,html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd



df = px.data.gapminder()
kospi_df = pd.read_csv('kospi_sample_year.csv')
kosdaq_df = pd.read_csv('kosdaq_sample_year.csv') 
df2 = px.data.tips()
animations = {
    'Scatter': px.scatter(
        df, x="gdpPercap", y="lifeExp", animation_frame="year", 
        animation_group="country", size="pop", color="continent", 
        hover_name="country", log_x=True, size_max=55, 
        range_x=[100,100000], range_y=[25,90]),
    'KOSPI Test' : px.scatter(kospi_df, x="부채", y="자본", animation_frame="연도", 
        animation_group="종목", size="자산", color="업종", 
        hover_name="종목", log_x=True, size_max=100,
        range_x=[100000000,6.31E+15], range_y=[-5E+13,3E+14]),
    'KOSDAQ Test' : px.scatter(kosdaq_df, x="부채", y="자본", animation_frame="연도", 
        animation_group="종목", size="자산", color="업종", 
        hover_name="종목", log_x=True, size_max=100,
        range_x=[100000000,6.31E+15], range_y=[-5E+13,3E+14]),
    'KOSPI X축=매출 Y축=액면가 크기=자산' : px.scatter(kospi_df, x="매출액", y="액면가", animation_frame="연도", 
        animation_group="종목", size="자산", color="업종", 
        hover_name="종목", log_x=True, size_max=100,
        range_x=[100000000,6.31E+15], range_y=[-5E+13,3E+14]),    
    'KOSDAQ X축=매출 Y축=액면가 크기=자산' : px.scatter(kosdaq_df, x="매출액", y="액면가", animation_frame="연도", 
        animation_group="종목", size="자산", color="업종", 
        hover_name="종목", log_x=True, size_max=100,
        range_x=[100000000,6.31E+15], range_y=[-5E+13,1E+14]),    

    'KOSPI 업종별 매출액': px.bar(
        kospi_df, x="업종", y="매출액", color="업종", 
        animation_frame="연도", animation_group="종목", hover_name="종목",
        range_y=[0,500000000000000]),
    'KOSDAQ 업종별 매출액': px.bar(
        kosdaq_df, x="업종", y="매출액", color="업종",  hover_name="종목",
        animation_frame="연도", animation_group="종목", 
        range_y=[0,15000000000000]),
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