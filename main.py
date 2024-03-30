from receiver.receiver_device import Receiver
from emitter.emitter_device import Emitter
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
dir_path = os.path.dirname(os.path.realpath(__file__))

if device_type == "receiver":

    receiver = Receiver(working_dir=dir_path, install_dir=device_install_dir, system_dir=device_system_dir, 
                    roomname=device_roomname, doornumber=device_doornumber)
    
    receiver.setup()
    #receiver.disable()
    
elif device_type == "emitter":
    emitter = Emitter(working_dir=dir_path, install_dir=device_install_dir, system_dir=device_system_dir, 
                    roomname=device_roomname, doornumber=device_doornumber)
    
    emitter.setup(install_pigpio=True)
    #emitter.disable()

else:
    raise Exception("Unknown Device Type")

