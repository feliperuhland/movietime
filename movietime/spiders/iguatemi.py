# -*- coding: utf-8 -*-

import scrapy

from movietime.util import format_movie_name


def _get_type(movie_type):
    if movie_type in ['DUB', 'NAC']:
        return 'DUB'
    return movie_type


class IguatemiSpider(scrapy.Spider):
    name = "iguatemi"
    allowed_domains = ["iguatemi.com.br"]
    start_urls = ['http://iguatemi.com.br/florianopolis/cinema/']

    def parse(self, response):
        for movie_link in response.css('article.filmeContainer'):
            url = response.urljoin(movie_link.css('a::attr(href)')[0].extract())
            yield scrapy.Request(url, callback=self.movie_parse)

    def movie_parse(self, response):
        movie_time = [mt for mt in response.css('section.detalhes > ul > li > p::text').extract_first().split(' | ')]
        yield {
            'name': format_movie_name(response.css('header.filmeTitle > h1::text').extract_first()),
            'movie_theater': self.name.capitalize(),
            'url': response.url,
            'table': [{
                    'time': movie_type.split(' ')[0].replace('*', ''),
                    'type': _get_type(movie_type.split(' ')[1])
                } for movie_type in movie_time
            ],
        }
