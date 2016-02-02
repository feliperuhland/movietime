# -*- coding: utf-8 -*-

import scrapy

from movietime.util import format_movie_name


def get_table_from_type(table, movie_type):
    def _split_time(text):
        return text.extract().split(' ')[0]

    return [
        {'type': movie_type, 'time': _split_time(movie_time)}
        for movie_time in table
        if _split_time(movie_time) != u'INDISPONÍVEL'
    ]


class BeiramarSpider(scrapy.Spider):
    name = "beiramar"
    allowed_domains = ["shoppingbeiramar.com.br"]
    start_urls = ['http://www.shoppingbeiramar.com.br/cinema.html']

    def parse(self, response):
        for movie_link in response.css('div.cinema-filme-box'):
            url = response.urljoin(movie_link.css('a::attr(href)').extract_first())
            yield scrapy.Request(url, callback=self.movie_parse)

    def movie_parse(self, response):
        dub = response.css('div.filmes-dublados > ul > li::text')
        leg = response.css('div.filmes-legendados > ul > li::text')
        yield {
            'name': format_movie_name(response.css('h1.hNomeFilmeCompleto::text').extract_first()),
            'movie_theater': self.name.capitalize(),
            'url': response.url,
            'table': get_table_from_type(dub, 'DUB') + get_table_from_type(leg, 'LEG')
        }
