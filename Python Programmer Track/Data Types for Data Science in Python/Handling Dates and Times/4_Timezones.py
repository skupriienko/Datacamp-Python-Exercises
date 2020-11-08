from pytz import timezone
from datetime import datetime

# Create a Timezone object for Chicago
chicago_usa_tz = timezone('US/Central')

# Create a Timezone object for New York
ny_usa_tz = timezone('US/Eastern')

daily_summaries = [(datetime.datetime(2001, 1, 1, 15, 35), '126455'),
 (datetime.datetime(2001, 1, 2, 22, 52), '501952'),
 (datetime.datetime(2001, 1, 3, 10, 42), '536432'),
 (datetime.datetime(2001, 1, 4, 12, 38), '550011'),
 (datetime.datetime(2001, 1, 5, 21, 39), '557917'),
 (datetime.datetime(2001, 1, 6, 7, 14), '255356'),
 (datetime.datetime(2001, 1, 7, 14, 10), '169825'),
 (datetime.datetime(2001, 1, 8, 16, 48), '590706'),
 (datetime.datetime(2001, 1, 9, 0, 32), '599905')]
# Iterate over the daily_summaries list
for orig_dt, ridership in daily_summaries:

    # Make the orig_dt timezone "aware" for Chicago
    chicago_dt = orig_dt.replace(tzinfo=chicago_usa_tz)

    # Convert chicago_dt to the New York Timezone
    ny_dt = chicago_dt.astimezone(ny_usa_tz)

    # Print the chicago_dt, ny_dt, and ridership
    print('Chicago: %s, NY: %s, Ridership: %s' % (chicago_dt, ny_dt, ridership))
