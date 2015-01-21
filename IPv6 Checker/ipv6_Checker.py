#!/usr/bin/python

#Copyright 2014 Quam Sodji

import subprocess

def getinfo(hardware): #Return network info on select interface
    info = subprocess.check_output(["networksetup", "-getinfo", hardware])
    return info

wireless = ["Airport", "Wi-Fi"]  #The two type of interfaces that refers to wireless

list_network = subprocess.check_output(["networksetup", "-listallnetworkservices"])
list_network = list_network.split('\n')

for device in wireless:
    if device in list_network: 
      response = getinfo(device)
      response_check = response.split("\n")
      if "IPv6: Off" not in response_check:
         check = subprocess.check_output(["networksetup", "-setv6off", device])
         Status = "Off"
      else:
           for setting in response_check:
               if setting.startswith("IPv6:"):
                  if setting != "IPv6: Off":
                    Status = setting
                  else:
                       Status = "Off"
    else:
        Status = "No wireless interfaces configured"
        continue
          

print "<result>%s</result>"%Status
