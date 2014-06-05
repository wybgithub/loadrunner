'''
Created on Jun 4, 2014

@author: wyb
'''
from templates import *

class HostChiefTemplate(Template):
    
    subTemplates = []
    
    hostNames = []
    
    def __init__(self, subTemplates):
        self.subTemplates = subTemplates
        
    def handle(self, s):
        #print s
        pass
    
class SingleHostTemplate(Template):
     
    def handle(self, s):
        #print s
        pass