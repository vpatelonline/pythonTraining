from dash import Dash, html
import dash_bootstrap_components as dbc


navbar=dbc.NavbarSimple(
    brand='Soccer Player Dashboard',
    children=[
        html.Img(src='https://uptime.com/media/website_profiles/sofifa.com.png',
                 height=20),
        html.A('Data Source',
               href='https://sofifa.com',
               target='_blank',
               style={'color': 'black'})
            ],
    color='primary',
    fluid=True
)

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout=html.Div(navbar)

if __name__ == '__main__':
    app.run_server(debug=True)

