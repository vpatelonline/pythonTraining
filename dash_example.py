from dash import Dash,html

app=Dash()

app.layout = html.Div("My Dashboard 3")

if __name__ == '__main__':
    app.run_server(debug=True)
