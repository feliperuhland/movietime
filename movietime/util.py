# coding: utf-8

from slugify import slugify


def format_movie_name(movie_name):
    return slugify(movie_name, separator=' ').upper().replace('O FILME', '')
