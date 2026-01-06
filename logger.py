import pandas as pd
import datetime
import os

class Logger():
    def __init__(self):
        self.columns = [['Time', 'Current (A)', 'SOC', 'Vrc (V)', 'Terminal Voltage (V)']]
        self.data = []
        
    def csv_saver(self,name):
        curr_dt = datetime.datetime.now()
        formatted_dt = curr_dt.strftime("%m_%d_%Y-%H_%M_%S")
        self.final_name = name+ "-" + formatted_dt + '.csv'
        df = pd.DataFrame(self.data, columns= self.columns)
        filepath = os.path.join(r'C:\Users\Mohamed Ali\OneDrive - University of Windsor\Desktop\Battery-ECM\logs',self.final_name )
        df.to_csv(filepath, index=False)
        return df
    
    def appending_values(self, time, i, SOC, Vrc, V):
        self.data.append([time, i, SOC, Vrc, V])
        
    
        
        
        
        
    
    