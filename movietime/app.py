# coding: utf-8

import collections
import json

import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
        ]
        settings = dict(template_path=os.path.join(os.path.dirname(__file__), "templates"))
        super(Application, self).__init__(handlers, **settings)


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        movie_theater = [
            'beiramar',
            'iguatemi',
            'floripa',
        ]
        entries = {}

        for mt in movie_theater:
            with open('output/{}.json'.format(mt)) as json_file:
                for item in json.load(json_file):
                    entries.setdefault(item['name'], []).append(item)

        self.render("index.html", entries=collections.OrderedDict(sorted(entries.items(), key=lambda x: x)))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
