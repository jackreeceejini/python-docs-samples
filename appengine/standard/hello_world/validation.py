months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def valid_month(month):
    monthAbbr = dict((month[:3].lower(), month) for month in months)
    return monthAbbr.get(month[:3].lower(), None)

def valid_day(day):
    day2 = day[:2]
    if day2.isdigit():
        day2Int = int(day2)
        if day2Int >= 1 and day2Int <=31:
            return day2Int
    else:
        return None

def valid_year(year):
    year = year[:4]
    if year.isdigit():
        yearInt = int(year)
        if yearInt >= 1900 and yearInt <= 2020:
            return yearInt
    return None

if __name__  == "__main__":
    print(valid_month('JaNuary'))

    print(valid_day('0'))
    print(valid_day('10,.'))

    print(valid_year('1038'))
    print(valid_year('1950'))
    