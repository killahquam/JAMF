#!/bin/sh

#Script to reset and enable ssh 
#2015 Quam Sodji

#The script remove the sshd_config then recreates it
#Add the enabled default settings
#Turns remotelogin on 


rm -r /etc/sshd_config
touch /etc/sshd_config
echo "SyslogFacility AUTHPRIV" > /etc/sshd_config
echo "AuthorizedKeysFile .ssh/authorized_keys" >> /etc/sshd_config
echo "AcceptEnv LANG LC_*" >> /etc/sshd_config
echo "Subsystem sftp /usr/libexec/sftp-server" >> /etc/sshd_config
systemsetup -setremotelogin on

exit 0