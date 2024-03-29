# -*- coding: utf-8 -*-
'''
    Cebus AI computing legionary clouds.
'''

# This file is part of cebus.
#
# Distributed under the terms of the last AGPL License. The full
# license is in the file LICENCE, distributed as part of this
# software.

# Chinese analogies: Cangjie search for the Pixiu.

# Welcome to the central execution background unit system bus 
# unix supervisor; central artificial intelligence actor system.
# or cebus for short, this software have a funny name, don't you think?
# it sounds all like nonsense but have strong powerful magics!
# lets see what this is all about.

# mango: Manage Asynchronous Number of General ORGs

# Organizations of Roman Generality (ORGs)

# -- A Cohort is the basic tactical ORG system.

# A computing cohort have the power of 480 cores; a cohort consist of
# six centurias of 80 units used to follow campaigns with defined goals 
# and strategies to achive those goals using strategies and analogies.

# cores can also be virtual cpu's or cloud computing units.
# cebus works with a default set of 10 cohorts maximum per cloud legion.


# -- Strategy and tactics

# 0 Setting a goal
# 1 Strategy for achieving a goal
# 2 Analogy

# autonomous units that can be cloned, distributed and replaced at will.

# require systems to manage their own configuration, healing, 
# provisioning and migration dont make slaves out of humans
# if he can't fix by it self you can't fix it.

# ORG Organization of Restricted Generality.
# ------------------------------------------
# 
# ORG Organization of Restricted Generality. 
# ORGs are computer organizations but people are integral to their operation.

# goals and computational processing are followed and executed 
# by the abstract figure of a minion.

__author__ = 'Jean Chassoul'


import os
import tornado.ioloop

from tornado import gen
from tornado import web

# import systemd

from cebus.handlers import HomeHandler

from cebus.handlers import analogies
from cebus.handlers import applications
from cebus.handlers import campaigns
from cebus.handlers import clouds
from cebus.handlers import clusters
from cebus.handlers import cohorts
from cebus.handlers import daemons
from cebus.handlers import goals
from cebus.handlers import machines
from cebus.handlers import minions
from cebus.handlers import nodes
from cebus.handlers import strategies
from cebus.handlers import structures

from cebus.tools import options

import logging

import arrow

import zmq

import salt

import salt.config

import salt.client


# fun testing box
fun = []

# e_tag
e_tag = False

# salt master centurion.
master_opts = salt.config.master_config(
    os.environ.get('SALT_MASTER_CONFIG', './salt/master')
)

local = salt.client.LocalClient()

# more on peer-to-peer communicatin
# http://en.wikipedia.org/wiki/Bencode


if __name__ == '__main__':
    '''
        Cebus cloud AI supervisor
    '''
    options = options.options()
    base_url = options.base_url

    application = tornado.web.Application([

        # cebus
        (r'/', HomeHandler),

        # analogies
        #(r'/analogies/(?P<analogy_uuid>.+)/?', analogies.Handler),
        #(r'/analogies/?', analogies.Handler),

        # applications
        (r'/applications/(?P<app_uuid>.+)/?', applications.Handler),
        (r'/applications/?', applications.Handler),

        # campaigns
        #(r'/campaigns/(?P<campaing_uuid>.+)/?', campaigns.Handler),
        #(r'/campaigns/?', campaigns.Handler),

        # clouds
        (r'/clouds/(?P<cloud_uuid>.+)/?', clouds.Handler),
        (r'/clouds/?', clouds.Handler),

        # daemons
        #(r'/daemons/(?P<daemon_uuid>.+)/?', daemons.Handler),
        #(r'/daemons/?', daemons.Handler),

        # goals
        #(r'/goals/(?P<goal_uuid>.+)/?', goals.Handler),
        #(r'/goals/?', goals.Handler),

        # minions
        (r'/minions/(?P<minion_uuid>.+)/?', minions.Handler),
        (r'/minions/?', minions.Handler),

        # structures
        #(r'/structures/(?P<structure_uuid>.+)/?', structures.Handler),
        #(r'/structures/?', structures.Handler)

        # strategies
        #(r'/strategies/(?P<strat_uuid>.+)/?', strategies.Handler),
        #(r'/strategies/?', strategies.Handler)

        ],

        # pagination page_size
        page_size=options.page_size
    )

    application.listen(options.port)
    logging.info('Listening on http://%s:%s' % (options.host, options.port))
    tornado.ioloop.IOLoop.instance().start()

    '''

        If we believe in data structures, we must believe in independent (hence simultaneous) processing. 

        For why else would we collect items within a structure? 

        Why do we tolerate languages that give us the one without the other?

    '''