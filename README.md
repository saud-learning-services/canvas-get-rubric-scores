# Canvas Get Rubric Scores
⛔️ IN DEVELOPMENT - USE AT YOUR OWN RISK ⛔️

> - name: canvas-get-rubric-scores
> - runs-with: terminal in a Jupyter notebook
> - python>=3.8
> - canvasapi>=2.0.0

## Summary

Project to extract rubric assessment details from a selected Canvas course. 
Note - this should work for peer reviews with rubrics as well! 

## Input

You will need to give this tool an active Canvas API token for it to work. To do so, you need to create a .env file with the following

```
API_TOKEN = 'yourTokenHere'
API_INSTANCE = 'yourInstanceHere'
```

a. Set your token to the `API_TOKEN` field in the `.env` file (replace "yourTokenHere")

> `API_TOKEN=yourTokenHere`
> becomes
> `API_TOKEN=fdfjskSDFj3343jkasdaA...`

b. set your API_INSTANCE 
> `API_INSTANCE = 'https://canvas.ubc.ca'`

## Output

> TBD

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
