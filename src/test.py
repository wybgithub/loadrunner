'''
Created on Jun 3, 2014

@author: wyb
'''
from blockSpliter import BlockSpliter
from setTemplates import *

def main():
    a = ["Product", "ScenarioGeneralConfig", "ScenarioPrivateConfig", "ScenarioCommonConfig", "ScenarioIniFlags", "HostChief", "TestChief", "OnlineMonitor", "LRExtensions", "ScenarioDiagnostics", "ScenarioAlertsConfig", "ScenarioSchedulerConfig", "ScenarioGroupsData", "ScenarioSLAConfig"]
    templates = []
    bs = BlockSpliter()
    bs.splitParaSeg()
    templates = bs.getTemplates()
    
    templatesSetter = TemplatesSetter(templates)
    templatesSetter.setPath()
    templates = templatesSetter.getTemplates()
    
    #sessionFileConstroctor = SessionFileConstroctor()
    #sessionFileConstroctor.constroct()
    
    
    
if __name__ == '__main__':
    main()
    
    