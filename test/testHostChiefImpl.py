'''
Created on Jun 5, 2014

@author: wyb
'''
from core.handlers import *
from core.handlersImpl import *
from core.hostChiefImpl import *
from core.stack import *
from core.templates import *

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
    #for i in range(len(allBlocks)):
    process = globals()["HostChief"]()
    print process
    template = process.handle(allBlocks[5])
    print template
    for singletemplate in template.subTemplates:
        line = ""
        suffix = ""
        for (k, v) in singletemplate.dict.items():
            if "{" in k:
                suffix += k + "=" + v + "\n"
            else:
                line += k + "=" + v + "\n"
        line += "}"
        line = suffix + line
        print line
    fh.close()
    
if __name__ == '__main__':
    main()
    pass