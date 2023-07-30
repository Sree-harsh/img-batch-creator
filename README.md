# ROS Image Saver Package

The ROS Image Saver package is a ROS node that allows you to save images in batches of required sizes by subscribing to a specific ROS topic containing image messages. This package is useful in scenarios where you need to capture and store a large number of images with limited disk space or for organizing images into batches for further processing.

## Prerequisites
Before using this package, you need to have the following installed:
ROS (Robot Operating System) - Tested with ROS noetic in Ubuntu 20.04 .
Python 3.x
OpenCV Python package

## Installation
Clone the repository into your catkin workspace:
```Shell
  cd ~/catkin_ws/src
  git clone https://github.com/Sree-harsh/img-batch-creator.git
```
Build the package:
```Shell
  cd ~/catkin_ws
  catkin build
```
## Usage
Before using rosrun make sure the python file is converted into an executable
```Shell
  rosrun img-batch-creator img_saver.py
```

Make sure to replace the topic name with the actual ROS topic from which you want to subscribe to the images.
Make sure to change the path to the directory as per your local system.

1.The node will start listening to the specified image topic. Whenever a new image message is received, it will save the image to a folder in batches of required sizes. Each batch folder will contain a maximum of 30 images (default).

2.The images are saved in the following format: images/batchX/image_Y.jpg, where X is the batch number, and Y is the image number within the batch.

## Configuration
You can configure the batch size.

imgs_in_batch: Maximum number of images to save in each batch (default is 30) .

