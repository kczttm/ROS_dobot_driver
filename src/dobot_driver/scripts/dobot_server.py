#!/usr/bin/env python3
import rospy
import time
from DobotSerialInterface import DobotSerialInterface
from dobot_driver.msg import joint_angles
from dobot_driver.srv import setpose

#sudo chmod 777 /dev/ttyACM0
# run line above in terminal before running this code

class CreateDobot:
    def __init__(self):
        self.port='/dev/ttyACM0'

        self.dobot_interface = DobotSerialInterface(self.port)
        self.dobot_interface.set_speed()
        self.dobot_interface.set_playback_config()
        #self.dobot_interface.send_absolute_angles(0,0,0,0)
        
        self.angles = joint_angles()
        self.req_q = [0,0,0,0]
        
        self.dirty = False  # Flag for service call
        
        # publish the current joints config q1 q2 q3
        self.angles_pub = rospy.Publisher('raw_angles',joint_angles,queue_size = 1)
        
        # service initialization
        self.pose_server = rospy.Service('set_raw_angles', setpose, self.pose_update)
        
        # set ROS timer for update
        self.w_interval = 0.1  # serial write interval
        self.r_interval = 0.05 # serial read interval
        rospy.Timer(rospy.Duration(self.w_interval), self.dobot_update)
        
        
    def read_angles(self):
    	return self.dobot_interface.current_status.angles
    	
    def pose_update(self,req):
    	self.req_q = [req.q1,req.q2,req.q3,req.q4]
    	self.dirty = True
    	return 1
    	
    def dobot_update(self, timer):
    	if not self.dirty:
    	    return
    	q = self.req_q
    	self.dobot_interface.send_absolute_angles(q[0],q[1],q[2],q[3])
    	self.dirty = False



if __name__ == '__main__':
    try:
        rospy.init_node('dobot_server_main', anonymous = True) 
        bot = CreateDobot()
        while not rospy.is_shutdown():
            bot.angles = bot.read_angles()
            bot.angles_pub.publish(bot.angles)
            time.sleep(bot.r_interval)  # read loop update
    except rospy.ROSInterruptException:
        pass
