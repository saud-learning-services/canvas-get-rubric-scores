from canvasapi import Canvas
from art import tprint
import settings
import getpass
from interface import get_user_inputs

def _get_course_rubrics(course):
    rubrics = course.get_rubrics()
    return(rubrics)

def _get_assignment_submissions(assignment):
    submissions = assignment.get_submissions(include="full_rubric_assessment")
    return(submissions)

def _get_submission_rubrics(submissions):
    results = []

    for i in submissions:
        r = {'user_id': i.user_id, \
             'submission_id': i.id, \
             'rubric': i.__dict__.get('full_rubric_assessment')
        }
        results.append(r)

    return(results)

def main():
    try: 
        base_url = 'https://ubc.instructure.com'
        
        if settings.TOKEN:
            token = settings.TOKEN   
        else:
            token = getpass.getpass('Please input your Canvas API Token')
            
        
        get_user_inputs(base_url, token)
        rubric_results = _get_submission_rubrics(_get_assignment_submissions(settings.ASSIGNMENT))

        print(rubric_results)

    except Exception as e:
        print('Whoops, something went wrong. Check your setup has been done correctly.') # only worry about this if it prints below
        print('\nERROR:')
        print(str(e))

if __name__ == "__main__":
    main()