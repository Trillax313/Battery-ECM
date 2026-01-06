import actions
import model
import logger
import matplotlib.pyplot as plt

log = logger.Logger()
battery = model.BatteryECM(model.params)
action = actions.BatteryActions(battery,log)



class HPPC():
    def __init__(self):
        self.dt = 1
        
    def run(self, battery, endSOC):
        
        while battery.curr_SOC > endSOC:
            targetSOC = round(battery.curr_SOC, 1) - 0.1
            action.rest(3600, self.dt)
            action.cc_time(1*battery.Q/3600, self.dt, 10)
            action.rest(600, self.dt)
            action.cc_time(0.75*battery.Q/3600, self.dt, 10)
            action.rest(600,self.dt)
            action.cc_SOC(1*battery.Q/3600, self.dt, targetSOC )
        
        df = log.csv_saver('HPPC')
        return (df)
    


Hppc= HPPC()
data = Hppc.run(battery, 0.1)



plt.plot(data['Time'], data['Terminal Voltage (V)'])
plt.show()



