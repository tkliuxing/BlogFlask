#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from blogflask import app
import blogflask
import optparse
import sys


def option_parser():
    opt_p = optparse.OptionParser()
    opt_p.add_option(
        "-P", "--port",
        action="store",
        type="int",
        dest="port",
        default="5000",
    ).container.add_option(
        "-H", "--host",
        action="store",
        type="string",
        dest="host",
        default="127.0.0.1",
    ).container.add_option(
        "--debug",
        action="store_true",
        dest="debug",
    )
    (options, args) = opt_p.parse_args(sys.argv)
    return options


if __name__ == '__main__':
    OPTIONS = option_parser()
    port = OPTIONS.port
    host = OPTIONS.host
    app.debug = OPTIONS.debug or getattr(blogflask, 'DEBUG', False)
    app.run(port=port,host=host)
