# Loop while true
while True:
    net_exports = nea.get(query_date, -1)
    query_date = datetime(query_date.year - 1, 1, 1)
    # Skip if net exports are not positive
    if net_exports < 0:
        continue
    surplus_years.append(query_date)
    # Check if 5 years have been collected
    if len(surplus_years) == 5:
        # Stop the loop
        break
print(surplus_years)
