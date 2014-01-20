# -*- coding: utf-8 -*-
'''
    Cebus daemons handlers
'''
# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'

# daemons 

# kamailio source code url: http://www.kamailio.org/pub/kamailio/latest/src/
# describe with details how to get and compile the c source code of kamailio.

# the same for asterisk source code and compiling process, 
# remember that the task needs to be executed on every telecommunications minion.

import time
import motor
from tornado import gen
from tornado import web

from cebus.system import applications

from cebus.handlers import BaseHandler

from cebus.tools import content_type_validation
from cebus.tools import errors
from cebus.tools import check_json
from cebus.tools import check_timestamp

from bson import json_util

#@content_type_validation
class Handler(applications.Applications, BaseHandler):
    '''
        Cebus applications handler 
        
        Apps resource handler
    '''
    
    @web.asynchronous
    @gen.engine
    def get(self, app_id=None, page_num=0, start=None, stop=None):
        '''
            Cebus applications get handler

            Get apps registers
        '''
        if app_id:
            app_id = app_id.rstrip('/')
            
            if self.current_user:
                user = self.current_user
                app = yield motor.Op(self.get_app_record, user, app_id)
            else:
                app = yield motor.Op(self.get_app_record, None, app_id)
            
            if not app:
                self.set_status(400)
                system_error = errors.Error('missing')
                error = system_error.missing('app', app_id)
                self.finish(error)
                return
            
            self.finish(app)
            return
        
        if self.current_user:
            user = self.current_user
            orgs = yield motor.Op(self.get_orgs, user)

            cebus_accounts = (orgs['orgs'] if orgs else False)
            
            if not cebus_accounts:
                apps = yield motor.Op(self.get_apps_records,
                                       account=user, 
                                       elapse=None,
                                       start=None,
                                       stop=None,
                                       page=page_num)
            else:
                cebus_accounts.append(user)
                apps = yield motor.Op(self.get_apps_records,
                                       account=cebus_accounts,
                                       elapse=None,
                                       start=None,
                                       stop=None,
                                       page=page_num)
        else:
            apps = yield motor.Op(self.get_apps_records,
                                   account=None,
                                   elapse=None,
                                   start=None,
                                   stop=None,
                                   page=page_num)
        
        self.finish(json_util.dumps(apps))        
    
    @web.asynchronous
    @gen.engine
    def post(self):
        '''
            Cebus applications post handler

            Register a app record
        '''
        result = yield gen.Task(check_json, self.request.body)
        struct, error = result.args
        if error:
            self.set_status(400)
            self.finish(error)
            return

        records = yield gen.Task(self.new_app_record, struct)
        app_id, error = records.args    
            
        # WARNING: The complete error module it's going to be re-written
        if error:
            error = str(error)
            system_error = errors.Error(error)
            # Error handling 409?
            self.set_status(400)
        
        if error and 'Model' in error:
            error = system_error.model('Applications')
            self.finish(error)
            return
        elif error and 'duplicate' in error:
            error = system_error.duplicate('App', 'uniqueid', struct['uniqueid'])
            self.finish(error)
            return
        elif error:
            self.finish(error)
            return
        
        if 'accountcode' in struct:
            account = struct['accountcode']
            resource = {'account': account, 'resource':'applications', 'id':app_id}
            
            exist = yield motor.Op(self.check_exist, account)

            if exist:
                # update the account data set the app_id on applications resources
                update = yield motor.Op(self.new_resource, resource)
                
        # Set status
        self.set_status(201)

        # Return the new application id
        self.finish({'id':app_id})
    
    @web.authenticated
    @web.asynchronous
    @gen.engine
    def delete(self, app_id):
        '''
            Cebus applications delete handler

            Remove application records
        '''
        app_id = app_id.rstrip('/')
        result = yield motor.Op(self.remove_app, app_id)
        
        if not result['n']:
            self.set_status(400)
            system_error = errors.Error('missing')
            error = system_error.missing('app', app_id)
            self.finish(error)
            return
            
        self.set_status(204)
        self.finish()
    
    @web.authenticated
    @web.asynchronous
    @gen.engine
    def put(self):
        '''
            Cebus applications put handler
        '''
        pass
    
    @web.authenticated
    @web.asynchronous
    @gen.engine
    def patch(self):
        '''
            Cebus applications patch handler
        '''
        pass
    
    @web.authenticated
    @web.asynchronous
    @gen.engine
    def head(self):
        '''
            Cebus applications head handler
        '''
        pass