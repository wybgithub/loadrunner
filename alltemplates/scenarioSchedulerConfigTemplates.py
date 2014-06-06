'''
Created on Jun 5, 2014

@author: wyb
'''
from templates import *
import xml.etree.cElementTree as ET

class ScenarioSchedulerConfigTemplate(Template):
    
    tree = ET.ElementTree()
    
    def __init__(self, tree):
        self.tree = tree
    
    def handle(self, s):
        #print s
        pass
