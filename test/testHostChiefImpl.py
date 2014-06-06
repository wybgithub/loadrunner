'''
Created on Jun 5, 2014

@author: wyb
'''
from interfaces.handlers import *
from implementations.handlersImpl import *
from implementations.hostChiefImpl import *
from core.stack import *
from core.blockSpliter import *
from alltemplates.templates import *

def main():
    bs = BlockSpliter()
    bs.splitParaSeg()
    allBlocks = bs.getAllBlocks()
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