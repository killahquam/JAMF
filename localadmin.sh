#!/usr/bin/bash
#Create a localadmin via script
#Copyright by Quam Sodji 2014
dscl . create /Users/administrator
dscl . create /Users/administrator UserShell /bin/bash
dscl . create /Users/administrator RealName "administrator"
dscl . create /Users/administrator UniqueID 503
dscl . create /Users/administrator PrimaryGroupID 1000
dscl . create /Users/administrator NFSHomeDirectory /Local/Users/administrator
dscl . passwd /Users/administrator PASSWORD
dscl . append /Groups/admin GroupMembership administrator
