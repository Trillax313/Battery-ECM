import model


class BatteryActions():
    def __init__(self, battery):
        self.battery = battery

    def cc_time(self, i, dt, duration_s):
        for _ in range(int(duration_s/dt)):
            results = self.battery.step(i, dt)
        return results
    
    def cc_SOC(self,i,dt,targetSOC):
        if i>0:
            while self.battery.curr_SOC > targetSOC:
                results = self.battery.step(i, dt)
        else: 
            while self.battery.curr_SOC < targetSOC:
                results = self.battery.step(i, dt)
        return results
    
    def rest(self, duration_s, dt):
        for _ in range(int(duration_s/dt)):
            results = self.battery.step(0,dt)
        return results
    