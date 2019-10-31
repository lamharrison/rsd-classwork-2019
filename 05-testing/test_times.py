from times import time_range,overlap_time

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_class_time():
    large = time_range("2010-10-31 10:00:00", "2010-10-31 13:00:00")
    short = time_range("2010-10-31 10:05:00", "2010-10-31 12:55:00", 3, 600)
    result = overlap_time(large, short)
    expected = short  #test it without running it add
    assert result == expected

#what happens if large times is smaller than short times?
#what happens if the date is not exist, for example 29/02/leap year
#what happens with different dates, examples dates are same dates
#what happens if time range is in opposite order
#how to express for BC years?
