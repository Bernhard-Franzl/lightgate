#!/bin/bash
source /usr/local/lightgate/config.sh

working_directory=/usr/local/lightgate

if sshpass -p Ha1lll1oo1 ssh pi_server@masterarbeit.ddns.net -p 8080  true; then
    echo "webserver is alive"
    python3 $working_directory/archive_management/archive_management.py
    if sshpass -p Ha1lll1oo1 rsync -aPvbc -e 'ssh -p 8080' $working_directory/archive/ pi_server@masterarbeit.ddns.net:archive/; then
        systemctl stop receiver.service
        rm -r $working_directory/data_$ROOMNAME
        systemctl start receiver.service
    else
        echo "sync not successful"
    fi
else
    echo "webserver is down"
fi
