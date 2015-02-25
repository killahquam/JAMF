#!/bin/sh

#Reports back the status of SSH Remote Login via  Attribute
#Quam Sodji

ssh_chk=`systemsetup -getremotelogin`
ssh_conf="/etc/sshd_config"

if [[ "$ssh_chk" == *On ]] && [[ -f "$ssh_conf" ]]; then

   result="Enabled"
else
   result="Disabled"
fi

echo "<result>$result</result>"