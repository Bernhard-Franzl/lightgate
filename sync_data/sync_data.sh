#!/bin/bash
source /usr/local/lightgate/config.sh

dirname=data_$ROOMNAME
echo $dirname

sshpass -p Ha1lll1oo1 rsync -aPvbc -e 'ssh -p 8080' /usr/local/lightgate/$dirname/ pi_server@masterarbeit.ddns.net:$dirname 