from textanalysis.textanalysis import count_words

# Count the number of positive words
nb_positive_words = count_words('hotel-reviews.txt', ["good", "great"])

# Count the number of negative words
nb_negative_words = count_words('hotel-reviews.txt', ["bad", "awful"])

print("{} positive words.".format(nb_positive_words))
print("{} negative words.".format(nb_negative_words))
INCHES_PER_FOOT = 12.0  # 12 inches in a foot
INCHES_PER_YARD = INCHES_PER_FOOT * 3.0  # 3 feet in a yard

UNITS = ("in", "ft", "yd")


def inches_to_feet(x, reverse=False):
    """

    Parameters
    ----------
    x :
        
    reverse :
         (Default value = False)

    Returns
    -------

    """
    if reverse:
        return x * INCHES_PER_FOOT
    else:
        return x / INCHES_PER_FOOT
