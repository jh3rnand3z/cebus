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

from cebus.messages import Node



class BaseMinion(Unit):
    '''
        base schematics
    '''
	account = types.StringType(required=True)
    active = types.BooleanType(default=False)

    # TODO: Geo localization stuff ;)

    # location = StringType(required=True)
    # timezone = StringType(required=True)


# the fucking legion

class Centurion(BaseMinion):
	'''
		Roman Centurion
	'''
	pass


class Decanus(BaseMinion):
	'''
		Roman Decanus
	'''
	pass


class Legionary(BaseMinion):
	'''
		Roman Legionary
	'''
	pass


class Servant(BaseMinion):
	'''
		Roman Slave
	'''
	pass


class LegionaryORG(models.Model):
	'''
		LegionaryORG schematics
		-----------------------

		The Legion comprised ten cohorts, known simply as "the first cohort",
		"the second cohort" etc.

		The first cohort was considered to be the most senior and prestigious,
		and the tenth the least.

		A cohort consisted of approximately 480 men and commanded by one man.

		It consisted of six centuriae of 80 men, each commanded by a centurion 
		assisted by junior officers.

		The most senior centurion of the six command the entire cohort.
	'''
	centurion = compound.ModelType(Centurion)
	decanus = compound.ModelType(Decanus)
	legionary = compound.ModelType(Legionary)
	servant = compound.ModelType(Servant)


# the swarm

class Queen(BaseMinion):
	'''
		ZergORG Queen
	'''
	pass


class Cerebrate(Cluster):
	'''
		ZergORG Cerebrate
	'''
	pass


class Larva(BaseMinion):
	'''
		New and freaking out! Unexpected eggs
	'''
	pass


class Ling(Unit):
	'''
		ZergORG Ling
	'''
	pass


class Drone(BaseMinion):
	'''
		ZergORG Drone
	'''
	pass


class ZergORG(models.Model):
	'''
		ZergORG schematics
		------------------

		The Queen controls the Swarm through secondary agents called cerebrates. 

		Cerebrates command an individual cohort of ZergORG, 
		each with a distinct tactical role within the hierarchy. 

		Cerebrates further delegate power through the use of overlords 
		for battlefield direction and queens for hive watch.


		###Some notes about the species

		the ZergORG do not use technology; 

		Instead, they assimilate other species traits by directed mutation
		in order to match such technology.

		ZergORG units are designed to be cheap and fast to produce,
		encouraging players to overwhelm their opponents with sheer numbers.
	'''
	queens = compound.ModelType(Queen)
	cerebrates = compound.ModelType(Cerebrate)
	overlords = compound.ModelType(Overlord)
	lings = compound.ModelType(Ling)
	drones = compound.ModelType(Drone)


# tropical cloud forest

class TropicalNode(Node):
    '''
        Node basic data structure
    '''
    # minion centurion
    cebus = types.URLType(default=False)
    # minion overlord
    hawks = types.URLType(default=True)
    # minion units
    capuchins = compound.ModelType(Unit)
    # minion squirrel servants
    squirrels = compound.ModelType(Unit)


class MinionCluster(Unit):
    '''
        Minion cluster schematics
    '''
    nodes = compound.ModelType(TropicalNode)

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
		Web Spider monkey
	'''
	pass


class Howler(BaseMinion):
	'''
		Communication Howler monkey
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
		----------------------

		hablada de mierda.

		bosques, squirrels, capuchinos, hawks, peccaries, howlers, scourges

		el ultimo comodin, howlers communicacion, peccaries databases, 
		hawks supervisor overlords, capuchin standard legionary, 
		squirrels are slaves, all live in the forest.

		


	'''
	cebus = compound.ModelType(Cebus)
	hawks = compound.ModelType(Hawk)
	capuchins = compound.ModelType(Capuchin)
	squirrels = compound.ModelType(Squirrel)


class CapuchinImmunes(Unit):
	'''
		Immune units
		------------
	
		The inmune concept born again from the roman legion
		just go a little back in time you!

		Special duty stuff; Immunes are units who possessed 
		specialized skills, qualifying them for better pay 
		and excusing them for labour and guard work.

		On the old empire, enginners, musicians, educators,
		carpenters, hunters, medical, etc. Are all inmune units.

		types of stuff: small, medium, high
	'''

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

	# http web spiders
	spiders = compound.ModelType(Spider)
	# sip real-time communication howlers
	howlers = compound.ModelType(Howler)
	# data peccaries
	peccaries = compound.ModelType(Peccary)

	# here you have a clean canvas.
	scourges = compound.ModelType(Scourge)