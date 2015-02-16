'''
Created on Feb 16, 2015

@author: ian
'''
import job_manager
import job

if __name__ == '__main__':
    job_mng = job_manager.job_manager()
    
    # this is a list of jobs
    #for i in range(0,10):
    #    job_mng.create_job(str(i))
        
    #for job in job_mng.get_jobs_list():
    #    print job.name
        
    #job_mng.remove_job("0")
    
    #print "\n\n"
    #for job in job_mng.get_jobs_list():
    #    print job.name
        
    job_mng.restore_jobs()
        
    print "\n\n Currently stored"
    for job in job_mng.jobs:
        print job.name
        
        
    
    
        
    
    