# Canvas Get Rubric Scores
⛔️ IN DEVELOPMENT - USE AT YOUR OWN RISK ⛔️

> - name: canvas-get-rubric-scores
> - runs-with: terminal in a Jupyter notebook
> - python>=3.8
> - canvasapi>=2.0.0

## Summary

Project to extract rubric assessment details from a selected Canvas course into a .csv file. 
Note - this should work for peer reviews with rubrics as well! 

## Input

- Canvas Instance _(instance of Canvas being used - ex. https://ubc.instructure.com)_
- Canvas API Token _(generate through Account => Settings)_
- Course ID _(last digits of URL when visiting course page)_
  
You will need to give this tool an active Canvas API token for it to work. To do so, you need to create a .env file with the following

```
API_TOKEN = 'yourTokenHere'
API_INSTANCE = 'yourInstanceHere'
```

Your .env file should be in this project folder:

<img width="540" alt="image" src="https://user-images.githubusercontent.com/22600917/172930834-c160322e-b583-4a08-a06c-1074360f17f8.png">

a. Set your token to the `API_TOKEN` field in the `.env` file (replace "yourTokenHere")

> `API_TOKEN=yourTokenHere`
> becomes
> `API_TOKEN=fdfjskSDFj3343jkasdaA...`

b. set your API_INSTANCE to your Canvas Instance
> `API_INSTANCE = 'https://canvas.ubc.ca'`

The Jupyter Notebook tell you if the information in the .env file is correct.

It will then ask you to input the Course ID.

## Output

### CourseName_AssignmentName_Date_rubric_scores.csv:

_Lists of all rubrics used in scoring, including the following columns:_

- **course_id:** id of the course
- **course_name:** name of the course
- **assignment_name:** name of the assignment
- **user_id:** id of the student being evaluated
- **user_name:** name of the student being evaluated
- **user_score:** assessment score
- **submission_attempt:** how many attempts were taken to submit the assugnment
- **submission_timestamp:** when the final submission was made
- **submission_status:** sumbitted, late, unsubmitted, excused...
- **assessment_id:** unique id of the rubric assessment
- **assessor_name:** name of the assessor
- **assessor_id:** id of the assessor
- several columns of **criterion #** which indicate the score for that criterion

## Getting Started

### First Time (do once)

1. Clone this repo: `$ git clone saud-learning-services/canvas-get-rubric-scores`
   > - this will create the canvas-get-rubric-scores directory in whichever folder you are set to in terminal (check with `$ pwd` to see current working directory)
   > - see [terminal basics](https://github.com/saud-learning-services/instructions-and-other-templates/blob/main/docs/terminal-basics.md) to change directories
2. Import environment (once): `$ conda env create -f environment.yml`

### Every Time

1. Make sure you are in the right directory: `$ pwd` if it isn't `..../canvas-get-rubric-scores` then you need to navigate to it: `$ cd {YOUR_PATH}/canvas-get-rubric-scores`
2. Make sure you have your token (in .env - see [above](#input)
3. Activate the environment: `$ conda activate canvas-get-rubric-scores`
4. Launch jupyter: `$ jupyter notebook` and open dash-app.ipynb
5. Follow instructions
6. You're basically a wizard now [🧙‍♀️](https://tenor.com/bo4Bs.gif)
