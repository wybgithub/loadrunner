'''
Created on Jun 3, 2014

@author: wyb
'''


class Handlers:
    
    a = ["Product", "ScenarioGeneralConfig", "ScenarioPrivateConfig", "ScenarioCommonConfig", "ScenarioIniFlags", "HostChief", "TestChief", "OnlineMonitor", "LRExtensions", "ScenarioDiagnostics", "ScenarioAlertsConfig", "ScenarioSchedulerConfig", "ScenarioGroupsData", "ScenarioSLAConfig"]

    functionsList = []
    
    dict = {}
    
    def getHandlerTypes(self):
        return self.a
    
    def handle(self, s):
        pass
    
    def analyze(self, s):
        firstTime = True
        lines = s.split("\n")
        for line in lines:
            if (("{" in line) and (firstTime == True)):
                index = line.find("{")
                dict["templateName"] = line[index:].strip()
                firstTime = False
            if "=" in line:
                kv = line.split("=")
                self.dict[kv[0].strip()]=kv[1].strip()
        return self.dict
        pass

    
