# -*- coding: utf-8 -*-
'''
    Cebus HTTP base handlers
'''

# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


# Remember Cangjie


import motor

from tornado import gen
from tornado import web

from cebus.tools import errors


'''
    Request methods
    ---------------

    HTTP defines methods (sometimes referred to as fucking verbs) 
    to indicate the desired action to be performed on the Universal Unique 
    Identified (Resource) node, cluster, cohort, cloud.

    What this resource represents, whether pre-existing data or data that
    is generated dynamically, depends on the implementation of the server.

    Often, the resource corresponds to a file or the output of an executable
    residing on the server.

    The HTTP/1.0 specification:
        section 8 defined the GET, POST and HEAD methods

    HTTP/1.1 specification:
        section 9 added 5 new methods: OPTIONS, PUT, DELETE, TRACE and CONNECT.

    By being specified in these documents their semantics are well known 
    and can be depended upon.

    Any client can use any method and the server can be configured 
    to support any combination of methods.

    If a method is unknown to an intermediate it will be treated 
    as an unsafe and non-idempotent method.

    There is no limit to the number of methods that can be defined 
    and this allows for future methods to be specified without 
    breaking existing infrastructure. 

    RFC5789 specified the PATCH method.

    so... after all that stuff, we're coding on:

    [GET]
        Requests a representation of the specified resource.

        Requests using GET should only retrieve data and should have no other effect. 

        (This is also true of some other HTTP methods.)

    [HEAD]
        Asks for the response identical to the one that would correspond to a GET request, 
        but without the response body. 

        This is useful for retrieving meta-information written in response headers, 
        without having to transport the entire content.

    POST
        Requests that the server accept the entity enclosed in the request 
        as a new subordinate of the web resource identified by the URI.

        The data POSTed might be, as examples, an annotation for existing resources; 
        a message for a bulletin board, newsgroup, mailing list, or comment thread; 
        a block of data that is the result of submitting a web form to a data-handling process; 
        or an item to add to a database.

    PUT
        Requests that the enclosed entity be stored under the supplied URI. 

        If the URI refers to an already existing resource, it is modified; 
        if the URI does not point to an existing resource, then the server 
        can create the resource with that URI.

    DELETE
        Deletes the specified resource.

    [OPTIONS]
        Returns the HTTP methods that the server supports for the specified URL. 

        This can be used to check the functionality of a web server by requesting '*' 
        instead of a specific resource.

    PATCH
        Is used to apply partial modifications to a resource.

'''


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

        # DOMAIN

        self.set_header("Access-Control-Allow-Origin", "cebus.ca")
    
    def get_current_username(self):
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