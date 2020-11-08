indices = """
title
The Dark Knight Rises                         0
Batman Forever                                1
Batman                                        2
Batman Returns                                3
Batman & Robin                                4
Batman: Mask of the Phantasm                  5
Batman                                        6
Batman Begins                                 7
Batman: Under the Red Hood                    8
Batman: Year One                              9
Batman: The Dark Knight Returns, Part 1      10
Batman: The Dark Knight Returns, Part 2      11
Batman v Superman: Dawn of Justice           12
Toy Story                                    13
Jumanji                                      14
Grumpier Old Men                             15
Waiting to Exhale                            16
Father of the Bride Part II                  17
Heat                                         18
Sabrina                                      19
Tom and Huck                                 20
Sudden Death                                 21
GoldenEye                                    22
The American President                       23
Dracula: Dead and Loving It                  24
Balto                                        25
Nixon                                        26
Cutthroat Island                             27
Casino                                       28
Sense and Sensibility                        29
"""

movie_plots = """
0       Following the death of District Attorney Harve...
1       The Dark Knight of Gotham City confronts a das...
2       The Dark Knight of Gotham City begins his war ...
3       Having defeated the Joker, Batman now faces th...
4       Along with crime-fighting partner Robin and ne...
5       An old flame of Bruce Wayne's strolls into tow...
6       The Dynamic Duo faces four super-villains who ...
7       Driven by tragedy, billionaire Bruce Wayne ded...
8       Batman faces his ultimate challenge as the mys...
9       Two men come to Gotham City: Bruce Wayne after...
10      Batman has not been seen for ten years. A new ...
11      Batman has stopped the reign of terror that Th...
12      Fearing the actions of a god-like Super Hero l...
"""

# Initialize the TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Construct the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(movie_plots)

# Generate the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Generate recommendations
print(get_recommendations('The Dark Knight Rises', cosine_sim, indices))