from canvasapi import Canvas
import util
import sys

def create_instance(API_URL, API_KEY):
    try:
        canvas = Canvas(API_URL, API_KEY)
        util.print_success("Token Valid: {}".format(str(canvas.get_user('self'))))
        return(canvas)
    except Exception as e:
        util.print_error("\nInvalid Token: {}...\n{}".format(API_KEY[0:12], str(e)))
        #sys.exit(1)
        #raise