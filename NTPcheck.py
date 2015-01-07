#!/usr/bin/python
#Script written by Quam Sodji
#Copyright 2014 Quam Sodji
#Script checks for NTP vulnerability patch via casper

import subprocess
import platform

def check_ntp():
     check = subprocess.check_output(["what", "/usr/sbin/ntpd"])  
     o = check.strip()
     p = o.split()
     t = p[2]
     c = t.split(":")
     result = c[1]
     return result

#Check the version and also handles new sub versions of Yosemite
def check_version():
    osvers = platform.mac_ver()[0] 
    sub_ver = osvers[3:]
    sub_ver = float(sub_ver)

    if sub_ver == 8.5:
       return "Mountain Lion 10.8.5"
    elif sub_ver == 9.5:
       return "Mavericks 10.9.5"   
    elif sub_ver >= 10.1:
         return "Yosemite"
    else:
         return osvers

print check_version()
applied_patch = ["ntp-77.1.1","ntp-88.1.1","ntp-92.5.1"]

#The NTP fix is only available for the following OSX versions
Needed_vers = ["Mountain Lion 10.8.5", "Mavericks 10.9.5", "Yosemite"]

running_version = check_version()
if not running_version in Needed_vers:
       Status = "No:OS is %s"%running_version
else:       
     result = check_ntp()

     if result in applied_patch:
        Status =  "Yes"
     else:
          apply_update = subprocess.check_output(["softwareupdate", "--install", "OS X NTP Security Update-1.0"])
          value_one = check_ntp()
          if value_one in applied_patch:
             Status = "Yes"
          else:
               Status = apply_update

    
print "<result>%s</result>" %Status
