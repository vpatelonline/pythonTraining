import pandas as pd

# Load the CSV data
file_name = "D:\IT\Python\Meteorite_Landings.csv"
data = pd.read_csv(file_name)

# Remove rows with missing values in 'reclat' and 'reclong'
data = data.dropna(subset=['reclat', 'reclong'])

# Filter the data to include meteorite strikes between 1950 and 2010
filtered_data = data[(data['year'] >= 1950) & (data['year'] <= 2010)]

yearly_counts = filtered_data['year'].value_counts().sort_index()

import folium
#Create a Folium map with Stamen Toner base map

m = folium.Map(location=[0, 0], tiles='Stamen Toner', zoom_start=2)
#Add orange circle markers for each meteorite strike

for _, row in filtered_data.iterrows(): 
  folium.CircleMarker( location=[row['reclat'], 
  row['reclong']], radius=3, 
  color='orange', 
  fill=True, 
  fill_color='orange' ).add_to(m)

import matplotlib.pyplot as plt
# Create the line chart
plt.plot(yearly_counts.index, yearly_counts.values)
plt.xlabel('Years')
plt.ylabel('Meteor Strikes')
plt.title('Meteorite Strikes per Year (1950-2020)')

from dash import Dash, dcc, html
import plotly.graph_objs as go

# Initialize the Dash app
app = Dash(__name__)

# Convert the Folium map to HTML
map_html = m._repr_html_()

# Create a Plotly line chart from the Matplotlib chart
line_chart = go.Figure(go.Scatter(x=yearly_counts.index, y=yearly_counts.values, mode='lines'))
line_chart.update_layout(title='Meteorite Strikes per Year (1950-2020)', xaxis_title='Years', yaxis_title='Meteor Strikes')

# Define the layout of the Dash app
app.layout = html.Div([
    html.Div([html.Iframe(id='map', srcDoc=map_html, width='100%', height='600')], style={'width': '70%', 'display': 'inline-block'}),
    html.Div([dcc.Graph(id='line-chart', figure=line_chart)], style={'width': '30%', 'display': 'inline-block'})
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)