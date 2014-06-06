'''
Created on Jun 5, 2014

@author: wyb
'''
from templates import *


class TestChiefTemplate(Template):
    
    prefix = "{HostChief"
    
    subTemplates = []
    
    hostNames = []
    
    def __init__(self, subTemplates):
        self.subTemplates = subTemplates
        
    def handle(self, s):
        #print s
        pass
    
class SingleTestChiefTemplate(Template):
     
    def handle(self, s):
        #print s
        pass