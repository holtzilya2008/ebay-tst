#!/bin/bash
#
# Stop the webserver.
# Modified by Ilya Holtz
#
MyDir=~/dev/apps/ebay-tst/unsecured/www
MyPort=8000
MyHost=localhost
WsBase=$MyDir/logs/webserver-$MyHost-$MyPort
PidFile=$WsBase.pid
if [ -f $PidFile ] ; then
    Pid=$(cat $PidFile)
    pkill $Pid
 #    if kill -0 $Pid 2>&1 >/dev/null ; then
	# echo  "stopping $Pid"
	# kill -9 $Pid
 #    fi
    rm -f $PidFile
fi
echo "stopped"
