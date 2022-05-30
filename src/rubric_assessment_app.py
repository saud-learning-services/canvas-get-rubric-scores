import random
import pandas as pd
import json
import os
from helpers import create_instance

#canvasapi 
from canvasapi import Canvas

# DASH
from jupyter_dash import JupyterDash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Env details
from dotenv import load_dotenv
load_dotenv() 

URL = os.getenv('API_INSTANCE')
KEY = os.getenv('API_TOKEN')
COURSE_ID = os.getenv('COURSE_ID')
GRAPH_URL = f"{URL}/api/graphql"

canvas = create_instance(URL, KEY)

def app():

    # Get course id
    # once confirmed move to next step

    # 
    app = JupyterDash(__name__)

    app.layout = html.Div(
        children = [
            html.H1('Welcome!'),
            html.Div(
                children=[
                    html.H2('Input Course ID'),
                    html.Div(
                        children = [
                            dcc.Input(id='input-course-id', type='number', style={'display': 'inline-block'}),
                            html.Button('Submit', id='submit-course-id', n_clicks=0, style={'display': 'inline-block'})
                            ])]),
            html.Div(children='Enter your course id', id='course-details-display'),
            html.Div(children=[], id='confirmed-course')
        ], 
        id='initial-input-course')
        
    @app.callback(
        Output('course-details-display', 'children'),
        Input('submit-course-id', 'n_clicks'),
        State('input-course-id', 'value')
        )

    def update_output(n_clicks, value):
        if n_clicks > 0:

            try:
                course = canvas.get_course(value)
                return(
                    html.Div(children = [
                        html.P(f'You have selected: {course.name}', style={'color': 'green'}),
                        html.Button(f'Confirm {course.name}', id='confirm-course', n_clicks=0)
                    ])
                    )
            except Exception as err:
                return(
                    html.P(f'Error with course id {value}:\n{err}\nPlease submit another course id.', style={'color': 'red'})
                    )
            
        else:
            return(f'Please enter a course ID and press submit :D')

    @app.callback(
        Output('confirmed-course', 'children'),
        Input('confirm-course', 'n_clicks'),
        State('input-course-id', 'value')
    )

    def the_course_has_been_confirmed(n_clicks, value):
        if n_clicks >= 1:
            return('okay, we get it you want that course')


    app.run_server(mode='inline')

    

    

