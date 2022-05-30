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