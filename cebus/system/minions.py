# -*- coding: utf-8 -*-
'''
    Cebus campaings system logic.
'''
# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


import json

import motor

from tornado import gen

from cebus.messages import minions

# drones, overlord, guardian, capuchin, wizard, 

class Minions(object):
    '''
        Cebus minions system logic
    '''

    @gen.engine
    def new_minion(self, struct, callback):
        '''
            Spawn a new minion
        '''

    @gen.engine
    def stop_minion(self, struct, callback):
        '''
            Stop minion execution
        '''

    @gen.engine
    def assign_minion(self, struct, callback):
        '''
            Assign command
        '''

    @gen.engine
    def get_minion(self, struct, callback):
        '''
            Get a spawned minion
        '''

    @gen.engine
    def get_minions(self, struct, callback):
        '''
            Get all the spawned minions
        '''

    @gen.engine
    def check_exist(self, struct, callback):
        '''
            Check exist command
        '''

    @gen.engine
    def check_type(self, struct, callback):
        '''
            Check type command
        '''

    @gen.engine
    def get_status(self, struct, callback):
        '''
            Get status command
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