#!/bin/sh
#Quam Sodji 2014
# This script will return the correct Mac model

Last4Ser=$(ioreg -rd1 -c IOPlatformExpertDevice | awk -F'"' '/IOPlatformSerialNumber/{print $4}' | tail -c 5)
Last3Ser=$(ioreg -rd1 -c IOPlatformExpertDevice | awk -F'"' '/IOPlatformSerialNumber/{print $4}' | tail -c 4)

FullModelName=$(curl -s -o - "http://support-sp.apple.com/sp/product?cc=${Last4Ser}&lang=en_US"  xpath //root/configCode[1] 2>&1 | awk -F'<configCode>|</configCode>' '{print $2}' | sed '/^$/d')

if [[ "$FullModelName" == "" ]]; then
    FullModelName=$(curl -s -o - "http://support-sp.apple.com/sp/product?cc=${Last3Ser}&lang=en_US"  xpath //root/configCode[1] 2>&1 | awk -F'<configCode>|</configCode>' '{print $2}' | sed '/^$/d')
fi

echo "<result>$FullModelName</result>"