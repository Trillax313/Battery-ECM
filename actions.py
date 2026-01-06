import model
import logger



class BatteryActions():
    def __init__(self, battery, log):
        self.battery = battery
        self.log = log
        self.time = 0

    def cc_time(self, i, dt, duration_s):
        for _ in range(int(duration_s/dt)):
            results = self.battery.step(i, dt)
            self.log.appending_values(self.time, i, results[1],results[0], results[2])
            self.time += dt
        return results
    
    def cc_SOC(self,i,dt,targetSOC):
        if i>0:
            while self.battery.curr_SOC > targetSOC:
                results = self.battery.step(i, dt)
                self.log.appending_values(self.time, i, results[1],results[0], results[2])
                self.time += dt
        else: 
            while self.battery.curr_SOC < targetSOC:
                results = self.battery.step(i, dt)
                self.log.appending_values(self.time, i, results[1],results[0], results[2])
                self.time += dt
        return results
    
    def rest(self, duration_s, dt):
        for _ in range(int(duration_s/dt)):
            results = self.battery.step(0,dt)
            self.log.appending_values(self.time, 0, results[1],results[0], results[2])
            self.time += dt
            
        return results

