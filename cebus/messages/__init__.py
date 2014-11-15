# -*- coding: utf-8 -*-
'''
    Cebus base models and messages
'''

# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


# Remember Gabo Naum.

# System primitives:

# Unit, Node, Cluster, Cohort, Cloud. (5) five stuff rule.

# post, get, head, patch, put, delete, options. (7) Current HTTP methods.

import uuid

from schematics import models
from schematics import types
from schematics.types import compound



class ResourceContainer(models.Model):
    '''
        Cebus resource container
    '''
    contains = compound.ListType(types.UUIDType())

    total = types.IntType()


class ContactsContainer(models.Model):
    '''
        Contacts addresses container
    '''
    addresses = compound.ModelType(ResourceContainer)

    total = types.IntType()


class Resource(models.Model):
    ''' 
        Cebus system resource
    '''
    applications = compound.ModelType(ResourceContainer)
    analogies = compound.ModelType(ResourceContainer)
    behaviours = compound.ModelType(ResourceContainer)
    campaigns = compound.ModelType(ResourceContainer)

    goals = compound.ModelType(ResourceContainer)
    strategies = compound.ModelType(ResourceContainer)
    daemons = compound.ModelType(ResourceContainer)

    minions = compound.ModelType(ResourceContainer)

    nodes = compound.ModelType(ResourceContainer)
    clusters = compound.ModelType(ResourceContainer)
    cohorts = compound.ModelType(ResourceContainer)
    clouds = compound.ModelType(ResourceContainer)

    stations = compound.ModelType(ResourceContainer)
    structures = compound.ModelType(ResourceContainer)

    total = types.IntType()


class Unit(models.Model):
    '''
        Cebus base unit model
    '''
    name = types.StringType(required=False)
    uuid = types.UUIDType(default=uuid.uuid4)

    contacts = compound.ModelType(ContactsContainer)

    url = types.URLType()
    urls = compound.ListType(types.StringType())

    resources = compound.ModelType(Resource)

    cores = types.IntType(default=1)
    total = types.IntType()


class Node(Unit):
    '''
        Node basic data structure
    '''
    minions = compound.ModelType(Unit)
    servants = compound.ModelType(Unit)

    cores = types.IntType(default=8)
    # D:
    total = types.IntType()


class Cluster(Unit):
    '''
        Cluster data structure
    '''
    nodes = compound.ModelType(Node)

    cores = types.IntType(default=80)
    # ojo este total esta mamando.
    total = types.IntType()


class Cohort(Unit):
    '''
        Cohort data structure
    '''
    clusters = compound.ModelType(Cluster)

    cores = types.IntType(default=480)
    # alchile?
    total = types.IntType()


class Cloud(Unit):
    '''
        Cloud data structure
    '''
    cohorts = compound.ModelType(Cohort)

    cores = types.IntType(default=4800)
    # it looks like it.
    total = types.IntType()

# NOTA: el problema es con repetir una y otra vez el mismo total vacio, no es necesario ya que la shit se hereda de Unit.
# testear esta hablada de mierda.