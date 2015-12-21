#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21 déc. 2015

@author: druzy
'''

class Version(list):
    '''
    Represente a Version of module
    '''
    

    def __init__(self, version="1"):
        '''
        Construct this object
    
        -version : a int or a string
        '''
        if isinstance(version, int):
            self.__init__(str(version))
        
        else:
            list.__init__(self,version.split("."))
            
        
            
    def __repr__(self):
        ret=""
        for tmp in self:
            ret += tmp + "."
        
        return ret[:-1]
        
            
if __name__=="__main__":
    ver=Version(5)
    print(ver)