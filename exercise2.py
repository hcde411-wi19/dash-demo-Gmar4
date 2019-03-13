# Garrett Mar
# HCDE 411
# Winter 2019
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

# static data
pokemon_name = ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Mewtwo',
               'Articuno']
attack_power = [49, 52, 48, 30, 20, 45, 35, 110, 85]
defense_power = [49, 43, 65, 35, 55, 50, 30, 90, 100]


# initialize Dash app and initialize the static folder
app = dash.Dash(__name__, static_folder='static')
# set layout of the page
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Pokemon Attack/Defense Scatterplot'),

    # set the description underneath the heading
    html.Div(children='''
        Garrett Mar - HCDE 411
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='exercise-2',
        figure={
            # configure the data
            'data': [
                # This is how we define a scatter plot. Note that it also uses "go.Scatter",
                # but with the mode to be only "markers"
                go.Scatter(
                    x=defense_power, # x-axis values to defense_power array
                    y=attack_power, # y-axis values to attack_power array
                    mode='markers',
                    text=pokemon_name,  # Set dots to specific pokemon names
                    marker={
                        'size': 15,
                        'opacity': 0.8  # By making the points a bit transparent, it can alleviate the occlusion issue
                    }
                )
            ],
            'layout': {
                'title': 'Pokemon Defense vs. Attack Power',
                # Create X axis as Defense Power
                # Create Y axis as Attack Power
                'xaxis': {'title': 'Defense Power'},
                'yaxis': {'title': 'Attack Power'},
            }
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)

# Exercise 2
