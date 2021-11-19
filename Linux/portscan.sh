#!/bin/bash
host=192.168.1.2
for port in {1..65535}; do
	timeout .1 bash -c "echo > /dev/tcp/$host/$port" &&
		echo "port $port is open"
done
echo "Done."