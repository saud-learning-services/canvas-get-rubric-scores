# Canvas Get Rubric

> - name: canvas-get-rubric
> - runs-with: terminal
> - python>=3.8
> - canvasapi>=2.0.0
> - supports universal environment 🌎

## Summary

Project to extract rubric and details from Canvas course. Developed initially for Sauder AOL

## Input

You will need to give this tool an active Canvas API token for it to work. There are two methods of doing this (we recommend getting familiar with both):

a. Set your token to the `CANVAS_API_TOKEN` field in the `.env` file (replace "your-token-here")

> `CANVAS_API_TOKEN=your-token-here`
> becomes
> `CANVAS_API_TOKEN=fdfjskSDFj3343jkasdaA...`

or

b. Delete the `.env` file and the Jupyter Notebook will prompt you to paste in your token as input (this is the more common way to input tokens for Ops tools)

## Output

- if everything is setup correctly you should see an output like the following

<div>
    <img src="images/test-output.png" alt="Logo" width="350">
</div>

(instead displaying _your_ first name as it appears on Canvas)

## Getting Started - General Ops Method

1. Make sure you have [your environment created](https://github.com/saud-learning-services/instructions-and-other-templates/blob/main/docs/environment-setup.md) (either universal or project environment)
2. Follow steps to [run Jupyter notebook](https://github.com/saud-learning-services/instructions-and-other-templates/blob/main/docs/running-instructions.md)
3. Follow the instructions in the Jupyter notebook

**That's it! See below for some more advanced steps if you want to test out your terminal knowledge.**

---

## Want to Try in Terminal?

> Many of our projects will have instructions similar to the following that are for those who want to run the projects without any GUI. Give it a try if you're keen!

### First Time (do once)

1. Clone this repo: `$ git clone saud-learning-services/setup-test`
   > - this will create the setup-test directory in whichever folder you are set to in terminal (check with `$ pwd` to see current working directory)
   > - see [terminal basics](https://github.com/saud-learning-services/instructions-and-other-templates/blob/main/docs/terminal-basics.md) to change directories
2. Import environment (once): `$ conda env create -f environment.yml`

### Every Time

1. Make sure you are in the right directory: `$ pwd` if it isn't `..../setup-test` then you need to navigate to it: `$ cd {YOUR_PATH}/setup-test`
2. Make sure you have your token (either handy or in .env - see [above](#input))
3. Activate the environment: `$ conda activate setup-test`
4. Launch jupyter: `$ jupyter notebook`
5. Follow instructions
6. You're basically a wizard now [🧙‍♀️](https://tenor.com/bo4Bs.gif)
