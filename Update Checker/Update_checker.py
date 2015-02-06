#!/usr/bin/python
#Written by Quam Sodji

import subprocess
def schedule_status():
    schedule_status = subprocess.check_output(["softwareupdate", "--schedule"])
    schedule_status = schedule_status.strip()
    return schedule_status

check = schedule_status()
if check == "Automatic check is on":
    set_xprotect = subprocess.check_output(["softwareupdate", "--background","-critical"])
    print set_xprotect
else:
    set_scheduler = subprocess.check_output(["softwareupdate", "--schedule", "on"])
    check = schedule_status()
    print check