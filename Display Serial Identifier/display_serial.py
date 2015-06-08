#!/usr/bin/python
# Quam Sodji Copyright 2015
# Extension Attribute to retrive attached Display serial numbers if any
# Only applicable to monitors connected via HDMI, Thunderbolt or DVI

import subprocess

display_profile = subprocess.check_output(["system_profiler SPDisplaysDataType | awk '/Serial/ {print $4}'"],shell=True)
display_serial = display_profile.strip()
serials = display_serial.split("\n")
serials = filter(None,serials)
size = len(serials)
results = []

if not serials:
    print "<result>N/A</result>"

else:
    t = 1
    while t != size + 1:
        for i in serials:
            form = "%i:%s"%(t,i)
            results.append(form)
            t += 1
            
    recon_res = ('\n').join(results)
    print "<result>%s</result>"%recon_res
