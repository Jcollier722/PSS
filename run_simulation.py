"""This file runs the simulations"""
import copy


#******************* FCFS*******************#
"""Do the FCFS Simulation
Return a tuple where tuple[0] is the list and tuple[1] is the average turnaround
"""
def fcfs(job_list):
    #copy array so it can be re-used for other simulations
    this_list = copy.deepcopy(job_list)

    fcfs_get_finish(this_list)

    #turnaround time is simply finish time - arrival time
    #wait time is turnaround time - cycle time
    for job in this_list:
        job.turn = int(job.finish)-int(job.arrival)
        job.wait = int(job.turn) - int(job.cycle)


    #return list and stats
    return((this_list,get_avg_turn(this_list),get_avg_wait(this_list)))
   

"""Get the finish time of each job in a fcfs simulation"""
def fcfs_get_finish(job_list):
    finish_time = job_list[0].cycle

    #first job never waits in fcfs
    job_list[0].finish = finish_time
    job_list[0].wait = 0
    
    for job in job_list:
        if(job_list.index(job)!=0):
            finish_time = finish_time + job.cycle
            job.finish = finish_time
            
#******************SJN********************#
def sjn(job_list):
    
    #copy array so it can be re-used for other simulations
    this_list = copy.deepcopy(job_list)

    #initially, all jobs besdies the first are waiting
    waiting_q = this_list[1:]

    #first job will run to completion since sjn is non-prempetive
    finish_time = this_list[0].cycle
    this_list[0].finish = finish_time
    this_list[0].wait = 0

    #time for the rest of the jobs will start whenever the first job finishes
    time = int(this_list[0].finish)
    
    #while we still have jobs left
    while(len(waiting_q)!=0):
        """ Select the next job -> available at this time and minimum cycle """
        this_job = get_next_sjn(waiting_q,time)
        waiting_q.remove(this_job)
        this_job.finish = time + this_job.cycle

        #the chosen job will run to completion
        time = time + this_job.cycle

    #set the turnaround and wait times for each job
    for job in this_list:
        job.turn = int(job.finish) - int(job.arrival)
        job.wait = int(job.turn) - int(job.cycle)

    return((this_list,get_avg_turn(this_list),get_avg_wait(this_list)))


#******************SRT********************#
def srt(job_list):
    #take a copy
    this_list = copy.deepcopy(job_list)

    #init each job's remaining time to its cycle
    for t in this_list:
        t.time_left = t.cycle
    
    #unit of time
    time = 0

    #while there are still jobs with time remaining
    while(do_srt(this_list)):
        
        #running job is the job available at this time with the lowest cycle
        running_job = get_running(this_list,time)
        
        if(running_job is None):
            break
        else:
            running_job = this_list[this_list.index(running_job)]
            #print("Time: "+ str(time) + "  Running: "+ running_job.name)

        #if the running job will finish this cycle, set its finish value to time + 1
        if(running_job.time_left - 1 == 0):
            running_job.finish = time + 1
            running_job.time_left = 0

        #otherwise decrement time left and increment time stamp
        running_job.time_left = running_job.time_left - 1
        time = time + 1
    
    #set the turnaround and wait times for each job
    for job in this_list:
        job.turn = int(job.finish) - int(job.arrival)
        job.wait = int(job.turn) - int(job.cycle)

    return((this_list,get_avg_turn(this_list),get_avg_wait(this_list)))
        
        
  
"""
reference for average functions:
https://stackoverflow.com/questions/47779513/get-an-average-value-of-a-property-from-a-list-of-objects
"""
def get_avg_turn(job_list):
      return (sum([i.turn for i in job_list]) / len(job_list))

def get_avg_wait(job_list):
      return (sum([i.wait for i in job_list]) / len(job_list))
    
def sort_by_cycle(job_list):
    return (sorted(job_list, key=lambda x: x.cycle, reverse=False))

def sort_by_cycle_left(job_list):
    return (sorted(job_list, key=lambda x: x.time_left, reverse=False))

"""Get the first available job with shortest cycle time"""
def get_next_sjn(waiting,time):
    temp_wait = sort_by_cycle(waiting)
    for job in temp_wait:
        if(job.arrival <= time):
            return (job)

"""helper funciton to check if there are still jobs to process for srt """
def do_srt(job_list):
    for job in job_list:
        if(job.time_left != 0):
            return True
    return False

"""Get the job with the shortest cycle time available at this time"""    
def get_running(job_list,time):
    temp_list = sort_by_cycle_left(job_list)
    
    for job in temp_list:
        if(job.finish == None and job.arrival <= time):
            return job
            
    
