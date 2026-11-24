# Explore US Bikeshare Data

A command-line Python program that answers questions about bike share trips in Chicago, New York City and Washington, DC, using pandas. Data covers January to June 2017.

## What it reports

For the city, month and weekday you pick (or "all"):

- most common month, day of the week and start hour
- most common start station, end station and start-to-end trip
- total and average trip duration
- user types, and for Chicago and New York City also gender counts and birth year statistics (Washington has no gender or birth year columns)
- raw rows, five at a time, if you ask for them

## Run it

```
pip install pandas numpy
python bikeshare.py
```

Keep `chicago.csv`, `new_york_city.csv` and `washington.csv` in the same folder.

## Example (Chicago, March, all days)

- most common day: Friday, most common start hour: 17
- user types: 27,254 Subscribers and 2,385 Customers
- mean trip duration: about 708 seconds (11.8 minutes)

## Notes

- Birth years in the data include implausible values (for example 1899), so "earliest birth year" reflects data entry errors, not riders.
- Updated to run on current pandas (`dt.day_name()` replaces `weekday_name`, which pandas removed).
