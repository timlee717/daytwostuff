---
title: Day Two Stuff
---

## Today we are going to work through getting all our environments setup and do some quick tasks. 
## You will record your answers in the .py file, which will need to be pushed to your repo. You'll submit
## the repo link. 

### Clone the Repo
1. Go to Github and find the DayTwoStuff repo
2. Clone it to your GitHub Account
3. Create a new Codespace from the repo

### Open the Codespace in your local VS Code
1. Open VS Code on your local machine
2. Use the Codespaces extension to open your new Codespace in VS Code
3. Familiarize yourself with the layout of the project
4. Open a new .py file and add the section breaks to create a interactive .py file
    hint: you made need to reload juypter extension and/or add the ipykernel package
5. What is your terminal display "path"? (type/paste as text into the .py file) 

(venv) @timlee717 ➜ ~ $

### Create a virtual environment
1. open a bash terminal 
2. type the command for creating a virtual environment
3. make sure the environment is activated
4. Should you include the environment in your repo or not?  

No, you should not include the enviornment in your repo because that is what the  requirements.txt is supposed to do

5. Now what is your terminal display "path"? Is it different? 

 it is (venv) @timlee717 ➜ ~ $ now it used to be: @timlee717 ➜ /workspaces/daytwostuff (main) $

### Load/(create if needed) the requirements.txt file
1. use the correct terminal commands to load the requirements file into your virtual environment

### Viewing Data
1. In your current .py file load in a dataset.
2. Find a extension that will allow you to see the data in a data viewer (Data Wrangler)
3. Load the extension and view the data

### Extension Management
1. You've possibilly added a new extension, hopefully it was Data Wrangler, if not search and add it
2. Find the extension in the extension menu. What do you notice about the extension menu? 

There are two different subsections. One for locally installed extentsions and one for extensiions installed through codespaces (Data Wrangler and Jupyter)

3. Review the capabilities, what are three useful elements of Data Wrangler

It breaks down the percentage of each value in a column. It also gives us min and max values for numeric columns. And it gives us a count for the # of distinct values.


### Package managing
1. Install plotly in the terminal
2. Note the version
3. Add plotly to your requirements file using terminal commands
4. Then update the requirements document
5. Why do we use a requirements.txt file?

Requirements.txt file allows anyone to recreate the same Python environment by installing the same package versions in different places and times.

### Pip Freeze/(create if needed) the requirements.txt file
1. use the correct terminal commands to update your requirements.txt file

### Github 
1. You've made several changes to your environment, including adding a python file, dataset and updates to the requirements file
2. Commit and push these changes to your repo

### Recipe
1. Write yourself a step by step recipe for creating a new working project environment
    You don't need to include "loading data"
2. Create a new working project environment using these steps. 

### Submit to canvas
1. Submit your github links (this repo and your new project) to canvas
2. Include your answers to the questions above in the python script, in the first repo.

## If you finish early - take a look at "Sample script.py" The end result should be a map in the browser 
## showing the location of 2000 squirrels in central part. Try to draw, by hand, a flow diagram that includes 
## all the software necessary to make this simple script work. 