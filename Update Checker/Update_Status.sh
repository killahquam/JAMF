#!/bin/bash
#Script to verify the status of Auto Updates
#to ensure Critical and Security updates are applied
#By Quam Sodji Copyright 2015

### Check for schedule, critical and config settings
schedule_status=$(softwareupdate --schedule)
critical_status=$(defaults read /Library/Preferences/com.apple.SoftwareUpdate CriticalUpdateInstall 2>/dev/null)
config_status=$(defaults read /Library/Preferences/com.apple.SoftwareUpdate ConfigDataInstall 2>/dev/null)
run_config=$(softwareupdate --background-critical)

### The expected settings for schedule, critical and config
schedule_on="Automatic check is on"
critical_on="1"
config_on="1"


if [ "$schedule_status" == "$schedule_on" ] && [ "$critical_status" == "$critical_on" ] && [ "$config_status" == "$config_on" ]; then

    result="Enabled"
else
    result="Disabled"
fi

echo "<result>$result</result>"

