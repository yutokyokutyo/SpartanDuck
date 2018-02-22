#!/bin/sh
cd /home/pi/open-jtalk/AquesTalkPi/aquestalkpi
./AquesTalkPi -s 80 $@ | aplay
cd /home/pi/
