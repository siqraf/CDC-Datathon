﻿# Analyzing CO2 emissions from air travel & predicting trends
## Inspiration
Climate change is one of the most pressing issues of our time, and understanding how global emissions contribute to it is crucial for taking effective action. We were inspired to build a tool that visualizes emissions data in a meaningful way, empowering individuals and policymakers to grasp the impact of carbon emissions. Additionally, we wanted to leverage machine learning to predict future trends, helping the world anticipate and mitigate future emissions.

## What it does
Our project provides an interactive map that visualizes global emissions per capita using a green-to-red gradient, making it easy to identify which countries are contributing most to carbon emissions. It also incorporates a machine learning-based linear regression model to predict future emission trends. Users can explore both past data and future forecasts to make informed decisions and drive climate action.

## How we built it
We collected emissions and population data from various open datasets, which were merged and analyzed using Python. We used **Folium** to build dynamic maps that display per capita emissions by country. The maps use a green-to-red gradient to represent emissions levels, making it visually intuitive. For predictive analysis, we trained a linear regression model to forecast future emissions trends, integrating this with the data visualization for a holistic view of global emissions.

## Challenges we ran into
One of the biggest challenges was cleaning and merging the datasets to ensure accurate and meaningful data representation. Some countries had missing or incomplete data, which required handling through interpolation or data sourcing from alternative providers. Another challenge was fine-tuning the color scheme to provide clear and distinct visualization without overwhelming the user.

## Accomplishments that we're proud of
We're proud of creating a user-friendly tool that not only displays global emissions but also forecasts future trends. The combination of interactive maps with machine learning-based predictions allows users to both explore the current state and prepare for what’s next. Successfully merging and analyzing large datasets while maintaining performance was another key accomplishment.
