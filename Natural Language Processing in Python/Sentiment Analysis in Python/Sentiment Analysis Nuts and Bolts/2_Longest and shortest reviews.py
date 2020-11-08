length_reviews = movies.review.str.len()

# How long is the longest review
print(max(length_reviews))

length_reviews = movies.review.str.len()

# How long is the shortest review
print(min(length_reviews))