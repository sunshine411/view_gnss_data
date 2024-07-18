import matplotlib.pyplot as plt
import numpy as np

from scipy.spatial.transform import Rotation as R


def plt_gps():
    with open("../gps.txt", "r") as f:
        gps_data = [_.strip() for _ in f.readlines()]


    gps_lat = gps_data[9::15]
    gps_lon = gps_data[10::15]
    gps_alt = gps_data[11::15]

    gps_lat = [float(_.split(":")[-1]) for _ in gps_lat]
    gps_lon = [float(_.split(":")[-1]) for _ in gps_lon]
    gps_alt = [float(_.split(":")[-1]) for _ in gps_alt]
    plt.figure(figsize=(50,50))
    plt.plot(gps_lon, gps_lat)
    plt.show()
    pass


def plt_odom():
    with open("../odom.txt", "r") as f:
        odom_data = [_.strip() for _ in f.readlines()]


    odom_lat = odom_data[10::31]
    odom_lon = odom_data[11::31]
    odom_alt = odom_data[12::31]

    odom_lat = [float(_.split(":")[-1]) for _ in odom_lat]
    odom_lon = [float(_.split(":")[-1]) for _ in odom_lon]
    odom_alt = [float(_.split(":")[-1]) for _ in odom_alt]
    plt.figure(figsize=(50,50))
    plt.plot(odom_lat, odom_lon)
    plt.show()
    pass

def quaternion2euler(quaternion):
    r = R.from_quat(quaternion)
    euler = r.as_euler('xyz', degrees=True)
    return euler

def plt_imu():

    with open("imu.txt", "r") as f:
        imu_data = [_.strip() for _ in f.readlines()]

    imu_x = imu_data[7::23]
    imu_y = imu_data[8::23]
    imu_z = imu_data[9::23]
    imu_w = imu_data[10::23]

    imu_x = [float(_.split(":")[-1]) for _ in imu_x]
    imu_y = [float(_.split(":")[-1]) for _ in imu_y]
    imu_z = [float(_.split(":")[-1]) for _ in imu_z]
    imu_w = [float(_.split(":")[-1]) for _ in imu_w]

    quat = np.vstack([np.array(imu_x), np.array(imu_y), np.array(imu_z), np.array(imu_w)])
    euler = quaternion2euler(quat.T)

    # plt.figure(figsize=(50,50))
    plt.plot(euler[:,0])
    plt.plot(euler[:,1])
    plt.plot(euler[:,2])
    plt.show()
    pass

if __name__ == "__main__":
    plt_gps()
    plt_odom()