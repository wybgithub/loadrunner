import os
from handles import *
from handlersImpl import *
from hostChiefImpl import *
from stack import *
from templates import *

class BlockSpliter:
    templateFile = "./Scenario1.lrs"
    templates = []
    
    def splitParaSeg(self):
        allBlocks = []
        st = Stack()
        handles = Handlers()
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
                        allBlocks.append(start)
                        start = ""
                else:
                    continue  
            for i in range(len(handles.getHandlerTypes())):
                flag = "{" + handles.getHandlerTypes()[i]
                if flag in line:
                    start = line
                    st.push("{")          
                    break
                
        for i in range(len(allBlocks)):
            process = globals()[handles.getHandlerTypes()[i]]()
            template = process.handle(allBlocks[i])
            self.templates.append(template)
        fh.close()
        
    
    


