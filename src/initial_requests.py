"""Module that handles initial course authorization requests.

This module exports the following functions:
    get_initial_info - sends a query for Canvas assessment details.

An exception is raised when the user is not authorized for the course 
they are trying to access. The function prints an indicative message 
instead of proceeding.
"""

# uses GRAPH QL

import requests

def _get_query_by_course(url, query, course_id, KEY):
    # Return answer to query for course information if user is authorized.
    # Print error if user us not authorized to access the course.   
    r = requests.post(
        url, json={"query": query, "variables": {"id": f"{course_id}"}},
        headers={"Authorization": f"Bearer {KEY}"}
    )

    if r.status_code == 200:
        return(r.json())
    
    else:
        print(f"Error: {r.json()}")


def get_initial_info(url, course_id, KEY):
    """Send initial query for Canvas assessment information.
    
    parameters:
        url (str): URL of Canvas instance
        course_id (int): integer indicating the course number
        KEY (str): access token for authorization
    returns:
        all_json: json encoded response

    exceptions:
        If the user is not authorized to access that course, print a message.
    """
    query = """query($id: ID){
        __typename
        course(id: $id) {
            id
            _id
            name
            assignmentsConnection {
                nodes {
                    _id
                    name
                    dueAt
                    expectsSubmission
                    pointsPossible
                    state
                    rubric {
                        id
                        pointsPossible
                        title
                        _id
                        criteria {
                            _id
                            description
                            longDescription
                            points
                            ratings {
                                _id
                                longDescription
                                description
                                points
                            }
                        }
                    }
                    submissionsConnection {
                        nodes {
                            _id
                            score
                            state
                            submissionStatus
                            submittedAt
                            attempt
                            grade
                            user {
                                name
                                _id
                                sisId
                            }
                            commentsConnection {
                                nodes {
                                    comment
                                    author {
                                        name
                                        _id
                                    }
                                }
                            }
                            rubricAssessmentsConnection {
                                nodes {
                                    _id
                                    assessor {
                                        _id
                                        name
                                    }
                                    assessmentRatings {
                                        _id
                                        comments
                                        commentsHtml
                                        description
                                        points
                                        criterion {
                                            _id
                                            description
                                            longDescription
                                            points
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    """

    try:
        all_json = _get_query_by_course(url, query, course_id, KEY)
        return(all_json)
        
    except Exception as err:
        print(f"Error: {err}")

