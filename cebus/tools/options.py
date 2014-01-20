# -*- coding: utf-8 -*-
'''
    Cebus daemon configuration options
'''
# This file is part of cebus.
#
# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


import base64
import uuid
import os

import tornado.options

secret = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
config_path = 'cebus.conf'

def options():
    '''
        Cebus configuration options
    '''
    # Startup options
    tornado.options.define('ensure_indexes', default=True, type=bool, 
                           help=('Ensure collection indexes before starting'))
    # cebus debug mode
    
    # TODO: add, check and test the debug mode.

    # tornado.options.define('debug', default=False, type=bool, help=(
    #     'Turn on autoreload, log to stderr only'))
    # tornado.options.define('logdir', type=str, default='log', help=(
    #     'Location of logging (if debug mode is off)'))

    # Server settings
    tornado.options.define('host', default='127.0.0.1', type=str,
                           help=('Server hostname'))
    tornado.options.define('port', default=8889, type=int,
                           help=('Server port'))
    tornado.options.define('base_url', default='ai', type=str,
                           help=('Base url, e.g. "ai"'))
    
    # Requests with return settings
    # Pagination - Requests that return multiple items will be paginated
    # to 30 items by default.
    tornado.options.define('page_size', default=30, type=int,
                           help=('Set a custom page size up to 100'))
    tornado.options.define('cookie_secret', default=secret, type=str,
                           help=('Secure cookie secret string'))
    
    # Records settings
    tornado.options.define('record_streamer', default='', type=str,
                           help='Record streamer')
    tornado.options.define('record_streamer_host', default='127.0.0.1', type=str,
                           help='Record streamer host')
    tornado.options.define('record_streamer_port', default=5555, type=int,
                           help='Record streamer port')
    
    tornado.options.define('record_periodic_stuff', default='', type=str,
                           help='Record periodic stuff')
    
    tornado.options.define('periodic_records', default='', type=str,
                           help='Periodic Records Callbacks')
    
    # Parse config file, then command line, so command line switches take
    # precedence
    if os.path.exists(config_path):
        print 'Loading', config_path
        tornado.options.parse_config_file(config_path)
    else:
        print 'No config file at', config_path

    tornado.options.parse_command_line()
    result = tornado.options.options

    for required in (
        'host', 'port', 'base_url',
    ):
        if not result[required].value():
            raise Exception('%s required' % required)

    return result