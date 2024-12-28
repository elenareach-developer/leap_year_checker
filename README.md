## Leap Year Checker

> This package was created to check if a year is a leap year and to separate leap years from non-leap years in a set of years.

## Screenshot



## Install

```
$ pip install leap_year_checker
```

## Usage

```python

from leap_year_checker import is_valid_year, is_leap_year, classify_years, classify_years_counter

# Check if a year is valid it should be int and between 1 and 9999
try:
    year = 10000
    if is_valid_year(year):
        print(f"{year} is a valid year.")
except ValueError as e:
    print(e)

# Check if a year is a leap year
year = 2024
print(f"{year} is a leap year: {is_leap_year(year)}")

# Get leap and non-leap years in a range
start_year = 2000
end_year = 10000  # Will raise an error due to limit
try:
    leap_years, non_leap_years = classify_years(start_year, end_year)
    print("Leap years:", leap_years)
    print("Non-leap years:", non_leap_years)
except ValueError as e:
    print(e)

# Get the count of leap and non-leap years in the range (2000, 2004) => (2, 3) respectively

start_year = 2000
end_year = 2004  
try:
    leap_year_count, non_leap_year_count = classify_years_counter(start_year, end_year)
    print("Leap years count:", leap_year_count)
    print("Non-leap years count:", non_leap_year_count)
except ValueError as e:
    print(e)

```

## API

### is_valid_year(year)

#### year

Type: `int`

Validates if the input is and integen and the value between 1 and 9999

### is_leap_year(year)

#### year

Type: `int`

Check is a year is a leap year

### classify_years(start_year, end_year)

#### start_year, end_year

Type: `int`

Classify years in a range as leap or non-leap years for valid years and if start_year < end_year

### classify_years_counter(start_year, end_year)

#### start_year, end_year

Type: `int`

Count and classify years in a range as leap or non-leap years for valid years and if start_year < end_year

## Run tests from root derectory
python -m unittest discover

## License

[MIT][license] ElenaReach

[LICENSE]:
