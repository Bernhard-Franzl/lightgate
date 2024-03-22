from receiver.receiver import Receiver
import configparser
import os 


# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve the main arguments from the config file
device_type = config.get('Device', 'Type')
device_install_dir = config.get('Device', 'InstallationDirectory')
device_system_dir = config.get('Device', 'SystemDirectory')
device_roomname = config.get('Device', 'Roomname')
device_doornumber = config.getint('Device', 'Doornumber')

# Create a new instance of the Device class
if device_type == "receiver":

    dir_path = os.path.dirname(os.path.realpath(__file__))

    device = Receiver(working_dir=dir_path, install_dir=device_install_dir, system_dir=device_system_dir, 
                    roomname=device_roomname, doornumber=device_doornumber)
    
    device.setup_receiver()
    
elif device_type == "emitter":
    pass

else:
    raise Exception("Unknown device type.")

