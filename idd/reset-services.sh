#!/usr/bin/env bash
sudo service airtime-playout stop;
sudo service airtime-liquidsoap stop;
sudo service airtime-celery stop;


echo "waiting to reset..."
sleep 4;
sudo service airtime-playout start;
sudo service airtime-liquidsoap start;
sudo service airtime-celery start;
