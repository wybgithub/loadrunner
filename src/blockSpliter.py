import os
from handles import *
from handlersImpl import *
from stack import *
class BlockSpliter:
    templateFile = "./Scenario1.lrs"
    
    def split(self):
        allBlocks = []
        st = Stack()
        handles = Handlers()
        #print os.getcwd()
        fh = open(self.templateFile)
        lines = fh.readlines()
        start = ""
        for j in range(len(lines)):
            line = lines[j]
            if start != "":
                start += line
                #print line.strip()
                if "{" in line:
                    st.push("{")
                elif "}" in line:
                    st.pop()
                    if st.isEmpty():
                        allBlocks.append(start)
                        start = ""
                        #print line.strip()
                        #print "--------------"
                else:
                    continue
                
            for i in range(len(handles.getHandlerTypes())):
                #print "a " + str(i)
                #print handles.getHandlerTypes()
                flag = "{" + handles.getHandlerTypes()[i]
                if flag in line:
                    start = line
                    st.push("{")
                    #print "in"
                    #print line
                    process = globals()[handles.getHandlerTypes()[i]]()
                    process.handle()
                    #print line.strip()
                    break
            #print "end"
                
        for s in allBlocks:
            print s.strip()
            print "----------"
        fh.close()
        
    
    


