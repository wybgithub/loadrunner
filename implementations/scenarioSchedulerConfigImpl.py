'''
Created on Jun 5, 2014

@author: wyb
'''
#-*- coding: UTF-8 -*-

from interfaces.handlers import *
from alltemplates.templates import *
from core.stack import *
import xml.etree.cElementTree as ET
#from elementtree.ElementTree import ElementTree as et
from alltemplates.scenarioSchedulerConfigTemplates import *

import io
import os
import sys
import codecs

class ScenarioSchedulerConfig(Handlers):
    
    xmlFile = "../sessionFolder/scenarioSchedulerConfig.xml"
    
    tree = ET.ElementTree()
    
    def getDict(self):
        return self.dict
    
    def analyze(self, s):
        firstTime = True
        m = 0
        s = s.strip()
        lines = s.split("\n")
        start = ""
        xmlStr = ""
        st = Stack()
        for i in range(0, len(lines)):
            line = lines[i]
            if start != "":
                if "utf-16" in line:
                    line = line.replace("utf-16","utf-8")
                xmlStr += line + "\n"
                if "{" in line:
                    st.push("{")
                elif "}" in line:
                    st.pop()
                    if st.isEmpty():
                        index = xmlStr.find('}')
                        if index >= 0:
                            xmlStr = xmlStr[0:index]
                            xmlStr = xmlStr + "\n"
                            
                        break
                else:
                    continue
            if ("{" in lines[i]):
                start = line
                st.push("{")
                if firstTime == True:
                    index = line.find("{")
                    self.dict["templateName"] = line[index:].strip()
                    firstTime = False
        return xmlStr
            
    def handle(self, s):
        xmlstr = self.analyze(s)
        xmlstr = xmlstr.decode("UTF-8")
        if os.path.exists(self.xmlFile):
            os.remove(self.xmlFile)
         
        fh = codecs.open(self.xmlFile, 'a', encoding='UTF-8')
        xmlstr = xmlstr.encode("UTF-8")
        fh.write(xmlstr)
        fh.flush()
        fh.close()
        try:
            self.tree = ET.ElementTree(file=self.xmlFile)
            template = ScenarioSchedulerConfigTemplate(self.tree)
            return template
#             for elem in tree.iter():
#                 if elem.tag == "CurrentSchedulerId":
#                     print elem.tag
#                     print elem.text
#                     elem.text = "2"
#                     print elem.text
#             fl = codecs.open("xml2.xml", 'a', encoding='UTF-8')
#             fl.write(" ")
#             fl.close()
#             tree.write("xm.xml")             
        except Exception, e:
            print e
            return -1
        
        #dict = self.analyze(s)
        #template = ScenarioSchedulerConfigTemplate(dict)
        #return template