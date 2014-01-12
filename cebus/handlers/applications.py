#!/usr/bin/env python
'''
    Cebus applications handlers
'''
import time
import motor
import pandas as pd

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