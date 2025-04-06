import numpy as np #numpy is used cuz we need to represent vectors/arrays
def eultoquat(roll, pitch, yaw):
    c_roll = np.cos(roll/2)
    s_roll = np.sin(roll/2)
    c_pitch= np.cos(pitch/2)
    s_pitch = np.sin(pitch/2)
    c_yaw = np.cos(yaw/2)
    s_yaw = np.sin(yaw/2)

    w = (c_roll)*(c_pitch)*(c_yaw) + (s_roll)*(s_pitch)*(s_yaw)
    x = (s_roll)*(c_pitch)*(c_yaw) - (c_roll)*(s_pitch)*(s_yaw)
    y = (c_roll)*(s_pitch)*(c_yaw) + (s_roll)*(c_pitch)*(s_yaw)
    z = (c_roll)*(c_pitch)*(s_yaw) - (s_roll)*(s_pitch)*(c_yaw)

    return float(w),float(x),float(y),float(z)

if __name__ == "__main__":
    r = float(input("Enter the roll angle: "))
    roll = np.radians(r)
    p = float(input("Enter the pitch angle: "))
    pitch = np.radians(p)
    y = float(input("Enter the yaw angle: "))
    yaw = np.radians(y)

    quaternion = eultoquat(roll, pitch, yaw)
    print(f"The conversion is here : {quaternion}")
