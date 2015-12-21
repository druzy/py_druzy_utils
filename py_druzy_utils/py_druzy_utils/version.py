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
            list.__init__(self,version.split())
            
            