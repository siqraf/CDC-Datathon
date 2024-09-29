import pandas as pd
import folium
import requests
import json
import numpy as np
import webbrowser
import os


df = pd.read_csv('emissionsData.csv', low_memory=False)
df2 = pd.read_csv('world_population.csv', low_memory=False)


df2.columns = df2.columns.str.strip()

# Convert the 'TIME' column to numeric, forcing errors to NaN
df['TIME'] = pd.to_numeric(df['TIME'], errors='coerce')

# Merge population data into emissions data
df = df.merge(df2[['Country', 'Population']], on='Country', how='left')

# Create a new column 'EPC' (Emissions per Capita) by dividing 'Value' by 'Population'
df['EPC'] = df['Value'] / df['Population']

filtered_df = df[df['FREQUENCY'] == 'A']

# Group by LOCATION and TIME and sum the EPC column
result_df_filtered = filtered_df.groupby(['LOCATION', 'TIME', 'Country'], as_index=False)['EPC'].sum()

years = [2015, 2020, 2022]

geojsonURL = 'https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/world-countries.json'
response = requests.get(geojsonURL)
geoData = response.json()

# Function to generate and save map for a given year using EPC values
def generate_map_for_year(year):
    # Filter data for the selected year
    mapData = result_df_filtered[result_df_filtered['TIME'] == year][['LOCATION', 'EPC', 'Country']]
    
    # Merge the EPC data into the geojson data for tooltips
    for feature in geoData['features']:
        loc = feature['id'] 
        country_data = mapData[mapData['LOCATION'] == loc]
        if not country_data.empty:
            feature['properties']['EPC'] = round(country_data['EPC'].values[0], 4)
        else:
            feature['properties']['EPC'] = 'N/A'
    
    # Calculate the minimum and maximum EPC values for the year
    data_min = mapData['EPC'].min()
    data_max = mapData['EPC'].max()
    
    bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1, 2, 3, 10, 40, 106]

    m = folium.Map(location=[20, 10], zoom_start=2)
    
    folium.Choropleth(
        geo_data=geoData,
        name='choropleth',
        data=mapData,
        columns=['LOCATION', 'EPC'],
        key_on='feature.id',
        fill_color='RdYlGn_r',
        fill_opacity=0.7,
        line_opacity=0.0, 
        legend_name=f'Emissions per Capita in {year}',
        bins=bins, 
        reset=True
    ).add_to(m)
    
    # Add hover functionality
    folium.GeoJson(
        geoData,
        style_function=lambda feature: {
            'fillColor': '#ffffff00', 
            'color': 'black',  
            'weight': 2,  
            'fillOpacity': 0,
        },
        tooltip=folium.GeoJsonTooltip(
            fields=['name', 'EPC'],
            aliases=['Country:', 'EPC:'],
            localize=True,
            labels=True,
            sticky=True,
            toLocaleString=True,
            html=True
        )
    ).add_to(m)
    
    file_name = f'map_{year}_EPC.html'
    m.save(file_name)
    
    webbrowser.open('file://' + os.path.realpath(file_name))

for year in years:
    generate_map_for_year(year)
