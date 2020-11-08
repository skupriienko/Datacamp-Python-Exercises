# Loop over the DataFrame and print each row
for row in rangers_df.itertuples():
    print(row)
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
    i = row[0]
    year = row[3]
    wins = row[6]
    print(i, year, wins)
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W

  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if rangers_df.index[8] == 1:
    print(i, year, wins)
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    run_diffs.append(run_diff)

# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)
