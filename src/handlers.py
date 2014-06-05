'''
Created on Jun 3, 2014

@author: wyb
'''


class Handlers:
    
    a = ["Product", "ScenarioGeneralConfig", "ScenarioPrivateConfig", "ScenarioCommonConfig", "ScenarioIniFlags", "HostChief", "TestChief", "OnlineMonitor", "LRExtensions", "ScenarioDiagnostics", "ScenarioAlertsConfig", "ScenarioSchedulerConfig", "ScenarioGroupsData", "ScenarioSLAConfig"]

    functionsList = []
    
    def getHandlerTypes(self):
        return self.a
    
    def handle(self, s):
        pass
    
    def analyze(self, s):
        dict = {}
        lines = s.split("\n")
        for line in lines:
            if "=" in line:
                kv = line.split("=")
                dict[kv[0].strip()]=kv[1].strip()
        return dict
        pass

    
