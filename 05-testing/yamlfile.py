import datetime

import pytest
import yaml
import times

with open("fixture.yaml", 'r') as yamlfile:
    fixture = yaml.safe_load(yamlfile)


@pytest.mark.parametrize('test_name', fixture)  # fixture is a list of dictionaries [{'given':...}, {'class':...}, ]
def test_many(test_name):
    # test_name is a dictionary like: {'name': {'test_input':..., 'expected':...}
    properties = list(test_name.values())[0]  # We know there's only one element inside 'name'
    # get the input and expected values for each test
    test_input = properties['test_input']
    expected = properties['expected']
    large = times.time_range(*test_input['interval_1'])
    short = times.time_range(*test_input['interval_2'])
    result = times.overlap_time(large, short)



    if isinstance(expected, list):
    # If expected is a list when we've writen the results on the yaml
     if expected:
    # If it's not an empty list we need to convert a list of lists into a list of tuples.
        expected = [(start, stop) for start, stop in expected]
        assert result == expected
    else:
           # If it's not a list, then `expected` is the name of one of the inputs
         assert result == times.time_range(*test_input[expected])

def test_20_min():
    large = times.time_range("2019-01-01 00:00:00", "2019-01-01 23:50:00", 24, 10 * 60)