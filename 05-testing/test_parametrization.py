import pytest
from times import overlap_time, time_range

@pytest.mark.parametrize("large, short, expected", [(time_range("2010-01-12 00:00:00", "2010-01-12 23:50:00", 2, 600),
                                                     time_range("2010-01-13 00:00:00", "2010-01-13 23:50:00", 2, 600),
                                                     [])] )


def test_eval(large, short, expected):
    assert (overlap_time(large, short)) == expected