from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('CANVAS_API_TOKEN')

# Canvas object to provide access to Canvas API
COURSE = None

# Assignment object representing Canvas assignment specified by user input
ASSIGNMENT = None
