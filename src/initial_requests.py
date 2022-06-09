import requests
import json
import os

# uses GRAPH QL

def _get_query_by_course(url, query, course_id, KEY):
    
    r = requests.post(url, json={"query": query, "variables": {"id": f"{course_id}"}}, headers={"Authorization": f"Bearer {KEY}"})
    if r.status_code == 200:
        return(r.json())
    else:
        print(f"Error: {r.json()}")

def get_initial_info(url, course_id, KEY):

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
        #assignments = all_json["data"]["course"]["assignmentsConnection"]["nodes"]
        #group_sets = all_json["data"]["course"]["groupSetsConnection"]["nodes"]
        #course = { your_key: all_json["data"]["course"][your_key] for your_key in ["_id", "id", "courseCode", "name"] }
        #users = all_json["data"]["course"]["usersConnection"]["nodes"]
        return(all_json)
        
    except Exception as err:
        print(f"Error: {err}")