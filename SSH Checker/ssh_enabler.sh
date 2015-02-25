#!/bin/sh

#Script to reset and enable ssh 
#2015 Quam Sodji

#The script remove the sshd_config then recreates it
#Add the enabled default settings
#Turns remotelogin on 

sshd_fixer() {
	touch /etc/sshd_config
	echo "SyslogFacility AUTHPRIV" > /etc/sshd_config
	echo "AuthorizedKeysFile .ssh/authorized_keys" >> /etc/sshd_config
	echo "AcceptEnv LANG LC_*" >> /etc/sshd_config
	echo "Subsystem sftp /usr/libexec/sftp-server" >> /etc/sshd_config

	if [[ `systemsetup -getremotelogin` == *On ]];then
		echo "Remote login is already On.... Skipping"
		exit 0
	else
		systemsetup -setremotelogin on
	fi
}

if [[ -f "/etc/sshd_config" ]];then
	echo "Found it.. Deleting...."
	rm -r /etc/sshd_config
	sshd_fixer
else
	echo "sshd_config doesn't exists...Creating and Fixing ssh"
	sshd_fixer
fi	

exit 0