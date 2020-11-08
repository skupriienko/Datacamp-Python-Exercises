# Custom functions to clean data
# You'll now practice writing functions to clean data.

# The tips dataset has been pre-loaded into a DataFrame called tips. 
# It has a 'sex' column that contains the values 'Male' or 'Female'. 
# Your job is to write a function that will recode 'Female' to 0, 
# 'Male' to 1, and return np.nan for all entries of 'sex' 
# that are neither 'Female' nor 'Male'.

# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    
    # Return 1 if gender is 'Male'    
    elif gender == 'Male':
        return 1
    
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['recode'] = tips.sex.apply(recode_gender)

# Print the first five rows of tips
print(tips.head())
