How to set up the receiver raspberry pi, on Ubuntu Server:

##### Guide with new code base #####

1.) pull latest version of github repository
manually install git 

2.) specify all the information in the config.ini

3.) run main.py -> done

4.) at the end when prompted to delete everything unnecessary write -> yes

##### Manual mode #####
if he dosent find the access point
sudo systemctl restart wpa_supplicant.service

1.) sudo apt update
#sudo apt upgrade
#sudo apt autoremove

sudo apt install python3-RPi.GPIO network-manager net-tools raspi-config wireless-tools sshpass openssh-server


2.) scp or pi_receiver from webserver
scp -r -P 8080 pi_server@masterarbeit.ddns.net:~/pi_receiver/* ~

3.) ssh once to pi_server, to add to known hosts
ssh pi_server@masterarbeit.ddns.net -p 8080
sudo ssh pi_server@masterarbeit.ddns.net -p 8080 #also sudo into it needed for data management

4.) move system files into /etc/systemd/system

-> change conf file correct roomname and door in system folder
sudo nano system/ir_receiver.service.d/ir_receiver.conf

sudo mv system/* /etc/systemd/system
rm -r system


5.) Enable all services:
-> change conf file correct roomname and door
sudo nano ir_receiver.conf

afterwards start and "enable" both services, sudo systemctl enable/start *.service

sudo systemctl enable ir_receiver.service sync_data.service sync_data.timer sync_ip.service  sync_ip.timer  archive_management.timer 
sudo systemctl daemon-reload
sudo systemctl restart ir_receiver.service sync_data.service sync_data.timer sync_ip.service  sync_ip.timer  archive_management.timer

sudo reboot

#sudo apt upgrade
#sudo reboot

sudo nano /etc/systemd/system/ir_receiver.service.d/ir_receiver.conf
sudo nano ir_receiver.conf 
