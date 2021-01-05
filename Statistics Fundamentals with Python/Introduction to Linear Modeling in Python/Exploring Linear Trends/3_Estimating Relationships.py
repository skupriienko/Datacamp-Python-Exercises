# Complete the function to model the efficiency.
def efficiency_model(miles, gallons):
   return np.mean( miles / gallons )

# Use the function to estimate the efficiency for each car.
car1['mpg'] = efficiency_model(car1['miles'] , car1['gallons'] )
car2['mpg'] = efficiency_model(car2['miles'] , car2['gallons'] )

# Finish the logic statement to compare the car efficiencies.
if car1['mpg'] < car2['mpg'] :
    print('car1 is the best')
elif car1['mpg'] > car2['mpg'] :
    print('car2 is the best')
else:
    print('the cars have the same efficiency')