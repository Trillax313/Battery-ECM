import actions
import model

battery = model.BatteryECM(model.params)

action = actions.BatteryActions(battery)

Vrc,SOC,V = action.cc_time(5,1,100)

print(action.cc_SOC(1,1,0.9))

