# Write an expression to get the k-th element of the series
get_elmnt = lambda k: ((-1)**k)/(2*k+1)

# Write an expression to get the k-th element of the series
get_elmnt = lambda k: ((-1)**k)/(2*k+1)

def calc_pi(n):
    curr_elmnt = get_elmnt(n)

    # Define the base case
    if n == 0:
    	return 4

    # Make the recursive call
    return 4 * curr_elmnt + calc_pi(n-1)

# Compare the approximated Pi value to the theoretical one
print("approx = {}, theor = {}".format(calc_pi(500), math.pi))
