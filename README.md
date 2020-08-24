# TEAM-4_UMIC
lane_detection.ipynb is a notebook containing the code for getting the side vectors of a road lane in a gazebo simulated environment.
link of colab notebook - https://colab.research.google.com/drive/1JH5EQa2AeeDN9zTCvS3e6a_PO6WBWPJE?usp=sharing (open to editing)

mechanical folder contains the structure related files for our autonomous robot.

https://github.com/osrf/citysim
clone this repo and replace the world folder by the one which I uploaded
I have removed unwanted stuff from original one

The scripts folder contains the python scripts for lane detection and arrow detection implemented in ROS/GAZEBO as nodes.

#########################################3
# src-aryan folder :
contains the integration of line-follower,arrow_detection,laser,and ball pick-up and pushing code.
to use this, follow the steps below:

1) create a new workspace
2) make an src folder
3) catkin_make this workspace
4) replace the src folder you created with src_aryan folder from this repository
5) go to the world file in the env folder and change paths from '/aryan/final_ws' to your computers path name.
6) to launch the bot in gazebo run :- roslaunch bot1 controls.launch, and press the play button below to run the simulation in gazebo
7) all the python codes are present in the scripts folder inside bot1 package
8) the important codes that you have to run for the bot to work are - arrow.py , ball_detection.py and image.py, in that order respectiviely in separate terminals
   using command rosrun bot1 <filename.py>
9) image.py contains the main code for line following and ball pickup/push , wherease arrow.py finds the direction of arrow and sends it to image .py through a topic, so that the bot turns in the specified direction when intersection occurs. ball_detection sends the color and centroid value of the nearest ball to image.py through a topic. so that image.py can make decision to pickup/push ball if red/green and ball following with help of centroid. 
10) note - if laser value <23cm bot will stop.
11) problems - ball_following does not work now, and sometimes the green ball gets hit by collision properties of bot and doesnt go inside
