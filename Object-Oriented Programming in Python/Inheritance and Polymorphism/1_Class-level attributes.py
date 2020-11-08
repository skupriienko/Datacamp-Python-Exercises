# Create a Player class
class Player:
    MAX_POSITION = 10

    def __init__(self, position=0):
        self.position = 0


# Print Player.MAX_POSITION
print(Player.MAX_POSITION)

# Create a player p and print its MAX_POSITITON
p = Player()
print(p.MAX_POSITION)
