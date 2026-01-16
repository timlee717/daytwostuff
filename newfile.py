
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