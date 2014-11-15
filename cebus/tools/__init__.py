# -*- coding: utf-8 -*-
'''
    Cebus tools
'''
# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


from collections import namedtuple
from operator import itemgetter
from pprint import pformat

import json
import motor

import arrow

from datetime import datetime as dt

from tornado import gen


class Node(namedtuple('Node', 'location left_child right_child')):
    def __repr__(self):
        return pformat(tuple(self))


@gen.engine
def check_json(struct, callback):
    '''
        Cebus check json
    
        Check for malformed JSON Object
        < kind of iterator/function >
        
        # TODO: check_json()
        
        example: TBD
    '''
    try:
        struct = json.loads(struct)
    except Exception, e:
        api_error = Error(e)
        error = api_error.json()
        callback(None, error)
        return
            
    callback(struct, None)

@gen.engine
def check_account_type(db, account, account_type, callback):
    '''
        Cebus check account type

        check account type
    '''
    try:
        check_type = yield motor.Op(db.accounts.find_one,
                                    {'account': account, 
                                     'type':account_type},
                                    {'type':1, '_id':0})
        # TODO: clean this TRUE TRUE
        if check_type:
            check_type = True
        else:
            check_type = False
    except Exception, e:
        callback(None, e)
    
    callback(check_type, None)
        
@gen.engine
def check_account_authorization(db, account, password, callback):
    '''
        Cebus check account authorization

        Check account authorization
    '''
    try:
        account = yield motor.Op(db.accounts.find_one,
                                 {'account': account,
                                  'password': password})
        
    except Exception, e:
        callback(None, e)
        return
    
    callback(account, None)

@gen.engine
def convert_timestamp(start, stop, callback):
    '''
        Cebus convert timestamp

        Kind of better name for check_timestamp
    
        This function gets two unix timestamps and returns a dict
        with a start and stiop datetime objects
    '''
    pass

@gen.engine
def check_timestamp(start, stop, callback):
    '''
        Cebus check timestamp

        Return datetime if gets a unix timestamp
    '''
    try:

        start = (dt.fromtimestamp(float(start)) if start else None)
        stop = (dt.fromtimestamp(float(stop)) if stop else None)
    except Exception, e:
        callback(None, e)
        return

    callback({'start':start, 'stop':stop}, None)

def clean_structure(struct):
    '''
        Cebus clean structure
    '''
    struct = struct.to_primitive()

    struct = {
        key: struct[key] 
            for key in struct
                if struct[key] is not None
    }

    return struct

def clean_results(results):
    '''
        Cebus clean results
    '''
    results = results.to_primitive()

    results = results['results']

    results = [
        {
            key: dic[key]
                for key in dic
                    if dic[key] is not None 
        } for dic in results 
    ]

    return {'results': results}

def content_type_validation(handler_class):
    '''
        Cebus content-type validation

        @content_type_validation decorator
    '''
    
    def wrap_execute(handler_execute):
        '''
            Content-Type checker

            Wrapper execute function
        '''
        def ctype_checker(handler, kwargs):
            '''
                Content-Type checker implementation
            '''
            content_type = handler.request.headers.get("Content-Type", "")         
            if content_type is None or not content_type.startswith('application/json'):
                handler.set_status(406)
                handler._transforms = []
                handler.finish({
                    'status': 406,
                    'message': 'Must ACCEPT application/json: '\
                    '[\"%s\"]' % content_type 
                })
                return False
            return True
        
        def _execute(self, transforms, *args, **kwargs):
            '''
                Execute the wrapped function
            '''
            if not ctype_checker(self, kwargs):
                return False
            return handler_execute(self, transforms, *args, **kwargs)
        
        return _execute
    
    handler_class._execute = wrap_execute(handler_class._execute)
    return handler_class

def kdtree(point_list, depth=0):
    '''
        https://en.wikipedia.org/wiki/K-d_tree
    '''
    try:
        k = len(point_list[0]) # assumes all points have the same dimension
    except IndexError as e: # if not point_list:
        return None
    # Select axis based on depth so that axis cycles through all valid values
    axis = depth % k
 
    # Sort point list and choose median as pivot element
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2 # choose median
 
    # Create node and construct subtrees
    return Node(
        location=point_list[median],
        left_child=kdtree(point_list[:median], depth + 1),
        right_child=kdtree(point_list[median + 1:], depth + 1)
    )

#def main():
#    """Example usage"""
#    point_list = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
#    tree = kdtree(point_list)
#    print(tree)
#
#if __name__ == '__main__':
#    main()