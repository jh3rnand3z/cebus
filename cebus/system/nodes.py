

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
