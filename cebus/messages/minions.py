# -*- coding: utf-8 -*-
'''
    Cebus minions models and messages
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

from cebus.messages import Unit



class BaseMinion(Unit):
    '''
        base schematics
    '''
	account = types.StringType(required=True)
    active = types.BooleanType(default=False)

    # TODO: Geo localization stuff ;)

    # location = StringType(required=True)
    # timezone = StringType(required=True)


# here comes the swarm


class Drone(BaseMinion):
	'''
		ZergORG Drone
	'''
	pass


class Overlord(BaseMinion):
	'''
		ZergORG Overlord
	'''
	pass


class Cerebrate(Cluster):
	'''
		ZergORG Cerebrate
	'''
	pass


class Ling(Unit):
	'''
		ZergORG Ling
	'''
	pass


class ZergORG(models.Model):
	'''
		ZergORG schematics
	'''
	drones = compound.ModelType(Drone)
	overlords = compound.ModelType(Overlord)
	cerebrates = compound.ModelType(Cerebrate)
	lings = compound.ModelType(Ling)


class MinionNode(Unit):
    '''
        Node basic data structure
    '''
    # minion centurion
    cebus = types.URLType(default=False)
    # minion overlord
    hawks =  types.URLType(default=True)
    # minion units
    capuchins = compound.ModelType(Unit)

    # minion squirrel servants
    squirrels = compound.ModelType(Unit)

    cores = types.IntType(default=8)
    total = types.IntType()


class MinionCluster(Unit):
    '''
        Minion cluster schematics
    '''
    nodes = compound.ModelType(MinionNode)

    cores = types.IntType(default=80)
    total = types.IntType()


class MinionCohort(Cohort):
	'''
        Minion cohort schematics
    '''
    clusters = compound.ModelType(MinionCluster)

    cores = types.IntType(default=480)
    total = types.IntType()


# stuff from the cloud forest
# cloud forest inmunes.


class Squirrel(BaseMinion):
	'''
		Squirrel immune
	'''
	pass


class Hawk(BaseMinion):
	'''
		Hawk immune
	'''
	pass


class Cebus(BaseMinion):
	'''
		Cebus capucinus immune
	'''
	pass


class Capuchin(BaseMinion):
	'''
		White-headed capuchin
	'''
	pass


class Spider(BaseMinion):
	'''
		Spider immune
	'''
	pass


class Howler(BaseMinion):
	'''
		Howler monkey
	'''
	pass


class Peccary(BaseMinion):
	'''
		Data peccary
	'''
	pass


class Scourge(BaseMinion):
	'''
		Capuchin scourge wild card
	'''
	pass


class CapuchinORG(models.Model):
	'''
		CapuchinORG schematics
	'''
	squirrels = compound.ModelType(Squirrel)
	hawks = compound.ModelType(Hawk)
	cebus = compound.ModelType(Cebus)
	capuchins = compound.ModelType(Capuchin)


class CapuchinImmunes(Unit):
	'''
		Immune units 
	
		The inmune concept born again from the roman legion
		just go a little back in time you!

		Special duty stuff; Immunes are units who possessed 
		specialized skills, qualifying them for better pay 
		and excusing them for labour and guard work.

		On the old empire, enginners, musicians, educators,
		carpenters, hunters, medical, etc. Are all inmune units.

		types of stuff: small, medium, high
	'''
	# http web spiders
	spiders = compound.ModelType(Spider)
	# sip real-time communication howlers
	howlers = compound.ModelType(Howler)
	# data peccaries
	peccaries = compound.ModelType(Peccary)

	# here you have a clean canvas.
	scourges = compound.ModelType(Scourge)

	# Inmunes unit skills
	# the hole inmmune concept born again from legionary organization 
	# just a few milenium back in time, you! ;)

	# Special duty stuff
	#
	# Immunes are units who possessed specialized skills, 
	# qualifying them fro better pay and excusing them 
	# for labour and guard work.

	# Engineers, Musicians, spscientists, educators, carpenters, 
	# hunters, medical are all inmune units.

	# Immunes worker basic contructor advanced constructor 

	# types of stuff: small, medium, high.


# the legion

class Servant(BaseMinion):
	'''
		Roman slave
	'''
	pass


class Decanus(BaseMinion):
	'''
		Roman Decanus
	'''
	pass


class Centurion(BaseMinion):
	'''
		Roman Centurion
	'''
	pass


class Legionary(BaseMinion):
	'''
		Roman Legionary
	'''
	pass


class LegionaryORG(models.Model):
	'''
		LegionaryORG schematics
	'''
	servant = compound.ModelType(Servant)
	decanus = compound.ModelType(Decanus)
	centurion = compound.ModelType(Centurion)
	legionary = compound.ModelType(Legionary)


