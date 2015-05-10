#!/usr/bin/python
#Quam Sodji 2015
#Script for cleaning up JSS of empty users (users not associated with a computer)
#Script is using python-jss to access the JSS via the REST API
#https://pypi.python.org/pypi/python-jss/0.5.9
#Load script onto JSS and setup with a once a week cron job

import jss
import xml.etree.cElementTree as ET
import sys
import smtplib

######### SMTP SETTINGS #######

sender = 'from email goes here'
receivers = ['send to emails go here'] #You can have multiple emails

smtpObj = smtplib.SMTP('smtp server url','smtp port') #smtp server & port

####################################
## JSS URL, USERNAME & PASSWORD ##

gree_jss = jss.JSS(
    url='https://your_jss_url:8443',
    user='jss_username',
    password='jss_password')

#######################################
qualifier = []
id_to_remove = []
jss_names = []
removed_names = []

#Pull a list of all the users in the JSS
registered_users = str(gree_jss.User())
found_users = registered_users.split('\n')
for assigned_users in found_users:
    if "name" in assigned_users:
        qualifier.append(assigned_users)
for username in qualifier:
    username =  username[7:]
    jss_names.append(username)

#Find the users who do not have a computer assigned to them
for ind in jss_names:
    w = []
    boy = gree_jss.User(ind)
    tree = ET.ElementTree(boy)
    root = tree.getroot()
    for child in root.iter():
         w.append({child.tag:child.text})
    if len(w) < 21:
        id_to_remove.append(root[0].text)
        full_name = ind.replace("."," ")
        removed_names.append(full_name)
    else:
        pass

#Remove found users from the JSS        
if id_to_remove == []:
    print "No user found!"
    sys.exit(0)
else:
    user_count = len(id_to_remove)
    print "Found %i users without computers."%user_count
    for user_to_remove in id_to_remove:
        remove_user = gree_jss.User(user_to_remove)
        remove_user.delete()
    print "Users deleted: %i"%user_count
#Send email with removed users list
    removed_names = '\n'.join(removed_names)
    message = "Removed Users:\n %s"%removed_names
try:
    smtpObj.sendmail(sender, receivers, message)
    print "Email was sent successfully"
except SMTPException:
   print "Error: unable to send email"
