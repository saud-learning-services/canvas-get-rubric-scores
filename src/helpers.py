from canvasapi import Canvas
import util
import sys

def create_instance(API_URL, API_KEY):
    try:
        canvas = Canvas(API_URL, API_KEY)
        util.print_success("Token Valid: {}".format(str(canvas.get_user("self"))))
        return(canvas)
    except Exception as e:
        util.print_error("\nInvalid Token: {}...\n{}".format(API_KEY[0:12], str(e)))
        #sys.exit(1)
        #raise

def _matches_dict_key_val(dic, key, matches_val):
    """Returns the dictionary if the provided key matches the match_val
    
    parameters:
        dic (dict)
        key (string): the key string in the dict to find
        matches_val (str|int): they str or int to try to find in the key

    returns:
        boolean
    """
    # for use in list , example:
    # [d for d in list if _matches_dict_id(d, "key", matches_val)]
    return(dic[f"{key}"] == matches_val)
    
def _return_single_dict_match(some_list, match_key, match_val):
        out = [d for d in some_list if _matches_dict_key_val(d, match_key, match_val)][0]
        return(out)



def get_rubric_assessment(submission):
    user = submission["user"]
    
    new_dict = {"user_id":  user["_id"],
           "user_name":  user["name"],
           "user_sis_id": user["sisId"],
           "user_score": submission["score"],
           "submission_attempt": submission["attempt"],
            "submission_timestamp": submission["submittedAt"],
            "submission_status": submission["submissionStatus"]}
    
    try:
        rubric_details = submission["rubricAssessmentsConnection"]["nodes"]
        
        if rubric_details == []:
            return(new_dict)

        for i in rubric_details:
            assessment_ratings = i.get("assessmentRatings")
            
            points_list = []
            descriptive_list = []
            comments_list = []
            
            
            for j in assessment_ratings:
                criteria = j["criterion"]["description"]
                
                points = {criteria: j.get("points")}
                descriptive = {criteria: j.get("description")}
                comment = {criteria: j.get("comments")}
                
                points_list.append(points)
                descriptive_list.append(descriptive)
                comments_list.append(comment)
                
                new_dict.update({criteria: j.get("points")})
                
            new_dict.update({"points": points_list,
                            "descriptions": descriptive_list,
                            "comments": comments_list})
            
            return(new_dict)
        
    except Exception as err:
        print(f"Error: {err}")



def __get_assessment_criteria_scores(assessment_rating):
    criteria = assessment_rating.get("criterion").get("description")

    ratings_dictionary = {criteria: assessment_rating.get("points")}
    
#    ratings_dictionary = {f"{criteria}_json_": {"points": assessment_rating.get("points"),
#                                    "description": assessment_rating.get("description"),
#                                     "comment": assessment_rating.get("comments")},
#                         criteria: assessment_rating.get("points")}
    
    return(ratings_dictionary)

def _get_rubric_assessment_details(rubric_assessment):
    rubric_assessment_dict = {"assessment_id": rubric_assessment.get("_id"),
                             "assessor_name": rubric_assessment.get("assessor").get("name"),
                             "assessor_id": rubric_assessment.get("assessor").get("_id")}

    ratings = rubric_assessment.get("assessmentRatings")

    for i in ratings:
        rubric_assessment_dict.update(__get_assessment_criteria_scores(i))
    
    return(rubric_assessment_dict)
    
def _get_submission_details(submission):
    user = submission.get("user")
    
    submission_dict = {"user_id":  user["_id"],
                       "user_name":  user["name"],
                       "user_sis_id": user["sisId"],
                       "user_score": submission["score"],
                       "submission_attempt": submission["attempt"],
                       "submission_timestamp": submission["submittedAt"],
                       "submission_status": submission["submissionStatus"]}   
    
    return(submission_dict)    


def get_output_data(submissions):
    my_list = []
    
    for i in submissions:
    
        rubric_assessments = i.get("rubricAssessmentsConnection").get("nodes")
    
        for j in rubric_assessments:

            new_dict = {}

            new_dict.update(_get_submission_details(i))
            new_dict.update(_get_rubric_assessment_details(j))

            my_list.append(new_dict)
        
    return(my_list)
    