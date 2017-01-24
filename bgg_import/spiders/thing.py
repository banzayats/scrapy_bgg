# -*- coding: utf-8 -*-
import scrapy
from bgg_import.items import ThingItem


class ThingSpider(scrapy.Spider):
    name = "thing"
    
    start_urls = ['https://www.boardgamegeek.com/xmlapi2/thing?id=%s&stats=1' % id for id in xrange(1,50000)]

    def parse(self, response):

        def extract_with_xpath(query):
            return response.xpath(query).extract_first()

        yield {
            'id': extract_with_xpath('//items/item/@id'),
            'type': extract_with_xpath('//items/item/@type'),
            'primary_name': extract_with_xpath('//items/item/name[@type="primary"]/@value'),
	    'image': extract_with_xpath('//items/item/image/text()'),
	    'yearpublished': extract_with_xpath('//items/item/yearpublished/@value'),
            'minplayers': extract_with_xpath('//items/item/minplayers/@value'),
	    'maxplayers': extract_with_xpath('//items/item/maxplayers/@value'),
	    'playingtime': extract_with_xpath('//items/item/playingtime/@value'),
	    'minplaytime': extract_with_xpath('//items/item//@value'),
	    'maxplaytime': extract_with_xpath('//items/item/minplaytime/@value'),
	    'minage': extract_with_xpath('//items/item/minage/@value'),
	    'rating_usersrated': extract_with_xpath('//items/item/statistics/ratings/usersrated/@value'),
	    'rating_average': extract_with_xpath('//items/item/statistics/ratings/average/@value'),
	    'boardgame_rank_value': extract_with_xpath('//items/item/statistics/ratings/ranks/rank[@name="boardgame"]/@value'),
	    'boardgame_rank_average': extract_with_xpath('//items/item/statistics/ratings/ranks/rank[@name="boardgame"]/@bayesaverage'),
	    'thematic_rank_value': extract_with_xpath('//items/item/statistics/ratings/ranks/rank[@name="thematic"]/@value'),
	    'thematic_rank_average': extract_with_xpath('//items/item/statistics/ratings/ranks/rank[@name="thematic"]/@bayesaverage'),
	    'owned': extract_with_xpath('//items/item/statistics/ratings/owned/@value'),
	    'trading': extract_with_xpath('//items/item/statistics/ratings/trading/@value'),
	    'wanting': extract_with_xpath('//items/item/statistics/ratings/wanting/@value'),
	    'wishing': extract_with_xpath('//items/item/statistics/ratings/wishing/@value'),
	    'numcomments': extract_with_xpath('//items/item/statistics/ratings/numcomments/@value')
        }

