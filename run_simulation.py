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

    #take a copy
    this_list = copy.deepcopy(job_list)

    #first job does not wait, first job's finish time is just its cycle
    time_available = this_list[0].cycle
    this_list[0].finish = time_available
    this_list[0].wait = 0
    
    #initially every job besides the first is waiting
    waiting_q = this_list[1:]

    #while we still have processes to allocate
    while(len(waiting_q)!=0):
        #out of all the available jobs, pick the one with shortest cycle
        next_job = get_next_sjn(waiting_q,time_available)
        next_job = this_list[this_list.index(next_job)]
        
        #remove that job from the waiting
        waiting_q.remove(next_job)

        #set job's completion time
        next_job.finish = int(time_available) + int(next_job.cycle)

        #update the available time stamp
        time_available = int(time_available) + int(next_job.cycle)

    #set the turnaround and wait times for each job
    for job in this_list:
        job.turn = int(job.finish) - int(job.arrival)
        job.wait = int(job.turn) - int(job.cycle)

    return((this_list,get_avg_turn(this_list),get_avg_wait(this_list)))
        
"""
reference:
https://stackoverflow.com/questions/47779513/get-an-average-value-of-a-property-from-a-list-of-objects
"""
def get_avg_turn(job_list):
      return (sum([i.turn for i in job_list]) / len(job_list))

def get_avg_wait(job_list):
      return (sum([i.wait for i in job_list]) / len(job_list))
    
def sort_by_cycle(job_list):
    return (sorted(job_list, key=lambda x: x.cycle, reverse=False))

"""Get the first available job with shortest burst time"""
def get_next_sjn(waiting,time):
    temp_wait = sort_by_cycle(waiting)

    for job in temp_wait:
        if(job.arrival <= time):
            return (job)
    
