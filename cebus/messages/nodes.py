# -*- coding: utf-8 -*-
'''
    Cebus nodes models and messages
'''

# This file is part of cebus.

# Distributed under the terms of the last AGPL License. 
# The full license is in the file LICENCE, distributed as part of this software.

__author__ = 'Jean Chassoul'


# Remember Gabo Naum.

from schematics import models
from schematics import types
from schematics.types import compound

from cebus.messages import Node



class Conturbernium(Node):
	'''
		Soldiers of a contubernium shared a tent, 
		and could be rewarded or punished together as a unit.
	'''
	centurion = types.URLType(default=False)
    decanus =  types.URLType(default=True)


class Treant(Node):
	'''
		Treants are sentient tree forts with monkey characteristics. 

		They are typically portrayed as protectors of the forests and
		antagonists to industrialization and despoiling of nature. 


		The tree itself is a species of willow, most likely a weeping willow.

		It appears to be completely hollow.

		The entire interior of the tree trunk is covered in boards.
	'''
	cebus = types.URLType(default=False)
	hawk = types.URLType(default=True)