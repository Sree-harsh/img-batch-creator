#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os

bridge = CvBridge()

count = 1
batch_count = 1
initial = True
imgs_in_batch = 30


def image_callback(msg):

    global count , batch_count , initial

    if initial == True: #First Batch
        #Insert your current working directory
        current_batch_folder = "/media/warlord/workspace/ros_ws/src/img_saver/src/scripts/images/"+"batch" + str(batch_count)
        os.makedirs(current_batch_folder)
        initial = False

    try:
        # Convert the ROS image message to OpenCV format
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        cv_image = cv2.resize(cv_image , (1280,720))
    except Exception as e:
        rospy.logerr("Failed to convert image: %s" % str(e))
        return


    image_filename = "image_" + str(count) + ".jpg"

    # print(batch_count)

    cv2.imwrite("/media/warlord/workspace/ros_ws/src/img_saver/src/scripts/images/batch" + str(batch_count)+"/"+image_filename, cv_image)
    count+=1
    if count > imgs_in_batch  :
        batch_count += 1
        current_batch_folder = "/media/warlord/workspace/ros_ws/src/img_saver/src/scripts/images/"+"batch" + str(batch_count)
        os.makedirs(current_batch_folder)
        count = 1

# Initialize the ROS node
rospy.init_node("image_saver")

# Create a subscriber to listen to the image topic
rospy.Subscriber("Enter topic name from where the images are to be subscribed", Image, image_callback)

# Spin the ROS node
rospy.spin()

# Clean up the OpenCV windows
cv2.destroyAllWindows()