#!/bin/bash
echo "[Service]" > ir_receiver.conf
echo "Environment=\"ROOMNAME=$ROOMNAME\"" >> ir_receiver.conf
echo "Environment=\"DOORNUMBER=$DOORNAME\"" >> ir_receiver.conf
