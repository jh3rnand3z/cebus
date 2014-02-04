# -*- coding: utf-8 -*-
'''
    Cebus nodes system logic.
'''

# This file is part of cebus.

# Distributed under the terms of the last AGPL License.
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


import json

from cebus.messages.minions import Overlord
from cebus.messages.nodes import Conturbernium
from cebus.messages.nodes import Treant


class Node(object):
	'''
		Cebus node logic
	'''


    @gen.engine
    def new_node(self, struct, callback):
        '''
            Spawn node
        '''

        # validar el tipo de especie del nodo.

        try:
            node = nodes.Node(struct)
            node.validate()
        except Exception, e:
            callback(None, e)
            return

        node = clean_structure(node)

        result = yield gen.Task(self.db.nodes.insert, node)
        result, error = result.args

        if error:
            callback(None, error)
            return

        callback(node.get('uuid'), None)


	@gen.engine
    def get_node(self, account, node_uuid, callback):
        '''
            Get node
        '''
        try:
            if not account:
                node = yield motor.Op(
                    self.db.nodes.find_one, {
                    	'uuid': node_uuid
                    }
                )
            else:
                node = yield motor.Op(
                    self.db.nodes.find_one, {
                    	'uuid': node_uuid,
                        'account': account
                    }
                )
            if node:
            	node = nodes.Node(node)
            	node.validate()

        except Exception, e:
            callback(None, e)
            return

        callback(record, None)


	@gen.engine
    def get_nodes(self, account, callback):
        '''
            Get nodes
        '''
        page_num = int(page_num)
        page_size = self.settings['page_size']
        result = []

        if not account:

            query = self.db.nodes.find({'public':True})

        elif type(account) is list:

            accounts = [{'account':a, 'assigned': True} for a in account]

            query = self.db.nodes.find({'$or':accounts})
        else:
            query = self.db.nodes.find({'account':account,
                                        'assigned':True})

        query = query.sort([('uuid', -1)]).skip(page_num * page_size).limit(page_size)

        try:
            for record in (yield motor.Op(query.to_list)):
                result.append(records.Record(record))

            struct = {'results': result}
            results = reports.BaseResult(struct)
            results.validate()
        except Exception, e:
            callback(None, e)
            return

        results = clean_results(results)
        callback(results, None)


	@gen.engine
	def head_description(self, struct, callback):
		'''
		    Node head description
		'''
        # To be done by other fun head.
        pass


    @gen.engine
    def patch_node(self, struct, callback):
        '''
            Patch node
        '''
        # To be done by other fun head.
        pass	


	@gen.engine
	def delete_node(self, node_uuid, callback):
		'''
			Delete node
		'''
        try:
            result = yield motor.Op( self.db.nodes.remove,
                                     {'uuid':node_uuid} )
        except Exception, e:
            callback(None, e)
            return

        callback(result, None)


    @gen.engine
    def replace_node(self, struct, callback):
        '''
            Replace node
        '''
        try:
            node = nodes.Node(struct)
            node.validate()
        except Exception, e:
            callback(None, e)
            return

        node = clean_structure(node)
        
        result = yield gen.Task( self.db.nodes.update,
                                 {uuid: node.get('uuid')},
                                 node )
        result, error = result.args

        if error:
            callback(None, error)
            return

        callback(node.get('uuid'), None)


	@gen.engine
	def assign_node(self, struct, callback):
		'''
			Assign node
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