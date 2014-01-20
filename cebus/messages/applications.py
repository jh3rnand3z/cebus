# -*- coding: utf-8 -*-
'''
    Cebus applications models and messages
'''
# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


# Remember Gabo Naum.
import uuid

from schematics import models
from schematics import types
from schematics.types import compound

from schematics.contrib import mongo


class BaseApp(models.Model):
    '''
        Cebus base application

        Apps basic data structure
    '''
    id = mongo.ObjectIdType(required=False)

    uuid = types.UUIDType(default=uuid.uuid4)
    
    active = types.BooleanType(default=True)
    name = types.StringType(required=False)
    url = types.URLType()
    
    
class Application(BaseApp):
    '''
        Cebus application

        Application data structure
    '''
    accounts = compound.ListType(types.StringType())
    total = types.IntType()