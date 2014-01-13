#!/usr/bin/env python
'''
    Cebus applications api
'''
import datetime as dt
import pandas as pd

import motor

from tornado import gen

from bson import json_util
from bson import objectid

from cebus.messages import applications


class Applications(object):
    '''
        Cebus applications API

        Application API resources
    '''
    
    @gen.engine
    def new_app_record(self, struct, callback):
        '''
            Create a new application record
        '''
        try:
            app = applications.Application(**struct).validate()
        except Exception, e:
            callback(None, e)
            return
        
        records = yield gen.Task(self.db.apps.insert, app)
        result, error = records.args
            
        if error:
            callback(None, error)
            return
        
        callback(str(result), None)
    
    @gen.engine
    def get_app_record(self, account, app_id, callback):
        '''
            Get a single application record
        '''
        try:
            if not account:
                app = yield motor.Op(self.db.apps.find_one,
                                      {'_id':objectid.ObjectId(app_id)})
            else:
                app = yield motor.Op(self.db.apps.find_one,
                                      {'_id':objectid.ObjectId(app_id),
                                       'accountcode':account})
            if app:
                app = applications.Application(**app).validate()
        except Exception, e:
            callback(None, e)
            return
        
        callback(app, None)
    
    
    @gen.engine
    def get_apps_records(self, account, elapse, start, stop, page, callback):
        '''
            Get a list of records from multiple applications
        '''
        page = int(page)
        page_size = self.settings['page_size']
        result = []
        
        if not account:
            query = self.db.apps.find({'public':True})
        elif type(account) is list:
            accounts = [{'accountcode':a, 'assigned': True} for a in account]
            query = self.db.apps.find({'$or':accounts})
        else:
            query = self.db.apps.find({'accountcode':account,
                                        'assigned':True})
        
        query = query.sort([('_id', -1)]).skip(page * page_size).limit(page_size)
        
        try:
            for app in (yield motor.Op(query.to_list)):
                result.append(applications.Application(**app).validate())
        except Exception, e:
            callback(None, e)
            return
        
        callback({'results':result}, None)
    

    @gen.engine
    def remove_app(self, app_id, callback):
        '''
            Remove application records
        '''
        try:
            result = yield motor.Op(self.db.apps.remove,
                                    {'_id':objectid.ObjectId(app_id)})
        except Exception, e:
            callback(None, e)
            return
        
        callback(result, None)