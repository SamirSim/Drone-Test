from dronekit import *
import time
import json
from datetime import datetime, date

init = {}
with open('telemetry_info.json', 'w') as json_file:
	json.dump(init, json_file)

telemetry_infos = []

def fill_info(info):
	with open('telemetry_info.json', 'r+') as file:
		data = json.load(file)
		data.update(info)
		file.seek(0)
		json.dump(data, file, sort_keys=True, indent=2)


#vehicle = connect('127.0.0.1:14550', wait_ready=True)
vehicle = connect('127.0.0.1:14550',  wait_ready=False)

#vehicle.mode = VehicleMode("MISSION")
while (True):
	# vehicle is an instance of the Vehicle class
	print ("Autopilot Firmware version: ", vehicle.version)
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

	telemetry_data = {
		"time": str(datetime.now()),
		"firmware_version": str(vehicle.version),
		"global_location": str(vehicle.location.global_frame),
		"global_location_relative_altitude": str(vehicle.location.global_relative_frame),
		"local_location": str(vehicle.location.local_frame),
		"attitude": str(vehicle.attitude),
		"velocity": str(vehicle.velocity),
		"gps": str(vehicle.gps_0),
		"ground_speed": str(vehicle.groundspeed),
		"airspeed": str(vehicle.airspeed),
		"gimbal_status": str(vehicle.gimbal),
		"battery": str(vehicle.battery),
		"enf_ok": str(vehicle.ekf_ok),
		"last_heartbeat": str(vehicle.last_heartbeat),
		"range_finder": str(vehicle.rangefinder),
		"range_finder_distance": str(vehicle.rangefinder.distance),
		"range_finder_voltage": str(vehicle.rangefinder.voltage),
		"heading": str(vehicle.heading),
		"is_armable ": str(vehicle.is_armable),
		"system_status": str(vehicle.system_status.state),
		"mode": str(vehicle.mode.name),
		"armed": str(vehicle.armed)											
	}

	telemetry_infos.append(telemetry_data)

	toFill = {
		"data": telemetry_infos
	}

	with open('telemetry_info.json', 'r+') as file:
		data = json.load(file)
		data.update(toFill)
		file.seek(0)
		json.dump(data, file, sort_keys=True, indent=2)


	time.sleep(2)