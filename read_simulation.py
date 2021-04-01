"""This file turns a spreadsheet into a pandas df and creates job objects """
import pandas as pd

class job:
    def __init__(self,name,arrival,cycle,finish=None,turn=None,wait=None):
        self.name = name
        self.arrival=arrival
        self.cycle=cycle
        self.finish = finish
        self.turn=turn
        self.wait=wait

def read_spreadsheet(path):
    job_list = []
    data_frame = pd.read_excel(path)
    
    for row in data_frame.iterrows():
        job_list.append(job((row[1]['Job']),
                            (row[1]['Arrival Times']),
                            (row[1]['CPU Cycle'])))

    return job_list
        

    
   

    
