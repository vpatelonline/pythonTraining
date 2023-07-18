from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

electricity=pd.read_csv('electricity.csv')

year_min=electricity['Year'].min()
year_max=electricity['Year'].max()

app=Dash(external_stylesheets=[dbc.themes.SOLAR])

app.layout=html.Div([
    html.H1('Electricity Price By US States'),
    dcc.RangeSlider(id='year_slider',
                    min=year_min,
                    max=year_max,
                    value=[year_min,year_max],
                    marks={i:str(i) for i in range(year_min,year_max+1)}),

    dcc.Graph(id='map-graph'),
    dash_table.DataTable(id='price-info',
                         data=electricity.to_dict('records'))
])

@app.callback(
    Output('map-graph','figure'),
    Input('year_slider','value')
)
def update_map_graph(selected_year):
    filtered_electricity=electricity[
        (electricity['Year']>=selected_year[0]) &
        (electricity['Year']<=selected_year[1])   
    ]
    avg_price_electricity=filtered_electricity.groupby('US_State')['Residential Price'].mean().reset_index()

    map_fig=px.choropleth(avg_price_electricity,
                      locations='US_State',locationmode='USA-states',
                      color='Residential Price', color_continuous_scale='reds')
    return map_fig
if __name__ == '__main__':
    app.run_server(debug=True)

