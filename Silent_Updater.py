#!/usr/bin/python

import subprocess
import platform
lop = []
top = []
check = subprocess.check_output(["softwareupdate", "-l"])  
check_two = check.split("\n")
for i in check_two:
   t = i.strip()
   if t.startswith("*"):
     lop.append(t)
     b = "\n".join(lop)
   else:
        top.append(t)
        c = "\n".join(top)
        c = c.strip()
        c = c.split("[recommended]")


