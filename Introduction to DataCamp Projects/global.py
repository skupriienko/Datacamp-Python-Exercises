def square(value):
    """Returns the square of a number."""
    new_val = value ** 2
    return new_val


print(square(3))


# # Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""
    global team
    # Use team in global scope
    team = "justice league"
    return team

    # Change the value of team in global: team

# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)
