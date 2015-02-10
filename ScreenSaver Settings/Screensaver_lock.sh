#!/usr/bin/sh
#Script will set values for the screensaver settings to ensure a password prompt
#immediatly after the screensaver kicks in
#Quam Sodji

user=`defaults read /Library/Preferences/com.apple.loginwindow lastUserName`

defaults write /Users/"$user"/Library/Preferences/com.apple.screensaver askForPassword -int 1
defaults write /Users/"$user"/Library/Preferences/com.apple.screensaver askForPasswordDelay -int 0
chown $user /Users/"$user"/Library/Preferences/com.apple.screensaver.plist
