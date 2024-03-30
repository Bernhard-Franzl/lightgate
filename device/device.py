import os
import subprocess

class Device:     
           
    def __init__(self, device_type:str, working_dir:str, install_dir:str, system_dir:str, roomname:str, doornumber:int):
        """
        Initializes a new instance of the Device class.
        """
        self.device_type = device_type        
        self.roomname = roomname
        self.doornumber = doornumber
        self.working_dir = working_dir
        
        self.install_dir = install_dir
        os.makedirs(os.path.dirname(self.install_dir), exist_ok=True)
        
        self.system_path = system_dir
        os.makedirs(os.path.dirname(self.system_path), exist_ok=True)
    
    def generate_bash_config_file(self):
        """
        Generates a bash config file.
        """
        with open(os.path.join(self.working_dir, "config.sh"), "w") as file:
            
            file.write(f"ROOMNAME={self.roomname}\n")
            file.write(f"DOORNUMBER={self.doornumber}\n")
            file.write(f"DEVICETYPE={self.device_type}\n")
            
        self.copy_file(os.path.join(self.working_dir, "config.sh"), os.path.join(self.install_dir, "config.sh"))
             
    def install_packages(self, packages):
        subprocess.run(["sudo", "apt", "update"])
        for package in packages:
            subprocess.run(["sudo", "apt", "install", "-y", package])

    def make_directory(self, directory:str):
        """
        Creates a new directory in the specified path as sudo.
        """
        subprocess.run(["sudo", "mkdir", "-p", directory])
        
    def copy_file(self, src:str, dest:str):
        """
        Moves a file from the source to the destination and creates all missing directories in the destination.
        """
        self.make_directory(os.path.dirname(dest))
        os.system(f"sudo cp {src} {dest}")
        
    def setup_service(self, directory):
        
        has_timer = False
        
        # handle service files in the directory
        for file in os.listdir(directory):
            
            # separate based on file extension
            if file.endswith(".service"):
                self.copy_file(os.path.join(self.working_dir, directory, file),
                                os.path.join(self.system_path, file)) 
                 
            elif file.endswith(".timer"):
                self.copy_file(os.path.join(self.working_dir, directory, file),
                                os.path.join(self.system_path, file)) 
                has_timer = True
                            
            elif file.endswith(".conf"):
                self.copy_file(os.path.join(self.working_dir, directory, file),
                                os.path.join(self.system_path, f"{directory}.service.d", file))
            
            elif file.endswith(".py") or file.endswith(".txt") or file.endswith(".sh"):
                self.copy_file(os.path.join(self.working_dir, directory, file),
                                os.path.join(self.install_dir, directory, file))   
                
            else:
                if file not in ["__pycache__"]:
                    print(file)
                    raise Exception("Unknown file type.")
                
        return has_timer

    def enable_services(self, service_list:list, has_timer_list:list):
        """
        Enables services or the respective timers.
        """
        for i, service in enumerate(service_list):
            if has_timer_list[i]:
                os.system(f"sudo systemctl enable {service}.timer")
            else:
                os.system(f"sudo systemctl enable {service}.service")
    
    def start_services(self, service_list:list, has_timer_list:list):
        """
        Starts services.
        """
        for i, service in enumerate(service_list):
            if has_timer_list[i]:
                os.system(f"sudo systemctl start {service}.timer")
            else:
                os.system(f"sudo systemctl start {service}.service")

    def disable_services(self, service_list:list, has_timer_list:list):
        """
        Disables services or the respective timers.
        """
        for i, service in enumerate(service_list):
            if has_timer_list[i]:
                os.system(f"sudo systemctl disable {service}.timer")
                os.system(f"sudo systemctl disable {service}.service")
            else:
                os.system(f"sudo systemctl disable {service}.service")
                
    def stop_services(self, service_list:list, has_timer_list:list):
        """
        Stops services.
        """
        for i, service in enumerate(service_list):
            if has_timer_list[i]:
                os.system(f"sudo systemctl stop {service}.timer")
                os.system(f"sudo systemctl stop {service}.service")
            else:
                os.system(f"sudo systemctl stop {service}.service")
    
    def restart_services(self, service_list:list, has_timer_list:list):
        """
        Restarts services.
        """
        for i, service in enumerate(service_list):
            if has_timer_list[i]:
                os.system(f"sudo systemctl restart {service}.timer")
            else:
                os.system(f"sudo systemctl restart {service}.service")