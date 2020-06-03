from dronekit import *
import time

#vehicle = connect('127.0.0.1:14550', wait_ready=True)
vehicle = connect('127.0.0.1:14550',  wait_ready=False)

#vehicle.mode = VehicleMode("MISSION")
while (True):
  # vehicle is an instance of the Vehicle class
  print ("Autopilot Firmware version: ", vehicle.version                                       )
  #print ("Autopilot capabilities (supports ftp): ", vehicle.capabilities.ftp)
  print ("Global Location: ", vehicle.location.global_frame)
  print ("Global Location (relative altitude): ", vehicle.location.global_relative_frame)
  print ("Local Location: ", vehicle.location.local_frame)    #NED
  print ("Attitude: ", vehicle.attitude)
  print ("Velocity: ", vehicle.velocity)
  print ("GPS: ", vehicle.gps_0)
  print ("Groundspeed: ", vehicle.groundspeed)
  print ("Airspeed: ", vehicle.airspeed)
  print ("Gimbal status: ", vehicle.gimbal)
  print ("Battery: ", vehicle.battery)
  print ("EKF OK?: ", vehicle.ekf_ok)
  print ("Last Heartbeat: ", vehicle.last_heartbeat)
  print ("Rangefinder: ", vehicle.rangefinder)
  print ("Rangefinder distance: ", vehicle.rangefinder.distance)
  print ("Rangefinder voltage: ", vehicle.rangefinder.voltage)
  print ("Heading: " , vehicle.heading)
  print ("Is Armable?: ", vehicle.is_armable)
  print ("System status: ", vehicle.system_status.state)
  print ("Mode: ", vehicle.mode.name)    # settable
  print ("Armed: ", vehicle.armed)    # settable

  time.sleep(3)