from times import time_range,overlap_time
import datetime
import times

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

def test_20_min():
    large = times.time_range("2019-01-01 00:00:00", "2019-01-01 23:50:00", 24, 10 * 60)
    short = times.time_range("2019-01-01 00:30:00", "2019-01-01 23:55:00", 24, 35 * 60)
    result = times.overlap_time(large, short)
    assert all([(datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S") -
    datetime.datetime.strptime(t0, "%Y-%m-%d %H:%M:%S")).total_seconds() == 20 * 60
    for t0, t1 in result])
     # add methods