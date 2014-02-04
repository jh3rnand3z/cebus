# -*- coding: utf-8 -*-
'''
    Cebus HTTP nodes handlers
'''

# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'

import arrow
import motor

'''

Revolutionary Open Source

How to change the game by helping selfish people work together on your projects

Pieter Hintjens
ZeroMQ.org


'''

# import numpy as np
# import pandas as pd

#from bson import json_util

from tornado import gen
from tornado import web

from cebus.handlers import BaseHandler



@content_type_validation
class Handler(BaseHandler):
    '''       
        Records resource handler
    '''

    @web.asynchronous
    @gen.engine
    def get(self, node_uuid=None):
        '''
            nodes get handler

            Get node objects
        '''
        if record_uuid:
            record_uuid = record_uuid.rstrip('/')

            if self.current_user:
                user = self.current_user
                record = yield motor.Op(self.get_detail_record, user, record_uuid)
            else:
                record = yield motor.Op(self.get_detail_record, None, record_uuid)

            if not record:
                self.set_status(400)
                system_error = errors.Error('missing')
                error = system_error.missing('record', record_uuid)
                self.finish(error)
                return

            self.finish(record)
            return

        if self.current_user:
            user = self.current_user
            orgs = yield motor.Op(self.get_orgs, user)

            mango_accounts = (orgs['orgs'] if orgs else False)

            print(user, orgs, ' on get record objects.')

            if not mango_accounts:
                result = yield motor.Op(self.get_detail_records,
                                        account=user, 
                                        lapse=lapse,
                                        start=start,
                                        stop=stop,
                                        page_num=page_num)
            else:
                mango_accounts.append(user)
                result = yield motor.Op(self.get_detail_records,
                                        account=mango_accounts,
                                        lapse=lapse,
                                        start=start,
                                        stop=stop,
                                        page_num=page_num)
        else:
            result = yield motor.Op(self.get_detail_records,
                                    account=None,
                                    lapse=lapse,
                                    start=start,
                                    stop=stop,
                                    page_num=page_num)
        
        self.finish(json_util.dumps(result))

    @web.authenticated
    @web.asynchronous
    @gen.engine
    def head(self):
        '''
            node head handler
        '''
        pass

    @web.asynchronous
    @gen.engine
    def post(self):
        '''
            node post handler

            Register a record detail record
        '''

        result = yield gen.Task(check_json, self.request.body)
        struct, error = result.args
        
        if error:
            self.set_status(400)
            self.finish(error)
            return

        result = yield motor.Op(self.new_detail_record, struct)
 
        # WARNING: The complete error stuff is going to be re-written
        
        # cuz it sucks right now!
        
        if error:
            print('error 2')
            error = str(error)
            system_error = errors.Error(error)
            # Error handling 409?
            self.set_status(400)
        
        if error and 'Model' in error:
            error = system_error.model('Records')
            self.finish(error)
            return
        elif error and 'duplicate' in error:
            error = system_error.duplicate('Record', 'uniqueid', struct['uniqueid'])
            self.finish(error)
            return
        elif error:
            print('error 3')
            self.finish(error)
            return
        
        if 'accountcode' in struct:
            account = struct['accountcode']

            resource = {'account': account, 'resource':'records', 'uuid':result}

            exist = yield motor.Op(self.check_exist, account)

            if exist:
                
                update = yield motor.Op(self.new_resource, resource)

                flag = yield motor.Op(self.set_assigned_flag,
                                      account,
                                      result)

                print('after flag')


        self.set_status(201)
        self.finish({'id':result})

    @web.authenticated
    @web.asynchronous
    @gen.engine
    def put(self):
        '''
            node put handler

            Replace a registered node
        '''
        pass

    @web.authenticated
    @web.asynchronous
    @gen.engine
    def delete(self, record_uuid):
        '''
            node delete handler

            Remove a record register
        '''
        record_uuid = record_uuid.rstrip('/')
        result = yield motor.Op(self.remove_cdr, record_uuid)
        
        if not result['n']:
            self.set_status(400)
            system_error = errors.Error('missing')
            error = system_error.missing('record', record_uuid)
            self.finish(error)
            return
            
        self.set_status(204)
        self.finish()
    
    @web.authenticated
    @web.asynchronous
    @gen.engine
    def options(self):
        '''
            node options handler
        '''
        pass

    @web.authenticated
    @web.asynchronous
    @gen.engine
    def patch(self):
        '''
            node patch handler
        '''
        pass