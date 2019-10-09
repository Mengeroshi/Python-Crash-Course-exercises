import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

maximum = 10_000

filename = 'data/MODIS_C6_Central_America_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, lats, lons = [], [], []
    brightness, hover_texts = [], []
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        dates.append(date)
        lats.append(row[0])
        lons.append(row[1])

        bright = float(row[2])
        brightness.append(bright)

        label = f"{date.strftime('%d-%m-%Y')} - {bright}"

        hover_texts.append(label)

        count =+1
        #if count == maximum:
        #    break

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [bright/30 for bright in brightness],
        'color': brightness,
        'colorscale': 'YlOrRd',
        'reversescale': False,
        'colorbar': {'title': 'brightnesses'},
    },
}]

my_layout = Layout(title='Central Americal Fire Activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires_proof.html')