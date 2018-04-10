import pytest

from tests.utils import file_response
from documenters_aggregator.spiders.hacc import HaccSpider
from pprint import pprint as pp


"""
Uncomment below
"""

test_response = file_response('files/hacc.html')
spider = HaccSpider()
parsed_items = [item for item in spider.parse(test_response) if isinstance(item, dict)]


def test_name():
    assert parsed_items[0]['name'] == 'Build Your Future!'


def test_description():
   assert parsed_items[0]['description'].startswith('A hands-on opportunity to learn about the trades') == True


def test_start_time():
    assert parsed_items[0]['start_time'].strftime('%-I:%M %p').lower() == '4:00 pm'


def test_end_time():
    assert parsed_items[0]['end_time'].strftime('%-I:%M %p').lower() == '6:00 pm'


# def test_id():
    # assert parsed_items[0]['id'] == 'EXPECTED ID'


# def test_location():
    # assert parsed_items[0]['location'] == {
        # 'url': 'EXPECTED URL',
        # 'name': 'EXPECTED NAME',
        # 'address': 'EXPECTED ADDRESS'
        # 'coordinates': {
            # 'latitude': 'EXPECTED LATITUDE',
            # 'longitude': 'EXPECTED LONGITUDE',
        # },
    # }


# def test_sources():
    # assert parsed_items[0]['sources'] == {
        # 'url': 'EXPECTED URL',
        # 'note': 'EXPECTED NOTE'
    # }


# @pytest.mark.parametrize('item', parsed_items)
# def test_timezone(item):
    # assert item['timezone'] == 'EXPECTED TIMEZONE'


# @pytest.mark.parametrize('item', parsed_items)
# def test_all_day(item):
    # assert item['all_day'] is False


# @pytest.mark.parametrize('item', parsed_items)
# def test_classification(item):
    # assert item['classification'] is None


# @pytest.mark.parametrize('item', parsed_items)
# def test__type(item):
    # assert parsed_items[0]['_type'] == 'event'
