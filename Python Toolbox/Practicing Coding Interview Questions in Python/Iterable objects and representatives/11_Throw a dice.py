import random

def simulate_dice_throws():
    total, out = 0, dict([(i, [0, 0]) for i in range(1, 7)])
    while True:
        # Simulate a single toss to get a new number
        num = random.randint(1, 6)
        total += 1
        # Update the number and the ratio of realizations
        out[num][0] = out[num][0] + 1
        for j in range(1, 7):
        	out[j][1] = round(out[j][0]/total, 2)
        # Yield the updated dictionary
        yield out

# Create the generator and simulate 1000 tosses
dice_simulator = simulate_dice_throws()
for i in range(1, 1001):
    print(str(i) + ': ' + str(next(dice_simulator)))
