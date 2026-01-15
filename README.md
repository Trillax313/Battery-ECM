# Battery-ECM
The Purpose of this Repo is to create an accurate ECM of a Li-ion battery that is able to model the battery with high percision. Alongside modelling I also want to be able to understand test profile and the insight that each test profile provides. This repo will have test profiles like:
  1. Hybrid Pulse Power Characterization (HPPC)
  2. Rate Power Capability (RPT)
  3. Rate Capacity Cabality (RCT)
  4. Static charge or discharge at specific C-Rate
  5. And many more


All the params for the battery itself including the Capacitor value, R0 which is the equivalent series resistance which models the instantaneous drop, R1 which is the charge transfer resistance/ overall polarization resistance, capacity in Coulombs. All these params can be easily found in the params.yaml file which gets read into the model.py file.

The model.py file holds all your voltage states and creates equations that model the Randles model with 1 RC pair. Each method/function in the class is pretty self explanatory from the names of the function. This is the model and the time stepper it pretty much simulates 1 time step and how the battery would respond according to the various inputs, but for now the only input the battery takes into account is the current whether that is charge or discharge, and dt which is the time step size. These 2 things influence how the battery will respond but there could be various other things; for example if you wanted to see how the battery reacts after many discharge or charge cycles without having to run/simulate the battery from scratch for SOH predicition. Temperature is also another factor that significantly impacts the battery's performance. Pressure which currently I have no information on but that would be for future iterations

The action.py file stores all possible scenarios of charge or discharge for example CC for a specific amount of time, CC to a specific SOC% threshold, Constant voltage to taper the current so the voltage stays at a specific voltage. These are possible action blocks the test could take. In future iterations there could be specific cutoffs/ termination methods. Where if a specific SOC, SOH, Temperature, Pressure, Voltage, Current, is reach to terminate the test similar to how actual battery tests are developed with these safety limits in mind. 

All the test will be developed individually where the action blocks are put together to perform a specific test profile. For example HPPC, is a matter of rest -> discharge -> rest -> charge -> discharge to next SOC step. RPT, RCT, and any other test can be made up of action blocks to make a test profile. Inspiration comes from the AVL block style test scripting.

Finally the logging simply takes the Current, Voltage, Time and SOC and logs them to the logs file where it automattically stores the test into a csv, with the date and time of test completion. That way if it automatically saves all tests without any rewrites and can still provide good insight into which test is which.

There are some example HPPC logs found in the logs folder in this repo.

I have many updates to work on and they will come very soon so stayed toon.

