# Inspired by: https://github.com/ros-teleop/teleop_twist_keyboard/blob/master/teleop_twist_keyboard.py

import geometry_msgs.msg
import rclpy

from pynput import keyboard

disp_msg = """
This node takes keypresses from the keyboard and publishes them on the 
cmd_vel topic as Twist messages. It works best with a US keyboard layout.
---------------------------
Moving around:
   q    w    e
   a    s    d
   z    x    c

w (move forwards)
q (turn anti-clockwise while moving forwards)
e (turn clockwise while moving forwards)
a (turn anti-clockwise)
s (stop)
d (turn clockwise)
x (move backwards)
z (turn clockwise while moving backwards)
c (turn anti-clockwise while moving backwards)

Speed change: 1 2 3 4

1 (Increase linear speed by 0.1 units)
2 (Decrease linear speed by 0.1 units)
3 (Increase angular speed by 0.1 units)
4 (Decrease angular speed by 0.1 units)

CTRL-C to quit
"""

velocity_toggle_bindings = {
    'q': (1, 0, 0, 1),
    'w': (1, 0, 0, 0),
    'e': (1, 0, 0, -1),
    'a': (0, 0, 0, 1),
    's': (0, 0, 0, 0),
    'd': (0, 0, 0, -1),
    'z': (-1, 0, 0, -1),
    'x': (-1, 0, 0, 0),
    'c': (-1, 0, 0, 1),
}

speed_change_bindings = {
    '1': (0.1, 0),
    '2': (-0.1, 0),
    '3': (0, 0.1),
    '4': (0, -0.1),
}

key_pressed = None
key_press_time = 0

def on_press(key):
    try:
        """ print('alphanumeric key {0} pressed'.format(
            key.char)) """
        global key_pressed
        key_pressed = key.char
        global key_press_time
        key_press_time = 1
    except AttributeError:
        """ print('special key {0} pressed'.format(
            key)) """
        pass

def on_release(key):
    global key_pressed
    key_pressed = None
    global key_press_time
    key_press_time = 0
    """ print('{0} released'.format(
        key)) """
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def speed_values(linear_speed, angular_speed):
    return 'Current linear speed: %s\t Current angular speed: %s ' % (linear_speed, angular_speed)

def main(args=None):
    # Start non-blocking keboard listener
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    rclpy.init()

    node = rclpy.create_node('velocity_generator')
    pub = node.create_publisher(geometry_msgs.msg.Twist, '/cmd_vel', 10)

    linear_speed = 1.0
    angular_speed = 1.0
    toggle_linear_velocity_x = 0.0
    toggle_linear_velocity_y = 0.0
    toggle_linear_velocity_z = 0.0
    toggle_angular_velocity_z = 0.0
    status = 0.0

    try:
        print(disp_msg)
        print(speed_values(linear_speed, angular_speed))
        while True:
            if key_pressed in velocity_toggle_bindings.keys():
                toggle_linear_velocity_x = velocity_toggle_bindings[key_pressed][0]
                toggle_linear_velocity_y = velocity_toggle_bindings[key_pressed][1]
                toggle_linear_velocity_z = velocity_toggle_bindings[key_pressed][2]
                toggle_angular_velocity_z = velocity_toggle_bindings[key_pressed][3]
            elif key_pressed in speed_change_bindings.keys():
                global key_press_time
                # Allow speed change to happen only once on key press
                if key_press_time == 1:
                    linear_speed = linear_speed + speed_change_bindings[key_pressed][0]
                    angular_speed = angular_speed + speed_change_bindings[key_pressed][1]

                    print(speed_values(linear_speed, angular_speed))
                    print(disp_msg)
                    key_press_time = key_press_time + 1
            else:
                toggle_linear_velocity_x = 0.0
                toggle_linear_velocity_y = 0.0
                toggle_linear_velocity_z = 0.0
                toggle_angular_velocity_z = 0.0
                if (key_pressed == '\x03'):
                    break

            twist = geometry_msgs.msg.Twist()
            twist.linear.x = toggle_linear_velocity_x * linear_speed
            twist.linear.y = toggle_linear_velocity_y * linear_speed
            twist.linear.z = toggle_linear_velocity_z * linear_speed
            twist.angular.x = 0.0
            twist.angular.y = 0.0
            twist.angular.z = toggle_angular_velocity_z * angular_speed
            pub.publish(twist)
    except Exception as e:
        print(e)
    finally:
        twist = geometry_msgs.msg.Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        pub.publish(twist)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
