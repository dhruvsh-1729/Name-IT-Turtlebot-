#!usr/bin/env python
import multiprocessing
import rospy
import math as m
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen,SetPenRequest,TeleportAbsolute,TeleportAbsoluteRequest,TeleportRelative,TeleportRelativeRequest,Spawn,SpawnRequest

def teleport_absolute_client1(x,y,theta):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleport=rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
        teleport(x,y,theta)
    except rospy.ServiceException as e:
        print("Service failed : %s"%e)

def pen_client_off1(r,g,b,width,off):
    rospy.wait_for_service('/turtle1/set_pen')
    try:
        pen_off=rospy.ServiceProxy('/turtle1/set_pen',SetPen)
        pen_off(r,g,b,width,off)
    except rospy.ServiceException as e:
        print("Service failed : %s"%e)

def pen_client_on1(r,g,b,width,on):
    rospy.wait_for_service('/turtle1/set_pen')
    try:
        pen_on=rospy.ServiceProxy('/turtle1/set_pen',SetPen)
        pen_on(r,g,b,width,on)
    except rospy.ServiceException as e:
        print("Service failed : %s"%e)

def spawn_turtle(x,y,theta,name):
    rospy.wait_for_service('/spawn')
    try:
        new_turtle=rospy.ServiceProxy('/spawn',Spawn)
        new_turtle(x,y,theta,name)
    except rospy.ServiceException as e:
        print("Service failed : %s"%e)        

def rotate1(total_angle,distance,speed):
    
    velocity_publisher=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    vel=Twist()

    omega=2*m.pi*60/360
    angle=2*m.pi*total_angle/360

    pen_client_off1(69,86,255,0,255)
    teleport_absolute_client1(1.0, 8.0, 0.0)
    pen_client_on1(255,255,255,10,0)

    vel.linear.x=0
    vel.linear.y=0
    vel.linear.z=0
    
    vel.angular.x=0
    vel.angular.y=0
    vel.angular.z=abs(omega)


    while not rospy.is_shutdown():

        current_angle=0
        t0=rospy.Time().now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        current_distance=0
        t0=rospy.Time.now().to_sec()
        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        vel.angular.z=-abs(omega)
        current_angle=0
        t0=rospy.Time().now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        vel.angular.z=-abs(2*omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance/4)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        current_angle=0
        t0=rospy.Time().now().to_sec()
        vel.angular.z=abs(omega)
        while(current_angle<1.5*angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        current_distance=0
        t0=rospy.Time.now().to_sec()
        while(current_distance<3*distance/4):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(3.0, 8.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.linear.x=abs(speed)
        vel.angular.z=abs(omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(4.5, 8.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.angular.z=abs(omega)

        current_angle=0
        t0=rospy.Time().now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        current_distance=0
        t0=rospy.Time.now().to_sec()
        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        vel.angular.z=-abs(omega)
        current_angle=0
        t0=rospy.Time().now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        vel.angular.z=-abs(2*omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance/4)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.angular.z=abs(omega)

        current_angle=0
        t0=rospy.Time().now().to_sec()

        while(current_angle<2.2*angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        vel.angular.z=-abs(2*omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance/4)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(6.5, 8.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.linear.x=abs(speed)
        vel.angular.z=abs(omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(1.0, 5.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.angular.z=abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<2*angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)/2
        vel.angular.z=abs(omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance/4)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)/2
        vel.angular.z=-abs(omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance/4)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(2.0, 3.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.angular.z=abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<(7*angle/9)):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        vel.angular.z=-abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<(15*angle/9)):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(3.5, 3.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.angular.z=abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        vel.angular.z=-abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)/2
        vel.angular.z=-abs(omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance/4)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(4.5, 3.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.angular.z=abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(5.0, 3.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.angular.z=abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        vel.angular.z=-abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance/2):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(5.0, 4.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance/4):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(5.0, 3.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance/2):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(6.5, 3.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.angular.z=abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        vel.angular.z=-abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<16*angle/9):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<1.2*distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        vel.angular.z=abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<16*angle/9):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)
        t0=rospy.Time.now().to_sec()
        current_distance=0

        while(current_distance<distance):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        velocity_publisher.publish(vel)

        pen_client_off1(69,86,255,0,255)
        teleport_absolute_client1(8.25, 5.0, 0.0)
        pen_client_on1(255,255,255,10,0)

        vel.angular.z=abs(omega)
        current_angle=0
        t0=rospy.Time.now().to_sec()

        while(current_angle<2*angle):
            t1=rospy.Time.now().to_sec()
            current_angle=abs((t1-t0)*vel.angular.z)
            velocity_publisher.publish(vel)
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)/2
        vel.angular.z=abs(omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance/4)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

        vel.linear.x=abs(speed)/2
        vel.angular.z=-abs(omega)

        current_distance=0
        t0=rospy.Time.now().to_sec()

        while(current_distance<(m.pi*distance/4)):
            t1=rospy.Time.now().to_sec()
            current_distance=abs((t1-t0)*vel.linear.x)
            velocity_publisher.publish(vel)
        vel.linear.x=0
        vel.angular.z=0
        velocity_publisher.publish(vel)

if _name=="main_":
    rospy.init_node("my_client_node")
    rate = rospy.Rate(10)
    # spawn_turtle(10.0,1.0,0.0,'turtle2')

    # p1=multiprocessing.Process(target=rotate1,args=(90,2,1,))
    # p2=multiprocessing.Process(target=rotate2,args=(90,2,1,))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    rotate1(90,2,1)

    print("Completed!")
    


 
    while not rospy.is_shutdown():
        rate.sleep()