
# %%
import pandas as pd
# %%
df = pd.read_csv("DigiDB_digimonlist.csv")
# %%
df
# %%
print(df)

#5. What is your terminal display "path"? (type/paste as text into the .py file) 
# (venv) @timlee717 ➜ ~ $

# 4. Should you include the environment in your repo or not?  
# No, you should not include the enviornment in your repo because that is what the  requirements.txt is supposed to do

# 5. Now what is your terminal display "path"? Is it different? 
# it is (venv) @timlee717 ➜ ~ $ now it used to be: @timlee717 ➜ /workspaces/daytwostuff (main) $

# 2. Find the extension in the extension menu. What do you notice about the extension menu? 
# There are two different subsections. One for locally installed extentsions and one for extensiions installed through codespaces (Data Wrangler and Jupyter)

# 3. Review the capabilities, what are three useful elements of Data Wrangler
# It breaks down the percentage of each value in a column. It also gives us min and max values for numeric columns. And it gives us a count for the # of distinct values.

# 5. Why do we use a requirements.txt file?
# Requirements.txt file allows anyone to recreate the same Python environment by installing the same package versions in different places and times.


# 1. Write yourself a step by step recipe for creating a new working project environment
# You don't need to include "loading data"
# 1. Clone the Repo
# 2. Open the Codespace in your local VS Code
# 3. Create a virtual environment
# 4. Load/(create if needed) the requirements.txt file


# 1. create a new project folder and navigate into it using the terminal
# 2. initialize a new Git repository to track project changes
# 3. create a Python virtual environment using python3 -m venv .venv
# 4. activate the virtual environment to isolate project dependencies
# 5. install required Python packages using pip install -r requirements.txt
# 6. verify the environment is active and dependencies are installed correctly
# 7. add a .gitignore file and ensure the virtual environment folder is excluded from version control
# 8. commit the initial project setup to Git