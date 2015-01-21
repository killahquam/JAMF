#!/bin/sh
# Written by Quam Sodji
#Copyright 2014 Quam Sodji

# Script will capture the assigned ARDComputerField (Field 4) in DS and set it as Asset Tag in Casper

asset=$(defaults read /Library/Preferences/com.apple.RemoteDesktop Text4)

sudo jamf recon -assetTag $asset

exit 0
