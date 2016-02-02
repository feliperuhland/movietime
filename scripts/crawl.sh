#!/bin/sh

set -e 

scrapy crawl iguatemi -o output/iguatemi.json
scrapy crawl beiramar -o output/beiramar.json
scrapy crawl floripa -o output/floripa.json

