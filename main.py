import read_simulation as read
import run_simulation as sim


if __name__ == "__main__":
    
    job_list = read.read_spreadsheet('simulation.xlsx')

    #fcfs = sim.fcfs(job_list)
    #sjn = sim.sjn(job_list)
    srt= sim.srt(job_list)
   


