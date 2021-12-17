#!/usr/bin/env python3
import rospy
import time
from DobotSerialInterface import DobotSerialInterface
from dobot_driver.srv import setpose

#sudo chmod 777 /dev/ttyACM0
# run line above in terminal before running this code

class DobotControl:
    def __init__(self):
        self.port='/dev/ttyACM0'

        self.dobot_interface = DobotSerialInterface(self.port)
        self.dobot_interface.set_speed()
        self.dobot_interface.set_playback_config()
        #self.dobot_interface.send_absolute_angles(0,0,0,0)
        
        self.pose_server = rospy.Service('set_raw_angles', setpose, self.set_pose)

    def set_pose(self,req):
        self.dobot_interface.send_absolute_angles(req.q1,req.q2,req.q3,0)
        # 35 degree is the max command, however,anything bigger can be sent from a quick second 		# command
        return 1


if __name__ == '__main__':
    try:
        rospy.init_node('dobot_service', anonymous = True)
        bot = DobotControl()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
