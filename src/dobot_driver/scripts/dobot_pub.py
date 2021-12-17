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
        self.port='/dev/ttyACM1'

        self.dobot_interface = DobotSerialInterface(self.port)
        self.dobot_interface.set_speed()
        self.dobot_interface.set_playback_config()
        #self.dobot_interface.send_absolute_angles(0,0,0,0)
        
        
        
    def angle_pub(self):
        # publish the current joints config q1 q2 q3
        self.raw_angles = rospy.Publisher('raw_angles',joint_angles,queue_size = 1)
        rospy.init_node('dobot_pub',anonymous = True)
        
        rate = rospy.Rate(10)  # 10 Hz 
        while not rospy.is_shutdown():
            readangles=self.dobot_interface.current_status.angles
            rospy.loginfo(readangles)
            self.raw_angles.publish(readangles)
            rate.sleep()# run line above in terminal before running this code



if __name__ == '__main__':
    try:
        bot = dobot()
        bot.angle_pub()
    except rospy.ROSInterruptException:
        pass
