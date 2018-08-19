#!/bin/sh
for (( i = 0; i < 10; i++ ));do
	sleep 2
	echo -e "\033[31m$i\033[0m"
done
