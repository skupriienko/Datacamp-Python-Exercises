api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url,
                headers=headers,
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a data frame
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)

# Bravo! Check the response format whenever you work with a new API -- chances are the data you need is nested under a dictionary key, like here.
# One important note: to avoid problems like hitting usage limits or potential connection issues, this course mimics API requests in the background, and, if you set up the code right, returns the corresponding response object. The code you'll write looks exactly like what you would use to interact with the actual API, though. If you're curious about how this works, check out this GitHub repo (https://github.com/adrian-datacamp/mock-request).
