'''
Created on Feb 16, 2015

@author: ian
'''
import job
from jobs.job_storage import storage
from jobs.job_storage import restore


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
        """ create job instance and storage
        """
        new_job = job.job(name)
        store = storage(new_job)
        store.create()
        self.jobs.append(new_job)
        
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
    
    def restore_job(self,name):
        restr= restore()
        restr_job = restr.get_job(name)
        self.jobs.append(restr_job)
    
    def restore_jobs(self):
        restr= restore()
        jobs_list = restr.get_jobs()
        
        for job_store in jobs_list:
            if self.get_job(job_store.name) == None:
                self.jobs.append(job_store)
                
                
                    
        
        
        
        
        
        
        
        