'''
Created on Jun 3, 2014

@author: wyb
'''


class Handlers:
    
    a = ["Product", "ScenarioGeneralConfig", "ScenarioPrivateConfig", "ScenarioCommonConfig", "ScenarioIniFlags", "HostChief", "TestChief", "OnlineMonitor", "LRExtensions", "ScenarioDiagnostics", "ScenarioAlertsConfig", "ScenarioSchedulerConfig", "ScenarioGroupsData", "ScenarioSLAConfig"]


    #functions = [product, scenarioGeneralConfig, scenarioPrivateConfig, scenarioCommonConfig, scenarioIniFlags, hostChief, testChief, onlineMonitor, lRExtensions, scenarioDiagnostics, scenarioAlertsConfig, scenarioSchedulerConfig, scenarioGroupsData, scenarioSLAConfig]
    functionsList = []
    
    def getHandlerTypes(self):
        return self.a
        
    #def getHandlers(self):
    #    return self.functions
    
    
    
