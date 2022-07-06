"""Module that handles the display and interaction with the script.

This module raises the exception PreventUpdate when it counters a lack
of data for a display of a rubric assessment or a .csv download.
"""

import os
import sys
module_path = os.path.abspath(os.path.join("src/"))
if module_path not in sys.path:
    sys.path.append(module_path)
import pandas as pd

# canvasapi 
from canvasapi import Canvas

# DASH
from jupyter_dash import JupyterDash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Local imports
from helpers import create_instance, return_single_dict_match, get_output_data
from initial_requests import get_initial_info

# Environment details
from dotenv import load_dotenv
load_dotenv() 

URL = os.getenv("API_INSTANCE")
KEY = os.getenv("API_TOKEN")
GRAPH_URL = f"{URL}/api/graphql"

print(GRAPH_URL)

canvas = create_instance(URL, KEY)


def _drop_down_div(list_of_dicts, dropdown_id, div_id):
    # Create an HTML dropdown list of a given dictionary
    first_value = list_of_dicts[0].get("value")
    
    html_div = html.Div([
        dcc.Dropdown(options=list_of_dicts, value=first_value, id=dropdown_id),
        html.Div(id=div_id)
    ])
    
    return(html_div)

def app():
    ''' Format page and allow user to interact.  Confirm course id first.
    Select and show assignments and associated rubrics.  Allow download 
    of rubric .csv file.
    '''
    app = JupyterDash(__name__)
    app.config.suppress_callback_exceptions = True

    app.layout = html.Div(
        children = [
            html.H1("Welcome!"),
            html.Div(
                children=[
                    html.H2("Input Course ID:"),
                    html.Div(
                        children = [
                            dcc.Input(id="input-course-id", type="number"),
                            html.Button("Submit", id="submit-course-id",
                                        n_clicks=0
                            )
                        ]
                    )
                ]
            ),
            html.Div(children="Enter your course id",
                     id="course-details-display"
            ),
            html.Div(children=[], id="confirmed-course"),
        ], 
        id="initial-input-course"
    )
        
    @app.callback(
        Output("course-details-display", "children"),
        Input("submit-course-id", "n_clicks"),
        State("input-course-id", "value")
    )

    def access_canvas(n_clicks, value):
        # Confirm access token validity.
        # Query user for details to access Canvas course information.
        if canvas==None:
            return(
                html.P(f"""Error creating session. Confirm you have an active 
                token and a green confirmation at the top noting 'Token Valid: 
                ... '""", style={"color": "red"})
            )

        if n_clicks > 0:
            try:
                course = canvas.get_course(value)
                return(
                    html.Div(children = [
                        html.P(f"You have selected: {course.name}",
                               style={"color": "green"}),
                        html.Button(f"Confirm {course.name}",
                                    id="confirm-course", n_clicks=0),
                        dcc.Store(id="course-data")
                        ]
                    )
                )
            except Exception as err:
                return(
                    html.P(f"""Error with course id {value}:\n{err}\nPlease 
                    submit another course id.""", style={"color": "red"})
                )
            
        else:
            return(html.P("Please enter a course ID and press submit :D"))

    @app.callback(
        [Output("confirmed-course", "children"),
         Output("course-data", "data")],
        Input("confirm-course", "n_clicks"),
        State("input-course-id", "value")
    )

    def course_is_confirmed(n_clicks, value):
        # Display list of assignments in confirmed course
        if n_clicks >= 1:
            data = get_initial_info(GRAPH_URL, int(value), KEY)
            assignments = data["data"]["course"]["assignmentsConnection"]["nodes"]
            #TODO only return assignments with rubrics in list
            assignments_list = [{"label": i.get("name"), "value": i.get("_id")}
                                for i in assignments
            ]

            new_div = html.Div(
                children=[
                    html.H2("Select Assignment:"),
                    _drop_down_div(assignments_list, "assignments-dropdown",
                                  "assignments-dropdown-container"),
                    html.Div(children=[], id="selected-assignment"), 
                    dcc.Store(id="reviews-data")
                ],
                id="assignments-selection-container"
            )
            
            return(new_div, data)

        else:
            raise PreventUpdate

    @app.callback(
        [Output("selected-assignment", "children"), Output("reviews-data", "data")],
        [Input("assignments-dropdown", "value"), Input("course-data", "data")]
    )

    def show_selected_assignment(assignment_value, data):
        # Display dataframe for user-selected assignment
        if data is None:
            raise PreventUpdate

        else:
            assignments_info = data["data"]["course"]["assignmentsConnection"]["nodes"]
            assignment = return_single_dict_match(assignments_info, "_id", str(assignment_value))

            assignment_name = assignment.get("name")
            rubric = assignment.get("rubric")

            if rubric is None:
                return(html.P("No rubric found for this assignment.", id='no-rubric-message'), None)

            else:    
                rubric_title = rubric.get("title")

                try:
                    #TODO show submissions count
                    #TODO show users with no submissions
                    #TODO check for incomplete rubrics
                    submissions = assignment.get("submissionsConnection").get("nodes")

                    reviews_list = get_output_data(submissions)                    

                    df = pd.DataFrame(reviews_list)

                    new_html = html.Div([
                        html.Br(),
                        html.H3(f"Selected Assignment: {assignment_name} (ID: {assignment_value})"),
                        html.H3(f"Rubric: {rubric_title}"),
                        dash_table.DataTable(
                            df.to_dict("records"),
                            [{"name": i, "id": i} for i in df.columns],
                            id="rubric-datatable"
                        ),
                        html.Div([
                            html.Button("Download CSV", id="csv_download_button", n_clicks=0),
                            dcc.Download(id="download-dataframe-csv"),
                            html.Div(children=[], id="final-output-container")
                            ])
                        ], id="returning-assignment-details"
                    )

                    return(new_html, reviews_list)

                except Exception as err:
                    return(
                        html.Div([
                            html.H2(f"""{assignment_name} ({assignment_value})"""),
                            html.H3(f"Rubric: {rubric_title}"), 
                            html.P(f"This rubric has no assessment data. {err}")
                            ]),
                            None
                    )

    @app.callback(
        Output("final-output-container", "children"),
        Output("download-dataframe-csv", "data"),
        Input("reviews-data", "data"),
        Input("csv_download_button", "n_clicks"),
        prevent_initial_call=True
    )

    def save_csv(reviews_data, button_clicks):
        # Download .csv file of dataframe
        if reviews_data is None:
            raise PreventUpdate

        elif button_clicks > 0:
            df = pd.DataFrame(reviews_data)
            csv_name = "my_csv.csv"
            return(
                f"Complete! See csv: {csv_name}",
                dcc.send_data_frame(df.to_csv, csv_name)
            )
        
        else:
           raise PreventUpdate

    app.run_server(mode="inline")

