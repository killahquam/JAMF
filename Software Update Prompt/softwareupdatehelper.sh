#!/bin/bash

####################################################################################################
#
# Copyright (c) 2015, Quam Sodji.
# Script will prompt the user after Casper has installed the OS X updates to restart
# If the user chooses later, he will be prompted again in 4 hours at which time
# the user will only have the option to restart now
####################################################################################################

## Get the logged in user's name
userName=$(/usr/bin/stat -f%Su /dev/console)

## CUSTOMIZABLE SETTINGS  ####################
TIME=4 #in Hours

if [ "$TIME" == 1 ];then
	TIMESTAMP="hour"
else
	TIMESTAMP="hours"
fi
SCHEDULE="$TIME $TIMESTAMP"
JAMFHELPER="/Library/Application Support/JAMF/bin/jamfHelper.app/Contents/MacOS/jamfHelper"
LOGO="/private/tmp/COMPANY.icns"
TITLE="COMPANY IT Client Management"
PROMPT_HEADING="Updates have been installed on your Mac"
PROMPT_MESSAGE="Please restart your Mac to complete the process.
You can restart now or your Mac will be restarted automatically in "$SCHEDULE"."
PROMPT_MESSAGE_TWO="Please restart your Mac now to complete the update process!"
WAIT=$(($TIME * 3600)) #Based on the time entered, the counter will be set in seconds
#################  END #######################
# Display a GREE Corp branded prompt explaining the password prompt.
reply=$("$JAMFHELPER" -windowType utility -lockHUD -icon "$LOGO" -title "$TITLE" -heading "$PROMPT_HEADING"\
		-description "$PROMPT_MESSAGE" -button1 "Now" -defaultButton 1 -button2 "Later")

if [ "$reply" == 0 ];then
	echo "Rebooting......"
	reboot=$(shutdown -r now)

else
	echo "$userName chose to reboot later"
	sleep $WAIT  
	
	reply1=$("$JAMFHELPER" -windowType utility -lockHUD -icon "$LOGO" -title "$TITLE"\
		-description "$PROMPT_MESSAGE_TWO" -button1 "Now" -defaultButton 1)

	if [ "$reply1" == 0 ];then
		echo "Rebooting......"
		reboot=$(shutdown -r now)
	fi
fi