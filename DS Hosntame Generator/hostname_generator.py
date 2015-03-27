#!usr/bin/python
# Quam Sodji Copyright 2015
#jumpt.wordpress.com
# Original code was written by Tim Sutton
# http://macops.ca/interfacing-with-deploystudio-using-http/
import subprocess
import imp
import os
import urllib2
import random
import sys
import socket
import struct
import time
import calendar

global location, current_date, mount, machine_id, word_path

########  Deploystudio Credentials #####################

host = 'Deploystudio Url'
adminuser = 'Deploystudio_username'
adminpass = 'Deploystudio_password'

################### Paths ##############################

word_path = "/tmp/DSNetworkRepository/Files/words.txt"
mount = "/tmp/DSNetworkRepository/Modules/tmp/"
biplist_path = "/tmp/DSNetworkRepository/Modules/biplist/__init__.py"

##########################################################

biplist = imp.load_source('biplist',biplist_path)

def setupAuth():
    """Install an HTTP Basic Authorization header globally so it's used for
    every request."""
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password(realm='DeployStudioServer',
                              uri=host,
                              user=adminuser,
                              passwd=adminpass)
    opener = urllib2.build_opener(auth_handler)
    urllib2.install_opener(opener)

## Get the month and day from NTP instead of the mac
def getNTPTime(ntp_host = "time.apple.com"):
    port = 123
    buf = 1024
    address = (ntp_host,port)
    msg = '\x1b' + 47 * '\0'

    # reference time (in seconds since 1900-01-01 00:00:00)
    TIME1970 = 2208988800L # 1970-01-01 00:00:00

    # connect to server
    client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(msg, address)
    msg, address = client.recvfrom( buf )

    t = struct.unpack( "!12I", msg )[10]
    t -= TIME1970
    g = time.ctime(t).replace("  "," ")
    
    year = g[-2:]
    month = g[4:7]
    a = {v: k for k,v in enumerate(calendar.month_abbr)}
    num = a[month]
    if num < 10:
            num = str(0) + str(num)
    else:
         num = str(num)

    today = year + num
    return today

## Campus location based on Mac's IP Address
## If you don't need this option, Comment it out and edit hostname_generator()
## You can change the segment by changing '172' to whater string you would like to find
def network():
    interface = subprocess.check_output("ifconfig | awk ' /'172'/{print $2}'", shell=True)
    interface = interface[4:6]
    if interface == '30':
        return 'nyc'
    elif interface == '29':
         return 'sfo'

def Computer_serial():
    serial = subprocess.check_output("system_profiler SPHardwareDataType | awk '/'Serial'/{print $4}'", shell=True)
    serial = serial.strip()
    return serial

def architecture():
    mac_architecture = subprocess.check_output("arch")
    mac_architecture = mac_architecture.strip()
    return mac_architecture

def hostname_generator():
    location = network()
    current_date = getNTPTime()
    with open( word_path,'r') as f:
        words = [w.strip('\n') for w in f if len(w) == 9]
    guess = random.choice(words)
    guess = guess.lower()
    new_name = location + current_date + guess
    return new_name

machine_id = Computer_serial()

def getHostData():
    """Return the full plist for a computer entry"""
    machine_data = urllib2.urlopen(host + '/computers/get/entry?id=%s' % machine_id)
    temp_name = mount + machine_id + ".txt"
    file_name = open(temp_name,'w')
    file_name.write(machine_data.read())
    file_name.close()
    new_plist = mount + machine_id + ".plist"
    t = os.rename(temp_name, new_plist)
    plist = biplist.readPlist(new_plist)
    delete = os.remove(new_plist)
    return plist

def updateHostProperties(machine_id, properties, key_mac_addr=False, create_new=True):
    """Update the computer at machine_id with properties, a dict of properties and
    values we want to set with new values. Return the full addinfourl object or None
    if we found no computer to update and we aren't creating a new one Set create_new
    to False in order to disable creating new entries."""
    found_comp = getHostData()
    # If we found no computer and we don't want a new record created
    if not found_comp and not create_new:
        return None

    new_data = {}
    if found_comp:
        # Computer data comes back as plist nested like: {'SERIALNO': {'cn': 'my-name'}}
        # DeployStudioServer expects a /set/entry POST like: {'cn': 'my-new-name'}
        # so we copy the keys up a level
        update = dict((k, v) for (k, v) in found_comp[machine_id].items())
        new_data = update.copy()

    else:
        # No computer exists for this ID, we need to set up two required keys:
        # 'dstudio-host-primary-key' and one of 'dstudio-host-serial-number'
        # or 'dstudio-mac-addr' is required, otherwise request is ignored
        # - IOW: you can't only rely on status codes
        # - primary key is a server-level config, but we seem to need this per-host
        if key_mac_addr:
            new_data['dstudio-host-primary-key'] = 'dstudio-mac-addr'
        else:
            new_data['dstudio-host-primary-key'] = 'dstudio-host-serial-number'
        new_data[new_data['dstudio-host-primary-key']] = machine_id
    
    for (k, v) in properties.items():
        new_data[k] = v
    plist_to_post = biplist.writePlistToString(new_data)
    result = urllib2.urlopen(host + '/computers/set/entry?id=' + machine_id,
                            plist_to_post)
    return result

def main():
    setupAuth()
    # Update Computer Record with a new computer name or create a new record
    # if it doesn't exist and also add more fields if needed
    random_name = hostname_generator()
    mac_architecture = architecture()
    result = updateHostProperties(machine_id, {'cn': random_name,
                                            'dstudio-hostname': random_name,
                                            'architecture' : mac_architecture,
                                            'dstudio-host-type' : 'Mac' }, create_new=True)


if __name__ == "__main__":
    main()
