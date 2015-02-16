#!/bin/bash
#Enable updates
#Enable critical updates
#Quam Sodji Copyright 2015

defaults write /Library/Preferences/com.apple.SoftwareUpdate CriticalUpdateInstall -bool yes
defaults write /Library/Preferences/com.apple.SoftwareUpdate ConfigDataInstall -bool yes
schedule=$(softwareupdate --schedule on)
run_config=$(softwareupdate --background-critical)

exit 0
