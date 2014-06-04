'''
Created on Jun 3, 2014

@author: wyb
'''
from handles import *

class Product(Handlers):
    
    def handle(self):
        print self.a[0]
        pass
    
class ScenarioGeneralConfig(Handlers):

    def handle(self):
        print self.a[1]
        pass
        
class ScenarioPrivateConfig(Handlers):
    def handle(self):
        print self.a[2]
        pass
    
class ScenarioCommonConfig(Handlers):
    def handle(self):
        print self.a[3]
        pass
    
class ScenarioIniFlags(Handlers):
    def handle(self):
        print self.a[4]
        pass
    
class HostChief(Handlers):
    def handle(self):
        print self.a[5]
        pass
    
class TestChief(Handlers):
    def handle(self):
        print self.a[6]
        pass
    
class OnlineMonitor(Handlers):
    def handle(self):
        print self.a[7]
        pass
    
class LRExtensions(Handlers):
    def handle(self):
        print self.a[8]
        pass
    
class ScenarioDiagnostics(Handlers):
    def handle(self):
        print self.a[9]
        pass
    
class ScenarioAlertsConfig(Handlers):
    def handle(self):
        print self.a[10]
        pass
    
class ScenarioSchedulerConfig(Handlers):
    def handle(self):
        print self.a[11]
        pass
    
class ScenarioGroupsData(Handlers):
    def handle(self):
        print self.a[12]
        pass
    
class ScenarioSLAConfig(Handlers):
    def handle(self):
        print self.a[13]
        pass