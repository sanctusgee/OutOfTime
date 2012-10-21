'''
OUT OF TIME - Main Program
It does something
Code by Jacob Turner, released under the MIT license
'''

import time
import Tkinter as tk
from datetime import datetime, timedelta

group = "Group"
choices = ['1', '2', '3', '4','5', '6', '7', '8', '9', '10', '11', '12']

class TimerApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.running = False
        self.glabel = tk.Label(self, text=group, width=10)
        self.glabel.pack(side='left', padx=0, pady=0)
        self.var = tk.StringVar(self)
        self.var.set("1")
        self.option = tk.OptionMenu(self, self.var, *choices, command=self.settitle)
        self.option.pack(side='left', padx=0, pady=0)
        self.wm_title("OUT OF TIME - %s %s" % (group.upper(), self.var.get()))
        self.label = tk.Label(self, text="SET TIME")
        self.label.pack(padx=5, pady=5)
        self.hframe = tk.Frame(self)
        self.hframe.pack(side='left')
        self.hbutton = tk.Button(self.hframe, text="+1 hour", command=self.addhour)
        self.hbutton.pack(side='top', padx=5, pady=0)
        self.shbutton = tk.Button(self.hframe, text="-1 hour", command=self.subhour)
        self.shbutton.pack(side='bottom', padx=5, pady=0)
        self.hhframe = tk.Frame(self)
        self.hhframe.pack(side='left')
        self.hhbutton = tk.Button(self.hhframe, text="+30 min", command=self.addhalfhour)
        self.hhbutton.pack(side='top', padx=5, pady=0)
        self.shhbutton = tk.Button(self.hhframe, text="-30 min", command=self.subhalfhour)
        self.shhbutton.pack(side='bottom', padx=5, pady=0)
        self.qhframe = tk.Frame(self)
        self.qhframe.pack(side='left')
        self.qhbutton = tk.Button(self.qhframe, text="+15 min", command=self.addqtrhour)
        self.qhbutton.pack(side='top', padx=5, pady=0)
        self.sqhbutton = tk.Button(self.qhframe, text="-15 min", command=self.subqtrhour)
        self.sqhbutton.pack(side='bottom', padx=5, pady=0)
        self.minframe = tk.Frame(self)
        self.minframe.pack(side='left')
        self.minbutton = tk.Button(self.minframe, text="+1 min", command=self.addminute)
        self.minbutton.pack(side='top', padx=5, pady=0)
        self.sminbutton = tk.Button(self.minframe, text="-1 min", command=self.subminute)
        self.sminbutton.pack(side='bottom', padx=5, pady=0)
        self.tsecframe = tk.Frame(self)
        self.tsecframe.pack(side='left')
        self.tsecbutton = tk.Button(self.tsecframe, text="+30 sec", command=self.addtsec)
        self.tsecbutton.pack(side='top', padx=5, pady=0)
        self.stsecbutton = tk.Button(self.tsecframe, text="-30 sec", command=self.subtsec)
        self.stsecbutton.pack(side='bottom', padx=5, pady=0)
        self.fsecframe = tk.Frame(self)
        self.fsecframe.pack(side='left')
        self.fsecbutton = tk.Button(self.fsecframe, text="+15 sec", command=self.addfsec)
        self.fsecbutton.pack(side='top', padx=5, pady=0)
        self.sfsecbutton = tk.Button(self.fsecframe, text="-15 sec", command=self.subfsec)
        self.sfsecbutton.pack(side='bottom', padx=5, pady=0)
        self.secframe = tk.Frame(self)
        self.secframe.pack(side='left')
        self.secbutton = tk.Button(self.secframe, text="+1 sec", command=self.addsecond)
        self.secbutton.pack(side='top', padx=5, pady=0)
        self.ssecbutton = tk.Button(self.secframe, text="-1 sec", command=self.subsecond)
        self.ssecbutton.pack(side='bottom', padx=5, pady=0)
        self.optframe = tk.Frame(self)
        self.optframe.pack(side='left')
        self.ssbutton = tk.Button(self.optframe, text="Start/Stop", command=self.switch)
        self.ssbutton.pack(side='left', padx=5, pady=0)
        self.remaining = 0
        self.countdown(0)

    def switch(self):
        self.running = not(self.running)
        if self.running:
            self.activatebuttons()
            self.countdown(self.remaining)
        elif not self.running:
            self.disablebuttons()

    def countdown(self, remaining = None):
        self.update()
        if self.running:
            if remaining is not None:
                self.remaining = remaining
            if self.remaining < 0:
                self.label.configure(text="OUT OF TIME")
                self.disablebuttons()
            else:
                self.refreshtime()
                self.remaining -= 1
                self.after(1000, self.countdown)
        else:
            time.sleep(.1)
    
    def refreshtime(self):
        self.sec = timedelta(seconds=self.remaining)
        self.d = datetime(1,1,1) + self.sec
        self.label.configure(text="%d days, %d hours, %d minutes, %d seconds" % (self.d.day-1, self.d.hour, self.d.minute, self.d.second))

    def addhour(self):
        self.remaining += 3600
        self.refreshtime()

    def addhalfhour(self):
        self.remaining += 1800
        self.refreshtime()

    def addqtrhour(self):
        self.remaining += 900
        self.refreshtime()

    def addminute(self):
        self.remaining += 60
        self.refreshtime()

    def addtsec(self):
        self.remaining += 30
        self.refreshtime()

    def addfsec(self):
        self.remaining += 15
        self.refreshtime()

    def addsecond(self):
        self.remaining += 1
        self.refreshtime()

    def subhour(self):
        self.remaining -= 3600
        self.refreshtime()

    def subhalfhour(self):
        self.remaining -= 1800
        self.refreshtime()

    def subqtrhour(self):
        self.remaining -= 900
        self.refreshtime()

    def subminute(self):
        self.remaining -= 60
        self.refreshtime()

    def subtsec(self):
        self.remaining -= 30
        self.refreshtime()

    def subfsec(self):
        self.remaining -= 15
        self.refreshtime()

    def subsecond(self):
        self.remaining -= 1
        self.refreshtime()

    def settitle(self, groupnum):
        self.wm_title("OUT OF TIME - %s %s" % (group.upper(), self.var.get()))
    
    def activatebuttons(self):
        self.hbutton.config(state='active')
        self.hhbutton.config(state='active')
        self.qhbutton.config(state='active')
        self.minbutton.config(state='active')
        self.tsecbutton.config(state='active')
        self.fsecbutton.config(state='active')
        self.secbutton.config(state='active')
        self.shbutton.config(state='active')
        self.shhbutton.config(state='active')
        self.sqhbutton.config(state='active')
        self.sminbutton.config(state='active')
        self.stsecbutton.config(state='active')
        self.sfsecbutton.config(state='active')
        self.ssecbutton.config(state='active')

    def disablebuttons(self):
        self.hbutton.config(state='disabled')
        self.hhbutton.config(state='disabled')
        self.qhbutton.config(state='disabled')
        self.minbutton.config(state='disabled')
        self.tsecbutton.config(state='disabled')
        self.fsecbutton.config(state='disabled')
        self.secbutton.config(state='disabled')
        self.shbutton.config(state='disabled')
        self.shhbutton.config(state='disabled')
        self.sqhbutton.config(state='disabled')
        self.sminbutton.config(state='disabled')
        self.stsecbutton.config(state='disabled')
        self.sfsecbutton.config(state='disabled')
        self.ssecbutton.config(state='disabled')    
   
if __name__ == "__main__":
    app = TimerApp()
    app.mainloop()