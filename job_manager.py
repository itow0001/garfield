'''
Created on Feb 16, 2015

@author: ian
'''
import job
from jobs.job_storage import storage_actions as storage


class job_manager(object):
    '''
    Holds all the jobs
    '''
    def __init__(self):
        ''' Manages all jobs
        '''
        print "Job Manager Instance Running"
        self.jobs = []
    
    def create_job(self,name):
        new_job = job.job(name)
        store = storage(new_job)
        store.create()
        self.jobs.append(new_job)
        
    def refresh_jobs(self):
        pass
        
    def get_jobs_list(self):
        return self.jobs
    
    def get_job(self,name):
        for job in self.jobs:
            if job.name == name:
                return job
        return None
            
    def remove_job(self,name):
        found_job = self.get_job(name)
        if found_job != None:
            self.jobs.remove(found_job)
            store = storage(found_job)
            store.remove()
        return None
        
        
        
        
        
        