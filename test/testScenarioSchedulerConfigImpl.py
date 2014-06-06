'''
Created on Jun 5, 2014

@author: wyb
'''
from interfaces.handlers import *
from implementations.handlersImpl import *
from implementations.hostChiefImpl import *
from implementations.scenarioSchedulerConfigImpl import *
from core.stack import *
from alltemplates.templates import *
from core.blockSpliter import *

def main():
    templates = []
    templateFile = "../sessionFolder/Scenario1.lrs"
    
    allBlocks = []
    st = Stack()
    handlers = Handlers()
    fh = open(templateFile)
    lines = fh.readlines()
    start = ""
    for j in range(len(lines)):
        line = lines[j]
        if start != "":
            start += line
            if "{" in line:
                st.push("{")
            elif "}" in line:
                st.pop()
                if st.isEmpty():
                    allBlocks.append(start)
                    start = ""
            else:
                continue  
        for i in range(len(handlers.getHandlerTypes())):
            flag = "{" + handlers.getHandlerTypes()[i]
            if flag in line:
                start = line
                st.push("{")          
                break
    #for i in range(len(allBlocks)):
    #    print i
    #    print allBlocks[i]
        
    process = globals()["ScenarioSchedulerConfig"]()
    print process
    template = process.handle(allBlocks[11])
    print template
    fh.close()
    
def main2():
    bs = BlockSpliter()
    bs.splitParaSeg()
    allBlocks = bs.getAllBlocks()
    
    handles = ScenarioSchedulerConfig()
    handles.analyze(allBlocks[11])
    print handles.getDict()["templateName"]
    pass

if __name__ == '__main__':
    #main()
    main2()
    pass