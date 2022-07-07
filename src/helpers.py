"""Module that handles calling the Canvas API and creating the rubric assessment
data table.

This module exports the following functions:
    create_instance - creates a Canvas instance with URL and access token.
    return_single_dict_match - returns a single match in a dictionary.
    get_output_data - compiles submission and rubric assessment details into one
                      dictionary.

An exception is raised when the Canvas access token in create_instance is invalid.
The function prints an indicative message instead of proceeding.
"""

from canvasapi import Canvas
import util


def create_instance(API_URL, API_KEY):
    """Creates a Canvas instance using provided URL and access token.

    parameters:
        API_URL (string): URL for instance
        API_KEY (string): access token

    returns:
        access to Canvas API
    
    exceptions:
        If access token is invalid, prints a message indicating that the token is
        invalid.
    """
    try:
        canvas = Canvas(API_URL, API_KEY)
        util.print_success("Token Valid: {}".format(str(canvas.get_user("self"))))
        return(canvas)

    except Exception as e:
        util.print_error("\nInvalid Token: {}...\n{}".format(API_KEY[0:12], str(e)))


def _matches_dict_key_val(dict_, key, matches_val):
    """Return the dictionary if the provided key matches the match_val.
    
    parameters:
        dict_ (dict): dictionary to look through
        key (string): the key string in the dictionary to find
        matches_val (str|int): the str or int to try to find in the key

    returns:
        boolean
    """
    return(dict_[f"{key}"] == matches_val)


def return_single_dict_match(some_list, match_key, match_val):
    """Return a single match in a dictionary.

    parameters:
        some_list (dict)
        match_key (string): the key string in the dict to find
        matche_val (str|int): the str or int to try to find in the key

    returns:
        out (dict): dictionary pair
    """
    out = [d for d in some_list if _matches_dict_key_val(d, match_key, match_val)][0]
    return(out)

def get_course_assignment_info(course_info):
    """Return a dictionary with the course id, course name, and assignment name.

    parameters:
        course_info (json?)
    
    returns:
        course_and_assignment_dict (dict)
    """
    course_and_assignment_dict = {"course_id":  course_info.get["_id"],
                                  "course_name":  course_info.get["name"],
                                  "assignment_name": course_info.get["assignmentsConnection"].get["nodes"].get["name"],
    }
    return course_and_assignment_dict

def __get_assessment_criteria_scores(assessment_rating):
    # Create a dictionary which includes assessment criteria and points assigned
    criteria = assessment_rating.get("criterion").get("description")
    ratings_dictionary = {criteria: assessment_rating.get("points")}
    return(ratings_dictionary)

def _get_rubric_assessment_details(rubric_assessment):
    # Append assessment and assessor details to criteria and points
    rubric_assessment_dict = {
        "assessment_id": rubric_assessment.get("_id"),
        "assessor_name": rubric_assessment.get("assessor").get("name"),
        "assessor_id": rubric_assessment.get("assessor").get("_id")
    }

    ratings = rubric_assessment.get("assessmentRatings")

    for i in ratings:
        rubric_assessment_dict.update(__get_assessment_criteria_scores(i))
    
    return(rubric_assessment_dict)
    
def _get_submission_details(submission):
    # Create a dictionary including student information and submission details.
    user = submission.get("user")
    
    submission_dict = {"user_id":  user["_id"],
                       "user_name":  user["name"],
                       "user_sis_id": user["sisId"],
                       "user_score": submission["score"],
                       "submission_attempt": submission["attempt"],
                       "submission_timestamp": submission["submittedAt"],
                       "submission_status": submission["submissionStatus"]
    }   
    
    return(submission_dict)    


def get_output_data(submissions):
    """Compile submission and rubric assessment details into one dictionary.
    
    arguments:
        submissions (list): list containing all rubric submissions
    
    returns:
        output_data (dict): table containing all elements of rubric assessment
    """
    output_data = []

    for i in submissions:   
        
        
        rubric_assessments = i.get("rubricAssessmentsConnection").get("nodes")

        for j in rubric_assessments:
            new_dict = {}
            new_dict.update(_get_submission_details(i))
            new_dict.update(_get_rubric_assessment_details(j))
            output_data.append(new_dict)
        
    return(output_data)

