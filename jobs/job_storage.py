'''
Created on Feb 16, 2015

@author: ian
'''
import os
import cPickle as pickle
import shutil

class storage(object):
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
        self.save() 

    def save(self):
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
                
    def jobs_list(self):
        """ List of all job paths
        """
        jobs = []
        for dir in os.listdir(self.path):
            if ".py" in dir:
                pass
            else:
                jobs.append(dir)
        return jobs

class restore(object):
    """ handles stored jobs
    """
    def __init__(self):
        self.path = os.path.dirname(__file__)
    
    def jobs_path_list(self):
        """ List of all job paths
        """
        jobs = []
        for dir in os.listdir(self.path):
            if ".py" in dir:
                pass
            else:
                
                jobs.append(dir)
        return jobs
    
    def get_job(self,name):
        jobs_list = self.jobs_path_list()
        for job in jobs_list:
            if name in job:
                pickle_file = os.path.join(self.path,name,name)
                if os.path.exists(pickle_file):
                    with open(pickle_file, 'rb') as handle:
                        jb = pickle.load(handle)
                        return jb
        return None
    
    def get_jobs(self):
        jobs = []
        jobs_list = self.jobs_path_list()
        for job in jobs_list:
            pickle_file = os.path.join(self.path,job,job)
            #print pickle_file
            if os.path.exists(pickle_file):
                with open(pickle_file, 'rb') as handle:
                    jb = pickle.load(handle)
                    jobs.append(jb)
            else:
                print "file "+pickle_file+" does not exist"
                   
        return jobs
            
        
                        
                
        
        
    
                
                
                
                
            
            
        
        
            
            
    
        
        