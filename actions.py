import model




class BatteryActions():
    def __init__(self, battery):
        self.battery = battery

    def cc_time(self, i, dt, duration_s):
        for _ in range(duration_s):
            results = self.battery.step(i, dt)
        return results
    
    def cc_SOC(self,i,dt,targetSOC):
        direction = 1 if i > 0 else -1
        while direction * self.battery.curr_SOC > targetSOC:
            results = self.battery.step(i, dt)
        return results
    