#!/usr/bin/python
#Quam Sodji 2015
#Setup script to install the needed python modules
#Installs kn/Slack and python-jss modules
#We assume you have Git installed.......
import subprocess
import os
import sys
import shutil

clone_jss = subprocess.check_output(['git','clone','git://github.com/sheagcraig/python-jss.git'])
clone_slack = subprocess.check_output(['git','clone','git://github.com/kn/slack.git'])
path = os.path.dirname(os.path.realpath(__file__))

#Installing Slack
print "Installing Slack"
slack_folder = os.chdir(path + '/slack')
install_slack = subprocess.check_output(['python','setup.py','install'])
print "slack module installed"
#Installing Python JSS
print "Installing Python JSS"
jss_folder = os.chdir(path + '/python-jss')
install_jss = subprocess.check_output(['python','setup.py','install'])
print "python-jss module installed"
#Cleaning up
print "Cleaning up"
change_location = os.chdir(path)
remove_slack_clone = shutil.rmtree(path + '/slack')
remove_jss_clone = shutil.rmtree(path + '/python-jss')
print "Done."
sys.exit(0)