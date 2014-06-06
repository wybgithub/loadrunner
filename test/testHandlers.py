'''
Created on Jun 6, 2014

@author: wyb
'''
from core.blockSpliter import *
from core.handlers import *

def main():
    bs = BlockSpliter()
    bs.splitParaSeg()
    allBlocks = bs.getAllBlocks()
    
    handles = Handlers()
    for block in allBlocks:
        dict = handles.analyze(block)
        print dict["templateName"]
        
if __name__ == '__main__':
    main()
    pass