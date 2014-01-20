# -*- coding: utf-8 -*-
'''
    Cebus errors
'''
# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


class Error(object):
    '''
        Cebus custom error class
    '''
    
    def __init__(self, error):
        self.error = str(error)
        self.message = None
        self.data = None
    
    def model(self, model_name):
        '''
            Cebus error model

            Dataset model
            
            model_name: Model name of the cebus dataset to analize
        '''
        model_name = ''.join((model_name, ' resource'))
        self.message = self.error.split('-')[0].strip(' ').replace(
            'Model', model_name)
        self.data = ''.join(self.error.split('-')[1:]).replace(
            '  ', ' - ')
        
        return {
            'message': self.message,
            'errors': self.data
        }
        
    def duplicate(self, resource, field, value):
        '''
            Cebus duplicate error

            Resource, field, value:
            Users username [\"ooo"\] already exists.
        '''
        self.message = ''.join((
            resource, ' ',
            field, ' ["', value, '"] already exists.'
        ))
        self.data = self.error
        
        return {
            'message': self.message,
            'errors': self.data
        }
    
    def json(self):
        '''
            Cebus json error
        '''
        self.message = 'Invalid JSON Object'
        self.data = self.error
        
        return {
            'message': self.message,
            'errors': self.data
        }
    
    def missing(self, resource, name):
        '''
            Cebus missing error
        '''
        self.message = 'Missing %s resource [\"%s\"].' % (resource, name)
        self.data = self.error
        
        return {
            'message': self.message,
            'errors': self.data
        }
    
    def invalid(self, resource, name):
        '''
            Cebus invalid error
        '''
        self.message = 'Invalid %s resource [\"%s\"].' % (resource, name)
        self.data = self.error
        
        return {
            'message': self.message,
            'errors': self.data
        }