'''
Created on Jun 4, 2014

@author: wyb
'''
'''
Created on Jun 3, 2014

@author: wyb
'''
from interfaces.handlers import *

class Template:
    
    templateName = ""
    dict = {}
    
    def __init__(self, dict):
        self.dict = dict

class ProductTemplate(Template):
    pass
    
class ScenarioGeneralConfigTemplate(Template):

    def handle(self, s):
        pass
        
class ScenarioPrivateConfigTemplate(Template):
    def handle(self, s):
        #print s
        pass
    
class ScenarioCommonConfigTemplate(Template):
    def handle(self, s):
        #print s
        pass
    
class ScenarioIniFlagsTemplate(Template):
    def handle(self, s):
        #print s
        pass
    
class OnlineMonitorTemplate(Template):
    def handle(self, s):
        #print s
        pass
    
class LRExtensionsTemplate(Template):
    def handle(self, s):
        #print s
        pass
    
class ScenarioDiagnosticsTemplate(Template):
    def handle(self, s):
        #print s
        pass
    
class ScenarioAlertsConfigTemplate(Template):
    def handle(self, s):
        #print s
        pass
    
class ScenarioGroupsDataTemplate(Template):
    def handle(self, s):
        #print s
        pass
    
class ScenarioSLAConfigTemplate(Template):
    def handle(self, s):
        #print s
        pass