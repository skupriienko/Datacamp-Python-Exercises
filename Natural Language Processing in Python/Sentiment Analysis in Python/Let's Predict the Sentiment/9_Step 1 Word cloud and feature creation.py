# Create and generate a word cloud image
cloud_positives = WordCloud(background_color='white').generate(positive_reviews)

# Display the generated wordcloud image
plt.imshow(cloud_positives, interpolation='bilinear')
plt.axis("off")

# Don't forget to show the final image
plt.show()

# Tokenize each item in the review column
word_tokens = [word_tokenize(review) for review in reviews.review]

# Create an empty list to store the length of the reviews
len_tokens = []

# Iterate over the word_tokens list and determine the length of each item
for i in range(len(word_tokens)):
     len_tokens.append(len(word_tokens[i]))

# Create a new feature for the lengh of each review
reviews['n_words'] = len_tokens 