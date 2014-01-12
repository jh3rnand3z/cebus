# -*- coding: utf-8 -*-
'''
    Cebus base models
'''

# This file is part of cebus.
#
# Distributed under the terms of the last AGPL License. The full
# license is in the file LICENCE, distributed as part of this
# software.

__author__ = 'Jean Chassoul'

# Remember Gabo Naum.

import uuid

from schematics import models
from schematics import types
from schematics.types import compound


class BaseUnit(models.Model):
	'''
		Cebus base unit model
	'''
	active = types.BooleanType(default=True)
    uuid = types.UUIDType(default=uuid.uuid4)
    name = types.StringType(required=False)
    url = types.URLType()
    urls = compound.ListType(types.StringType())
    cores = types.IntType(default=8)


class Cohort(BaseUnit):
    '''
        Cohort data structure
    '''
    cores = types.IntType(default=480)
    centurias = compound.ListType(types.StringType())


class Centuria(BaseUnit):
    '''
        Centuria data structure
    '''
    cores = types.IntType(default=80)
    nodes = compound.ListType(types.StringType())


class Node(BaseUnit):
    '''
        Node basic data structure
    '''
    minions = compound.ListType(types.StringType())