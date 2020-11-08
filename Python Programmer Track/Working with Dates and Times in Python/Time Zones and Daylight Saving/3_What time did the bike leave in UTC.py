# Loop over the trips
for trip in onebike_datetimes[:10]:
    # Pull out the start and set it to UTC
    dt = trip['start'].astimezone(timezone.utc)

    # Print the start time in UTC
    print('Original:', trip['start'], '| UTC:', dt.isoformat())
