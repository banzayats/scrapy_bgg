# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem

TYPES = ['boardgame', 'boardgameexpansion']

class FilterPipeline(object):
    def process_item(self, item, spider):
        if item['type'] in TYPES:
            return item
        else:
            raise DropItem("Unsuitable thing type")
