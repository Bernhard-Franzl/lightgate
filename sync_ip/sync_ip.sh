#!/bin/bash
source /usr/local/lightgate/config.sh

dirname=ip_$ROOMNAME
sudo mkdir -p /usr/local/lightgate/$dirname 

hostn=$(hostname)
filename=ip_$hostn.txt

echo "$(hostname -I)" >> /usr/local/lightgate/$filename
echo "$(date)" >> /usr/local/lightgate/$filename


sudo mv /usr/local/lightgate/$filename /usr/local/lightgate/$dirname/$filename

sshpass -p Ha1lll1oo1 rsync -aPvbc -e 'ssh -p 8080' /usr/local/lightgate/$dirname/ pi_server@masterarbeit.ddns.net:$dirname 

