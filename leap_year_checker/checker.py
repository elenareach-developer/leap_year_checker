def is_valid_year(year):
    """
        Validates if the input is and integen and the value between 1 and 9999
        Args:
            year : int: The input to check
        
        Returns:
            bool: True if the input is a valid year, False otherwise
        Raises:
            ValueError: If the input not a valid year
    """
    if not isinstance(year, int):
        raise ValueError(f"Year must be integer. Received: {type(year)}")
    if year <1 or year > 9999:
        raise ValueError(f"Year must be between 1 and 9999. Receied: {year}")
    return True


def is_leap_year(year):
    """
        Check is a year is a leap year
        Args:
            year(int): The year to check
        Returns:
            bool: True if the year is a leap year
        Raises:
            ValueError: If the input not a valid year
    """
    is_valid_year(year) 
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)


def classify_years(start_year, end_year):
    """
        Classify years in a range as leap or non-leap years
        Args:
            start_years(int): The start of the range
            end_years(int): The end of the range
        Returns:
            tuple A tuple containing two sets of leap or non-leap years
        Raises:
            ValueError: If start_year is grader then end_year or if the years are invalid
    """
    is_valid_year(start_year)
    is_valid_year(end_year)
    if start_year > end_year:
        raise ValueError(f"Start year {start_year} cannot be greater then {end_year}")
    
    leap_years = set()
    non_leap_years = set()
   
    for year in range(start_year,end_year+1):
        is_leap = is_leap_year(year)
        if is_leap:
            leap_years.add(year)
        else:
            non_leap_years.add(year)
    return  leap_years, non_leap_years


def classify_years_counter(start_year, end_year):
    """
    Count and classify years in a range as leap or non-leap years.
    
    Args:
        start_year (int): The start of the range.
        end_year (int): The end of the range.
        
    Returns:
        tuple: A tuple containing the count of leap years and non-leap years.
        
    Raises:
        ValueError: If start_year is greater than end_year or if the years are invalid.
    """
    try:
        leap_years, non_leap_years = classify_years(start_year, end_year)
        return len(leap_years), len(non_leap_years)
    except ValueError as e:
        raise ValueError(f"An error occurred: {e}")


if __name__=="__main__":
    print(classify_years(2000,2004))
    print(classify_years_counter(2000,2004))