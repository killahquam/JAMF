#!/usr/bin/python
#Script to fix Local Admin account missing a Home folder
#Quam Sodji 2015

import os

if not os.path.exists("/var/administrator"):
    os.makedirs("/var/administrator")
    os.system("mkdir /var/administrator/{Desktop,Documents,Downloads,Library,Music,Pictures,Public,Movies}")
    os.system("chown -R administrator:staff /var/administrator")
    print "Home folder created"
else:
    print "Home folder exists"

