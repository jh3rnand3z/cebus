# -*- coding: utf-8 -*-
'''
    Cebus nodes
'''
# This file is part of cebus.

# Distributed under the terms of the last AGPL License.
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'

from cebus.messages import Unit

import json


class Node(object):
	'''
		Cebus node logic
	'''
	
	@gen.engine
	def new_node(self, struct, callback):
		'''
			Spawn node
		'''


	@gen.engine
	def delete_node(self, struct, callback):
		'''
			Delete node
		'''

	@gen.engine
	def assign_node(self, struct, callback):
		'''
			Assign node
		'''

	@gen.engine
	def get_node(self, struct, callback):
		'''
			Get node
		'''
		
	@gen.engine
	def get_nodes(self, struct, callback):
		'''
			Get nodes
		'''

	@gen.engine
	def check_exist(self, struct, callback):
		'''
			Check if node exist
		'''

	@gen.engine
	def check_type(self, struct, callback):
		'''
			Check node type
		'''

	@gen.engine
	def get_status(self, struct, callback):
		'''
			Get node status
		'''
