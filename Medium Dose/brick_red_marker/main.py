import time
#Added this cuz i wanted to simulate this in real time
import math

class brick_stuff:
    def __init__(self, dist = 0.55, speed = 0.5, ang_vel = 0.5):
        self.dist = dist #cuz the initial frame of ref was at the camera which was at the front of the rover.
                         #i moved it to the center of the rover which should be 55 cm behind the camera
        self.speed = speed
        self.ang_vel = ang_vel
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0 #starting line at the origin
    def input_marker(self):
        red_marker_x = float(input("Enter the x coordinate of the red marker\n"))
        red_marker_y = float(input("Enter the y coordinate of the red marker\n"))
        red_marker_z = float(input("Enter the z coordinate of the red marker\n"))
        return red_marker_x, red_marker_y, red_marker_z
    def det_marker(self, red_marker_x, red_marker_y, red_marker_z):
        print(f"Red marker detected at ({red_marker_x} , {red_marker_y} , {red_marker_z})")
        marker_new_x = red_marker_x
        marker_new_y = red_marker_y
        marker_new_z = red_marker_z + self.dist #i've assumed that the rover is positioned in such a way that the center of the rover is 55 cm behind the camera along the z axis
        return marker_new_x, marker_new_y, marker_new_z
    def move_brick(self, marker_new_x, marker_new_y, marker_new_z):
        print(f"Currently movin to ({marker_new_x} , {marker_new_y} , {marker_new_z})")
        dist_x = marker_new_x - self.pos_x
        dist_y = marker_new_y - self.pos_y
        dist_z = marker_new_z - self.pos_z
        dist = math.sqrt(dist_x**2 + dist_y**2 + dist_z**2)
        time_req = dist/self.speed
        time.sleep(time_req)
        self.pos_x = marker_new_x
        self.pos_y = marker_new_y
        self.pos_z = marker_new_z
        print(f"Currently at the right position....Bout to do a 360...")
    def turn(self):
        turn_time = (2*math.pi)/self.ang_vel
        time.sleep(turn_time)
        print(f"Successfully performed the 360 degree turn")

if __name__ == "__main__":
    rover = brick_stuff()
    marker_x, marker_y, marker_z = rover.input_marker()
    new_x, new_y, new_z = rover.det_marker(marker_x, marker_y, marker_z)
    rover.move_brick(new_x, new_y, new_z)
    rover.turn()


