import numpy as np

# Calculate the EAA for Project 1
eaa_project1 = np.pmt(rate=wacc, nper=8, pv=-1*npv_project1, fv=0)
print("Project 1 EAA: " + str(round(eaa_project1, 2)))

# Calculate the EAA for Project 2
eaa_project2 = np.pmt(rate=wacc, nper=7, pv=-1*npv_project2, fv=0)
print("Project 2 EAA: " + str(round(eaa_project2, 2)))
