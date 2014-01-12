# -*- coding: utf-8 -*-
'''
    Cebus base handlers
'''

# This file is part of cebus.
#
# Distributed under the terms of the last AGPL License. The full
# license is in the file LICENCE, distributed as part of this
# software.

__author__ = 'Jean Chassoul'


# Remember Cangjie


import motor

from tornado import gen
from tornado import web

from cebus.tools import errors


class BaseHandler(web.RequestHandler):
    '''
        Cebus Base Handler
    '''

    @property
    def db(self):
        '''
            Cebus database
        '''
        return self.application.db
    
    def initialize(self, **kwargs):
        ''' 
            Initialize the Base Handler
        '''
        super(BaseHandler, self).initialize(**kwargs)

        self.etag = None
        
        # Mongodb database
        self.db = self.settings['db']

        # ZeroMQ streams
        # self.cdr_stream = self.settings['cdr_stream']

        # Tornado CDR periodic callbacks
        # self.cdr_periodic = self.settings['cdr_periodic']

        # Pagination settings
        self.page_size = self.settings['page_size']

    def set_default_headers(self):
        '''
            Cebus default headers
        '''
        self.set_header("Access-Control-Allow-Origin", "cebus.ca")
    
    def get_current_user(self):
        '''
            Return the username from a secure cookie
        '''
        return self.get_secure_cookie('username')   
    

class HomeHandler(BaseHandler):
    '''
        Hello World
    '''

    @web.asynchronous
    def get(self):
        '''
            Get some fun
        '''
        
        self.write({'hello': 'hello world!'})
        self.finish()