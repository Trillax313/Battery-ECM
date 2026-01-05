import yaml
import numpy as np
import pandas as pd

with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

SOC_OCV = pd.read_csv('~/Desktop/Battery/data/SOCOCV.csv') 
soc = np.array(SOC_OCV['SOC'])
ocv = np.array(SOC_OCV['OCV'])



class BatteryECM:
    def __init__(self,params):
        self.R0 = params['R0']
        self.R1= params['R1']
        self.C= params['C']
        self.Q= params['Q'] #coulobs (Ah * 3600) so in this the battery capacity is 3 Ah
        self.Vrc= params["Vrc"]
        self.curr_SOC= params["curr_SOC"]
        
    
    def step(self,i, dt):
        Vrc = self.update_Vrc(i,dt)
        curr_SOC = self.update_SOC(i,dt)
        V = self.update_V(i,dt)
        return Vrc, curr_SOC, V
    
    def update_Vrc(self,i,dt):
        dVrc = self.Vrc/(-1*self.R1*self.C) + (i/self.C)
        self.Vrc += dVrc * dt
        return self.Vrc
    
    def update_SOC(self,i,dt):
        coul = 1 if i > 0 else 0.9
        self.curr_SOC -= (i*dt*coul)/self.Q
        self.curr_SOC = np.clip(self.curr_SOC, 0, 1)
        return self.curr_SOC

    def update_V(self,i,dt):
        self.V = np.interp(self.curr_SOC,soc, ocv) - self.R0*i - self.Vrc
        return self.V
    


        
