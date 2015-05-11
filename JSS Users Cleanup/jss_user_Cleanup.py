#!/usr/bin/python
#Quam Sodji 2015
#Script for cleaning up JSS of empty users (users not associated with a computer)
#Script is using python-jss to access the JSS via the REST API and Kn/Slack 
#https://pypi.python.org/pypi/python-jss/0.5.9
#https://github.com/kn/slack
#Load script onto JSS and setup with a once a week cron job

import jss
import xml.etree.cElementTree as ET
import sys
import smtplib
import slack
import slack.chat

######### EMAIL SETTINGS #######

sender = 'from email goes here'
receivers = ['send to emails go here'] #You can have multiple emails
smtp_server = smtplib.SMTP('smtp server url','smtp port') #smtp server & port

######### SLACK SETTINGS #######
slack.api_token = 'slack-token'
slack_channel = ['slack channel'] #Supports multiple channels

####################################
## JSS URL, USERNAME & PASSWORD ##

gree_jss = jss.JSS(
    url='https://your_jss_url:8443',
    user='jss_username',
    password='jss_password')    #JSS account should be read Only on Computers,
                                #Mobile Device and Read 7 Delete on Users

#######################################

def email_me(): #Send email
    try:
        smtp_server.sendmail(sender, receivers, message)
        print "Email was sent successfully"
    except smtplib.SMTPException:
       print "Error: unable to send email"

def slack_me(): #use Slack
    for channel in slack_channel:
        slack.chat.post_message(channel, message, username='CASPER_BOT')

#############################################

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

    #email_me() #Uncomment for email
    #slack_me() #Uncomment for slack

    #You can uncomment both if you want both



