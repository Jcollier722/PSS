import read_simulation as read
import run_simulation as sim
import tkinter as tk
import write_results as wr
import os
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
BG = '#b4cffa'

class GUI(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.input = None
        self.output = None
        
        #title
        title = tk.Label(root,text='CPU Scheduler', font='arial 25 bold underline',bg=BG).place(relx=0.25,rely=0.05)

        #input prompt
        input_prompt = tk.Label(root,text='Select input file:',font='arial 15 bold',bg=BG).place(relx=0.02,rely=0.25)

        #input field and text var
        self.input_var = tk.StringVar()
        input_field = tk.Entry(root,width=30,textvariable=self.input_var).place(relx=0.38,rely=0.26)

        #input button
        input_button = tk.Button(root,text='Browse',command=self.get_input).place(relx=0.76,rely=0.25)

        #output prompt
        output_prompt = tk.Label(root,text='Select output file:',font='arial 15 bold',bg=BG).place(relx=0.02,rely=0.35)
        
        #output field and var
        self.output_var = tk.StringVar()
        output_field = tk.Entry(root,width=30,textvariable=self.output_var).place(relx=0.38,rely=0.36)

        #output button
        output_button = tk.Button(root,text='Browse',command=self.get_output).place(relx=0.76,rely=0.36)

        #submit subtton
        submit_button = tk.Button(root,text='Submit',height=3,width=35,bg='#d9fcec',command=self.run_simulation).place(relx=0.25,rely=0.55)

    def get_input(self):
        self.input = askopenfile(filetypes =[('Spreadsheet', '*.xlsx')])
        self.input_var.set(self.input.name)
        messagebox.showinfo('Success','File loaded')

    def get_output(self):
        files = [('Word', '*.docx')]
        self.output = asksaveasfile(filetypes = files,defaultextension=files)
        self.output_var.set(self.output.name)
        messagebox.showinfo('Success','Save location entered')
        
    def run_simulation(self):

        #get list of job from user
        job_list = read.read_spreadsheet(self.input.name)

        sjn = sim.sjn(job_list)
        fcfs = sim.fcfs(job_list)
        srt= sim.srt(job_list)
        rr= sim.round_robin(job_list)
        
        wr.export(self.output.name,sjn,fcfs,srt,rr)
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Page Removal Simulator")
    root.resizable(width=False, height=False)
    root.geometry('500x300')
    root.config(bg=BG)
    my_gui = GUI(root)
    root.mainloop()
    
    """
    job_list = read.read_spreadsheet('simulation.xlsx')
    
    sjn = sim.sjn(job_list)
    print("Wait: " + str(sjn[2]) + "  Turn: " + str(sjn[1]))

    fcfs = sim.fcfs(job_list)
    print("Turn: " + str(fcfs[1]) + "  Wait: " + str(fcfs[2]))
    
    srt= sim.srt(job_list)
    print("Turn: " + str(srt[1]) + "  Wait: " + str(srt[2]))
    
    rr= sim.round_robin(job_list)
    print("Turn: " + str(rr[1]) + "  Wait: " + str(rr[2]))
    
    """
  


