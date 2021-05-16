import datetime
import pytest
from clisya import Schedule
clisya = Schedule()



@pytest.mark.parametrize(
    ["datatime","excepted"],

    [
        ("2022-05-11 10:00:00","2022-05-11 00:00:00")
    ],
)
def test_date_to_convert_country(datatime,excepted):
    actual = clisya.date_to_convert(datatime)
    assert actual != excepted 

