# Lehman Brothers before Morgan Stanley?
lehman_first = lehman < morgan_stanley

print(f"It is {lehman_first} that Lehman Brothers declared bankruptcy first.")

# Goldman Sachs after TARP?
tarp_first = goldman_sachs > tarp

print(f"It is {tarp_first} that TARP was approved first.")

# Goldman Sachs and Morgan Stanley same day?
same_time = goldman_sachs == morgan_stanley

print(f"It is {same_time} that Morgan Stanley and Goldman Sachs acted simultaneously")
