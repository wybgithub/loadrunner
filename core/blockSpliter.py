import os
from interfaces.handlers import *
from implementations.handlersImpl import *
from implementations.hostChiefImpl import *
from core.stack import *
from alltemplates.templates import *

class BlockSpliter:
    
    templateFile = "../sessionFolder/Scenario1.lrs"
    
    allBlocks = []
    
    handles = Handlers()
    
    templates = []
    
    def getAllBlocks(self):
        return self.allBlocks
    
    def splitParaSeg(self):
        st = Stack()
        
        fh = open(self.templateFile)
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
                        self.allBlocks.append(start)
                        start = ""
                else:
                    continue  
            for i in range(len(self.handles.getHandlerTypes())):
                flag = "{" + self.handles.getHandlerTypes()[i]
                if flag in line:
                    start = line
                    st.push("{")          
                    break              
        
        fh.close()
        
    def callHandlers(self):
        for i in range(len(self.allBlocks)):
            process = globals()[self.handles.getHandlerTypes()[i]]()
            template = process.handle(self.allBlocks[i])
            self.templates.append(template)
    


