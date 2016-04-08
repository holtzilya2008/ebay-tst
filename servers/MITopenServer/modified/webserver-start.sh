#!/bin/bash
#
# Start the webserver.
# Modified by ilya Holtz
#
MyDir=~/dev/apps/ebay-tst/unsecured/www
MyPort=8000
MyHost=localhost
WsBase=$MyDir/logs/webserver-$MyHost-$MyPort
PidFile=$WsBase.pid
if [ -f $PidFile ] ; then
    Pid=$(cat $PidFile)
    if kill -0 $Pid 2>&1 >/dev/null ; then
	echo "ERROR: webserver is already running, PID=$Pid"
	exit 1
    else
	# The process does not exist, remove the pid file.
	rm -f $PidFile
    fi
fi

./webserver.py -H $MyHost -v -p $MyPort -l warning -r $MyDir -d $MyDir/logs
echo "started"
