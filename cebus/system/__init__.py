# -*- coding: utf-8 -*-
'''
    Central Execution Bus UNIX System Utility Supervisor.
    
    Cebus for short; cebus artificial intelligence system; 
    cebus is a ai system utility supervisor for computing clouds.
'''

# This file is part of cebus.
#
# Distributed under the terms of the last AGPL License. 

# The full license is in the file LICENCE, distributed as part of this software.

# The hunter told him that this was, without a doubt, the hoof print 
# of a Pixiu, being different from the hoof-print of any other beast alive.
#
# His conversation with the hunter greatly inspired Cangjie, leading him to 
# believe that if he could capture in a drawing the special characteristics
# that set apart each and every thing on the earth, this would truly be the
# perfect kind of character for writing. 
#
# From that day forward, Cangjie paid close attention to the characteristics
# of all things, including the sun, moon, stars, clouds, lakes, oceans, 
# as well as all manner of bird and beast.
#
# He began to create characters according to the special characteristics
# he found, and before long, had compiled a long list of characters for writing.

# research more about recursion.

# TODO: information about goals strategies and analogies 
# from Carl Hewitt talks about ORGs.

# cohort = {
# 	centuria: 6
# }

# centuria = {
#	centurion: 1,
#	optio: 1,
#	guard: 1,		# node of 8 computer guards.
#	decanus: 8		# node of 8 minions, basic working force.
# }

# node = {
#	capuchins: 8
# }

# centurion; 1 one for each centuria.

# lower ranks
# optio, guard, decanus, capuchin

# optio 1 for each centurion
# guard commander, 1 one for each centuria.
# decanus; Commmand a 8 eight unit 10 tent party.

# capuchin minion the basic unit (1 minion 1 core).

__author__ = 'Jean Chassoul'

from tornado import gen

from cebus.messages import Cohort, Centuria, Node

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


class Centuria(object):
	'''
		Cebus centuria logic
	'''

	@property
    def double(self):
        '''
            Double Cohort
        '''
        return self.double

	def __init__(self):
		self.cores = 80
		self.cores_double = 160
		self.double = False

	@gen.engine
	def new_centuria(self, struct, callback):
		'''
			Spawn new centuria
		'''

	@gen.engine
	def delete_centuria(self, struct, callback):
		'''
			Delete centuria
		'''

	@gen.engine
	def assign_centuria(self, struct, callback):
		'''
			Assign centuria
		'''

	@gen.engine
	def get_centuria(self, struct, callback):
		'''
			Get centuria
		'''

	@gen.engine
	def get_centurias(self, struct, callback):
		'''
			Get centurias
		'''

	@gen.engine
	def check_exist(self, struct, callback):
		'''
			Check if centuria exist
		'''

	@gen.engine
	def check_type(self, struct, callback):
		'''
			Check centuria type
		'''

	@gen.engine
	def get_status(self, struct, callback):
		'''
			Get centuria status
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