'''
Created on Jun 4, 2014

@author: wyb
'''
from handlers import *
from templates import *
from stack import *
from hostTemplates import *

class HostChief(Handlers):
    
    subTemplates = []
    hostNames = []
    
    def analyze(self, s):
        print "analyze"
        m = 0
        dict = {}
        s = s.strip()
        lines = s.split("\n")
        start = ""
        st = Stack()
        for i in range(0, len(lines)):
            line = lines[i]
            if start != "":
                start += line + "\n"
                if "{" in line:
                    st.push("{")
                elif "}" in line:
                    st.pop()
                    if st.isEmpty():
                        m+=1
                        start = start.strip()
                        sublines = start.split("\r\n")
                        for j in range(len(sublines)):
                            if "=" in sublines[j]:
                                kv = sublines[j].split("=")
                                dict[kv[0].strip()]=kv[1].strip()
                        self.subTemplates.append(SingleHostTemplate(dict))       
                        start = ""
                        dict = {}
                else:
                    continue  
            if (("{" in lines[i]) and (i != 0)):
                start = line
                st.push("{")  
    
    def handle(self, s):
        dict = self.analyze(s)
        template = HostChiefTemplate(self.subTemplates)
        return template
                        
        pass