# Load pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel('E://src//fcc-new-coder-survey.xlsx')

# View the head of the data frame
print(survey_responses.head())

# Create string of lettered columns to load
col_string = 'AD, AW:BA'

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("E://src//fcc-new-coder-survey.xlsx",
                        skiprows=2,
                        usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("E://src//fcc-new-coder-survey.xlsx",
                               sheet_name='2017')

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()
