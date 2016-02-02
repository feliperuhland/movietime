# -*- coding: utf-8 -*-

import scrapy

from movietime.util import format_movie_name


class FloripaSpider(scrapy.Spider):
    name = "floripa"
    allowed_domains = ["floripashopping.com.br"]
    start_urls = ['http://www.floripashopping.com.br/cinema/']

    def parse(self, response):
        for movie_link in response.css('div.lista-filmes > div > div > div > a::attr(href)'):
            url = response.urljoin(movie_link.extract().replace('cinema/', ''))
            yield scrapy.Request(url, callback=self.movie_parse)

    def movie_parse(self, response):
        table = []
        for type_col in response.css('div.infos > div > table'):
            movie_type = type_col.css('thead > tr > th::text').extract_first()[:3]
            for line in type_col.css('tbody > tr > td'):
                table.append({
                    'type': movie_type,
                    'time': line.css('p::text')[0].extract().split(' - ')[-1].replace('h', ':')
                })
        yield {
            'name': format_movie_name(response.css('div.tit-principal > span::text').extract_first()),
            'movie_theater': self.name.capitalize(),
            'url': response.url,
            'table': table
        }
