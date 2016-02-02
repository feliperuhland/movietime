# -*- coding: utf-8 -*-

# Scrapy settings for movietime project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movietime'

SPIDER_MODULES = ['movietime.spiders']
NEWSPIDER_MODULE = 'movietime.spiders'

DOWNLOAD_DELAY = 3

HTTPCACHE_ENABLED = False
