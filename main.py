import read_simulation as read
import run_simulation as sim


if __name__ == "__main__":
    
    job_list = read.read_spreadsheet('simulation.xlsx')

    """
    fcfs = sim.fcfs(job_list)
    print("Turn: " + str(fcfs[1]) + "  Wait: " + str(fcfs[2]))
    sjn = sim.sjn(job_list)
    print("Turn: " + str(sjn[1]) + "  Wait: " + str(sjn[2]))
    srt= sim.srt(job_list)
    print("Turn: " + str(srt[1]) + "  Wait: " + str(srt[2]))
    """
   
