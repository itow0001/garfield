'''
Created on Feb 16, 2015

@author: ian
'''

class job:
    '''This defines a job
    '''
    def __init__(self,name):
        self.name = name
        self.path = ""
        self.url  = ""
        self.parameters    = []
        self.pre_builders  = []
        self.builders      = []
        self.post_builders = []
        
    def get_name(self):
        return self.name
    
    def get_path(self):
        return self.path

        