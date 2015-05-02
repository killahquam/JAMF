#!/usr/bin/python
# Quam Sodji Copyright 2015
# Remove Sophos silently from Mac running any version from 9.0 to 9.2+

import subprocess
import os

version_9_0 = "9.0"
version_9_1 = "9.1"
version_9_2 = "9.2"
try:
    sophos_version = subprocess.check_output("mdls -name kMDItemVersion /Applications/Sophos\ Anti-Virus.app", shell=True)
    sophos_version = sophos_version.strip()
    sophos_version = sophos_version[17:]
    sophos_version = sophos_version[1:]
    sophos_version = sophos_version[:-3]
    if sophos_version == version_9_0:
        os.chdir("/Library/Application Support/Sophos/opm/Installer.app/Contents/MacOS/")
        remove_9_0 = subprocess.check_output(["./InstallationDeployer","--remove"])

    elif sophos_version == version_9_1:
         os.chdir("/Library/Application Support/Sophos/opm/Installer.app/Contents/MacOS/tools/")
         remove_9_1 = subprocess.check_output(["./InstallationDeployer","--remove"])

    elif sophos_version == version_9_2:
        os.chdir("/Library/Application Support/Sophos/opm/Installer.app/Contents/MacOS/tools/")
        remove_9_2 = subprocess.check_output(["./InstallationDeployer","--remove"])
    else:
        print "Found some other version of Sophos labeled : %s" %sophos_version
except:
    print "Sophos not installed"