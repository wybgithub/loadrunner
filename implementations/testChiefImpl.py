'''
Created on Jun 5, 2014

@author: wyb
'''
from interfaces.handlers import *
from alltemplates.templates import *
from core.stack import *
from alltemplates.testChiefTemplates import *

class TestChief(Handlers):
    
    subTemplates = []
    
    hostNames = []
    
    def analyze(self, s):
        firstTime = True
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
                        sublines = start.split("\n")
                        for j in range(len(sublines)):
                            if "=" in sublines[j]:
                                kv = sublines[j].split("=")
                                dict[kv[0].strip()]=kv[1].strip()
                        self.subTemplates.append(SingleTestChiefTemplate(dict))       
                        start = ""
                        dict = {}
                else:
                    continue  
            if (("{" in lines[i]) and (i != 0)):
                start = line
                st.push("{")
                if firstTime == True:
                    index = line.find("{")
                    self.dict["templateName"] = line[index:].strip()
                    firstTime = False  
    
    def handle(self, s):
        dict = self.analyze(s)
        template = TestChiefTemplate(self.subTemplates)
        return template
                        
        pass