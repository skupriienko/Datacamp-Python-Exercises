# A list of 480 superheroes has been loaded into your session (called heroes) as well as a list of each hero's corresponding publisher (called publishers). You'd like to filter the heroes list based on a hero's specific publisher, but are unsure which of the below functions is more efficient.
# def get_publisher_heroes(heroes, publishers, desired_publisher):

#     desired_heroes = []

#     for i,pub in enumerate(publishers):
#         if pub == desired_publisher:
#             desired_heroes.append(heroes[i])

#     return desired_heroes

# def get_publisher_heroes_np(heroes, publishers, desired_publisher):

#     heroes_np = np.array(heroes)
#     pubs_np = np.array(publishers)

#     desired_heroes = heroes_np[pubs_np == desired_publisher]

#     return desired_heroes

# Use get_publisher_heroes() to gather Star Wars heroes

# Use the get_publisher_heroes() function and the get_publisher_heroes_np() function to collect heroes from the Star Wars universe. The desired_publisher for Star Wars is 'George Lucas'.

star_wars_heroes = get_publisher_heroes(heroes, publishers, 'George Lucas')

print(star_wars_heroes)
print(type(star_wars_heroes))

# Use get_publisher_heroes_np() to gather Star Wars heroes
star_wars_heroes_np = get_publisher_heroes_np(heroes, publishers, 'George Lucas')

print(star_wars_heroes_np)
print(type(star_wars_heroes_np))
