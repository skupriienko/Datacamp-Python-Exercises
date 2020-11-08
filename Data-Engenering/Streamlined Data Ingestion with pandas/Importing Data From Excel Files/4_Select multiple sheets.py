# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=None)

# View the data type of all_survey_data
print(type(all_survey_data))
