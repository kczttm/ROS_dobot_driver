import time
from DoBot_FK import *
from DoBot_IK import *
from IK_Processing import *
from DobotSerialInterface import DobotSerialInterface
import numpy as np

#sudo chmod 777 /dev/ttyACM0
# run line above in terminal before running this code

port='/dev/ttyACM0'

dobot_interface = DobotSerialInterface(port)
dobot_interface.set_speed()
dobot_interface.set_playback_config()



time.sleep(0.1)
readangle=dobot_interface.current_status.angles
print(readangle)

xyzT = DoBot_FK([0,0,0,0])  
print(xyzT)
des_p0T = xyzT = DoBot_FK(np.deg2rad([-30,0,0,0]))  
time.sleep(1)
qsols = DoBot_IK(des_p0T)
q = IK_Processing(qsols)
print(q)
dobot_interface.send_absolute_angles(q)
for i in range(20):
    readangle=dobot_interface.current_status.angles
    readangle[3] = 0
    print(readangle)
    xyzT = DoBot_FK(np.deg2rad(readangle))
    #print(str(i) + 'th reading' + str(readangle))
    print(str(i) + 'th reading' + str(xyzT))
    print()
    time.sleep(0.05)

print(xyzT)
#time.sleep(3)
#time.sleep(0.1)
#readangle=dobot_interface.current_status.angles
#print(readangle)
#time.sleep(3)
#readangle=dobot_interface.current_status.angles
#print('angle ' + str(readangle))
#time.sleep(3)
#dobot_interface.send_absolute_angles(0,0,0,0)
#readangle=dobot_interface.current_status.angles
#print(readangle)
#time.sleep(3)
# for i in range(100):
#     dobot_interface.send_absolute_angles(30,0,0,0)
#     time.sleep(0.1)
#time.sleep(3)
#dobot_interface.send_absolute_angles(30,0,0,0)
#readangle=dobot_interface.current_status.angles
#print(readangle)
#time.sleep(3)
#dobot_interface.send_absolute_angles(0,20,20,0)
#readangle=dobot_interface.current_status.angles
#print(readangle)
#time.sleep(3)
dobot_interface.send_absolute_angles(0,0,0,0)
for i in range(10):
    readangle=dobot_interface.current_status.angles
    readangle[3] = 0
    xyzT = DoBot_FK(np.deg2rad(readangle)) 
    print(readangle)
    #print(str(i) + 'th reading' + str(readangle))
    print(str(i) + 'th reading' + str(xyzT))
    time.sleep(0.05)
    
time.sleep(3)
