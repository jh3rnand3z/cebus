# -*- coding: utf-8 -*-
'''
    Central Execution Bus UNIX System Utility Supervisor.
    
    Cebus for short; cebus AI supervisor for computing clouds.
'''

# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


from tornado import gen

from cebus.messages import Cluster, Cohort


class BasicCommands(object):
	'''
		Basic commands
	'''

	@property
	def action(self):
		'''
			action function
		'''
		return self.action 

	@property
	def move(self):
		'''
			move function
		'''
		return self.move
	
	@property
	def stop(self):
		'''
			stop function
		'''
		return self.stop
	
	@property
	def hold(self):
		'''
			hold function
		'''
		return self.hold

	@property
	def patrol(self):
		'''
			patrol function
		'''
		return self.patrol

	@property
	def build(self):
		'''
			build function
		'''
		return self.build

	@property
	def repair(self):
		'''
			repair function
		'''
		return self.repair

	def _init__(self):
		'''
			Cebus system commands
		'''
		self.action = None
		self.move = None
		self.stop = None
		self.hold = None
		self.patrol = None
		self.build = None
		self.repair = None



class Cluster(object):
	'''
		Cebus cluster logic
	'''

	@property
    def double(self):
        '''
            Double Cluster
        '''
        return self.double

	def __init__(self):
		self.cores = 80
		self.cores_double = 160
		self.double = False

	@gen.engine
	def new_cluster(self, struct, callback):
		'''
			Spawn new cluster
		'''

	@gen.engine
	def delete_cluster(self, struct, callback):
		'''
			Delete cluster
		'''

	@gen.engine
	def assign_cluster(self, struct, callback):
		'''
			Assign cluster
		'''

	@gen.engine
	def get_cluster(self, struct, callback):
		'''
			Get cluster
		'''

	@gen.engine
	def get_clusters(self, struct, callback):
		'''
			Get cluster
		'''

	@gen.engine
	def check_exist(self, struct, callback):
		'''
			Check if cluster exist
		'''

	@gen.engine
	def check_type(self, struct, callback):
		'''
			Check cluster type
		'''

	@gen.engine
	def get_status(self, struct, callback):
		'''
			Get cluster status
		'''



class Cohort(object):
	'''
		Cebus cohort logic
	'''

	@property
    def double(self):
        '''
            Double Cohort
        '''
        return self.double

	def __init__(self):
		self.cores = 480
		self.cores_double = 960
		self.double = False

	@gen.engine
	def new_cohort(self, struct, callback):
		'''
			New cohort
		'''

	@gen.engine
	def delete_cohort(self, struct, callback):
		'''
			Delete cohort
		'''

	@gen.engine
	def assign_cohort(self, struct, callback):
		'''
			Assign cohort
		'''

	@gen.engine
	def get_cohort(self, struct, callback):
		'''
			Get cohort
		'''

	@gen.engine
	def get_cohorts(self, struct, callback):
		'''
			Get cohorts
		'''

	@gen.engine
	def check_exist(self, struct, callback):
		'''
			Check if cohort exist
		'''

	@gen.engine
	def check_type(self, struct, callback):
		'''
			Check cohort type
		'''

	@gen.engine
	def get_status(self, struct, callback):
		'''
			Get cohort status
		'''