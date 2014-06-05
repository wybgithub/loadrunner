'''
Created on Jun 3, 2014

@author: wyb
'''
from handles import *
from templates import *
from stack import *

class Product(Handlers):
    
    def handle(self, s):
        dict = self.analyze(s)
        template = ProductTemplate(dict)
        return template
        pass
    
class ScenarioGeneralConfig(Handlers):

    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioGeneralConfigTemplate(dict)
        return template
        pass
        
class ScenarioPrivateConfig(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioPrivateConfigTemplate(dict)
        return template
        pass
    
class ScenarioCommonConfig(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioCommonConfigTemplate(dict)
        return template
        pass
    
class ScenarioIniFlags(Handlers):
    
    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioIniFlagsTemplate(dict)
        return template
        pass
    
class TestChief(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = TestChiefTemplate(dict)
        return template
        pass
    
class OnlineMonitor(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = OnlineMonitorTemplate(dict)
        return template
        pass
    
class LRExtensions(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = LRExtensionsTemplate(dict)
        return template
        pass
    
class ScenarioDiagnostics(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioDiagnosticsTemplate(dict)
        return template
        pass
    
class ScenarioAlertsConfig(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioAlertsConfigTemplate(dict)
        return template
        pass
    
class ScenarioSchedulerConfig(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioSchedulerConfigTemplate(dict)
        return template
        pass
    
class ScenarioGroupsData(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioGroupsDataTemplate(dict)
        return template
        pass
    
class ScenarioSLAConfig(Handlers):
    def handle(self, s):
        dict = self.analyze(s)
        template = ScenarioSLAConfigTemplate(dict)
        return template
        pass