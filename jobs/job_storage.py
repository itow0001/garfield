'''
Created on Feb 16, 2015

@author: ian
'''
import os
import cPickle as pickle
import shutil

class storage_actions(object):
    '''Store a job for later use
    '''
    def __init__(self,job):
        '''
        Handles persistent job info
        '''
        self.job = job
        self.path = os.path.dirname(__file__)
        self.job_dir = os.path.join(self.path, self.job.name)
        print "job_storage"
        print self.path
        
    def create(self):
        """ Directory level creation of a job
        """
        #create directory 
        if not os.path.exists(self.job_dir):
            os.makedirs(self.job_dir)
        else:
            print "Directory Exists ignoring action"
        #Store object  
        pickle_file = os.path.join(self.job_dir, self.job.name)
        with open(pickle_file, 'wb') as handle:
            pickle.dump(self.job, handle)
          
    def remove(self):
        """ Remove job directory
        """
        for dir in os.listdir(self.path):
            if ".py" in dir:
                pass
            elif self.job.name == dir:
                shutil.rmtree(self.job_dir)
            else:
                print dir
        
            
            
    
        
        