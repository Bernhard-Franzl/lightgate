#!/bin/bash
mkdir -p /etc/systemd/system/ir_receiver.service.d 
cp -f conf_files/ir_receiver.conf /etc/systemd/system/ir_receiver.service.d

