from device.device import Device
import os

class Receiver(Device):
    device_type = "receiver"
    
    def __init__(self, working_dir:str, install_dir:str, system_dir:str, roomname:str, doornumber:int):
        """
        Initializes a new instance of the Receiver class.
        """
        super().__init__(self.device_type, working_dir, install_dir, system_dir, roomname, doornumber)
        
        self.service_list = ["receiver", "sync_data", "sync_ip", "archive_management"]      
        #self.service_list = ["sync_ip"]    
        
    def setup(self):
        
        # install the required packages
        with open(os.path.join(self.working_dir, self.device_type, "requirements.txt"), "r") as file:
            packages_to_install = file.read().splitlines()

        # Call the install_packages function
        self.install_packages(packages_to_install)
        
        # generate the bash config file
        self.generate_bash_config_file()
        print("Bash configuration file generated.")
        
        # generate the ir receiver configuration file
        self.generate_ir_receiver_conf()
        print("IR receiver configuration file generated.")
        
        # setup the services move the files to the correct directories
        has_timer_list = []
        for service in self.service_list:
            print(f"Setting up the {service} service...")
            has_timer = self.setup_service(directory=service)
            has_timer_list.append(has_timer)

        # enable the services or the timers
        print("Enabling the services...")
        self.enable_services(self.service_list, has_timer_list)
        
        print("Reloading the systemd manager...")
        os.system("sudo systemctl daemon-reload")
        
        print("Starting the services...")
        self.start_services(self.service_list, has_timer_list)
        
        print("###################################")
        print("Do not forget to change hostname!")
        print("###################################")
 
    def disable(self):
        # disable the services or the timers
        print("Disabling the services...")
        # brute force by assuming that all services have timers
        self.has_timer_list = [True for i in range(len(self.service_list))]
        self.disable_services(self.service_list, self.has_timer_list)
        
        print("Reloading the systemd manager...")
        os.system("sudo systemctl daemon-reload")
        
        print("Stopping the services...")
        self.stop_services(self.service_list, self.has_timer_list)
                                           
    def generate_ir_receiver_conf(self):
        """
        Generates the IR receiver configuration file for the device.
        """
        with open(os.path.join(self.working_dir,"receiver","receiver.conf"), "w") as f:
            f.write(f"[Service]\n")
            f.write(f"""Environment="ROOMNAME={self.roomname}"\n""")
            f.write(f"""Environment="DOORNUMBER={self.doornumber}"\n""")
            f.write(f"WorkingDirectory={self.install_dir}\n")
    
