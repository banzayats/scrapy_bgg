# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class ThingItem(Item):
    id = Field()
    type = Field()
    primary_name = Field()
    image = Field()
    yearpublished = Field()
    minplayers = Field()
    maxplayers = Field()
    playingtime = Field()
    minplaytime = Field()
    maxplaytime = Field()
    minage = Field()
    rating_usersrated = Field()
    rating_average = Field()
    boardgame_rank_value = Field()
    boardgame_rank_average = Field()
    thematic_rank_value = Field()
    thematic_rank_average = Field()
    owned = Field()
    trading = Field()
    wanting = Field()
    wishing = Field()
    numcomments = Field()

    # Housekeeping fields
    date = Field()
