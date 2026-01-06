import actions
import model

dt = 1

battery = model.BatteryECM(model.params)

action = actions.BatteryActions(battery)

class HPPC():
    def run(self, battery, endSOC):
        
        while battery.curr_SOC > endSOC:
            targetSOC = round(battery.curr_SOC, 1) - 0.1
            action.rest(3600, dt)
            action.cc_time(1*battery.Q/3600, dt, 10)
            action.rest(600, dt)
            action.cc_time(0.75*battery.Q/3600, dt, 10)
            action.rest(600,dt)
            action.cc_SOC(1*battery.Q/3600, dt, targetSOC )
        return (battery.curr_SOC)


results= HPPC()
print(results.run(battery, 0.5))


