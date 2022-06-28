#!/bin/sh

# copy crontab template
cp /crontab.txt /etc/crontabs/root
# copy template s3cfg
# cp /.s3/.s3cfg /root/.s3cfg

python3 /run.py

# start cron
crond -f