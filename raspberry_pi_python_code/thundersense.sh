#!/bin/sh
# /etc/init.d/thundersense.sh
### BEGIN INIT INFO
# Provides: thundersense
# Required-Start: $network $syslog $remote_fs
# Required-Stop: $network
# Default-Start: 2 3 5
# Default-Stop: 0 1 6
# Short-Description: M1 python
# Description: Start or stop the M1 python script
### END INIT INFO



case "$1" in
  start)
    echo "Starting Service "
    python /m1/m1_thundersense_rpi_demo.py
    ;;
  stop)
    echo "Stopping Service "
    ;;
  *)
    echo "Usage: /etc/init.d/test {start|stop}"
    exit 1
    ;;
esac

exit 0
