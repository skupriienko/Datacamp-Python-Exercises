import numpy as np

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Create a list of arrival times
arrival_times = [*range(10, 60, 10)]

print(arrival_times)

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[name],time) for name,time in enumerate(new_times)]

print(guest_arrivals)

# def welcome_guest(self, guest, time):
#     pass

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')
