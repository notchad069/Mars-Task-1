#!/bin/bash
echo "Pre mission check startin..."
read -p "Enter the battery percentage: " Battery

if [ $Battery -ge 20 ]; then
	echo "Good to go!"
else
	echo "Nah get back to base"
fi

if ping -c 1 www.google.com ; then
	echo "Communications systems are workin"
else
	echo "Communication failure"
fi
	
if [ $Battery -ge 20 ] && ping -c 1 www.google.com ; then
	echo "All systems operational"
fi	
 
