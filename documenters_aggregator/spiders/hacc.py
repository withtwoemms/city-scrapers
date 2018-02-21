# -*- coding: utf-8 -*-
import scrapy
from documenters_aggregator.spider import Spider
from pprint import pprint as pp


class HaccSpider(Spider):
    name = 'hacc'
    long_name = 'House Authority of Cook County'
    allowed_domains = ['thehacc.org']
    start_urls = ['http://thehacc.org/events/']

    def parse(self, response):
        """
        `parse` should always `yield` a dict that follows the Event Schema
        <https://city-bureau.gitbooks.io/documenters-event-aggregator/event-schema.html>.

        Change the `_parse_id`, `_parse_name`, etc methods to fit your scraping
        needs.
        """
        print('\nRESPONSE_XPATH: ', response.xpath('//section[@id="tribe-events-content"]//div[@class="content"]'))
        container = response.xpath('//section[@id="tribe-events-content"]//div[@class="content"]')
        for i, item in enumerate(container):

            start_time = self._parse_start(item)
            data = {
                '_type': 'event',
                'id': self._parse_id(item),
                'name': self._parse_name(item, i),
                'description': self._parse_description(item),
                'classification': self._parse_classification(item),
                'start_time': start_time,
                'end_time': self._parse_end(item),
                'timezone': self._parse_timezone(item),
                'status': self._parse_status(item),
                'all_day': self._parse_all_day(item),
                'location': self._parse_location(item),
                'sources': self._parse_sources(item),
            }
            pp(data)

        data['id'] = self._generate_id(data, start_time)

        yield data

        # self._parse_next(response) yields more responses to parse if necessary.
        # uncomment to find a "next" url
        # yield self._parse_next(response)

    def _parse_next(self, response):
        """
        Get next page. You must add logic to `next_url` and
        return a scrapy request.
        """
        next_url = None  # What is next URL?
        return scrapy.Request(next_url, callback=self.parse)

    def _parse_id(self, item):
        """
        Calulate ID. ID must be unique and in the following format:
        <spider-name>/<start-time-in-YYYYMMddhhmm>/<unique-identifier>/<underscored-event-name>

        Example:
        chi_buildings/201710161230/2176/daley_plaza_italian_exhibit
        """
        return ''

    def _parse_name(self, item, index):
        """
        Parse or generate event name.
        """
        text_array = item.xpath('//div[@class="info"]//a//text()').extract()
        return text_array[index]

    def _parse_description(self, item):
        """
        Parse or generate event name.
        """
        return ''

    def _parse_classification(self, item):
        """
        Parse or generate classification (e.g. public health, education, etc).
        """
        return ''

    def _parse_start(self, item):
        """
        Parse start date and time.
        """
        # print('\nRESPONSE_XPATH: ', response.xpath('//section[@id="tribe-events-content"]//p[@class="subtitle"]'))
        # print('***ITEM: ', item)
        # item.xpath('//br')
        # pp(item.xpath('./br'))
        # pp(item.xpath('./br').extract().__class__.__name__)
        # pp(item.xpath('./br/text()').extract())
        # pp(dir(item.xpath('./br')))
        # pp(dir(item.xpath('./br')))
        return ''

    def _parse_end(self, item):
        """
        Parse end date and time.
        """
        return ''

    def _parse_timezone(self, item):
        """
        Parse or generate timzone in tzinfo format.
        """
        return 'America/Chicago'

    def _parse_all_day(self, item):
        """
        Parse or generate all-day status. Defaults to False.
        """
        return False

    def _parse_location(self, item):
        """
        Parse or generate location. Latitude and longitude can be
        left blank and will be geocoded later.
        """
        return {
            'url': '',
            'name': '',
            'address': '',
            'coordinates': {
                'latitude': '',
                'longitude': '',
            },
        }

    def _parse_status(self, item):
        """
        Parse or generate status of meeting. Can be one of:
        * cancelled
        * tentative
        * confirmed
        * passed
        By default, return "tentative"
        """
        return 'tentative'

    def _parse_sources(self, item):
        """
        Parse or generate sources.
        """
        return [{
            'url': '',
            'note': '',
        }]
