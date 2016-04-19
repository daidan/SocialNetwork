# -*- coding: utf-8 -*-
'''
Created on 2016年4月19日

@author: daidan
'''
import sys
import os
from numpy import *
import networkx


g=networkx.Graph()
g.add_edge(1,2)
g.add_node("spam")
print g.nodes()
print g.edges()

