import numpy as np

# Set your weighted average cost of capital equal to 12.9%
wacc = 0.129

# Calculate the net present value for Project 1
npv_project1 = np.npv(wacc, cf_project1)
print("Project 1 NPV: " + str(round(npv_project1, 2)))

# Calculate the net present value for Project 2
npv_project2 = np.npv(wacc, cf_project2)
print("Project 2 NPV: " + str(round(npv_project2, 2)))
