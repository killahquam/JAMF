#setup.py
#!/usr/bin/python
import subprocess
import os
import time
import shutil

"""Configure the pieces for hostname generator"""
#### Modifiable fields ###########
DS_repo_path = '/Users/killah/Desktop/scripts/'


############### Paths ###############

Biplist_url = 'https://bitbucket.org/wooster/biplist'
Repo_file = DS_repo_path + 'Files/'
Temp_folder = DS_repo_path + 'Modules/tmp/'
Module_folder = DS_repo_path + 'Modules/'
Biplist_folder = DS_repo_path + 'Modules/biplist/'
source_file = DS_repo_path + 'Modules/tmp/biplist/biplist/__init__.py'
removal_temp = DS_repo_path + 'Modules/tmp/biplist/'
word_file = DS_repo_path + 'Files/words.txt'
word_List = '/usr/share/dict/words'

#######################################

if os.path.isdir(Repo_file):
    print "Files exists...Skipping"
    pass
else:
    Files = os.mkdir(Repo_file)
    print "Files folder created"
if os.path.isdir(Module_folder):
    print "Modules exists...Skipping"
    pass
else:    
    Modules = os.mkdir(Module_folder)
    print "Modules folder created"
if os.path.isdir(Temp_folder):
    print "tmp exists...Skipping"
    pass
else:
    create_temp = os.mkdir(Temp_folder)
    print "tmp folder created"
if os.path.isdir(Biplist_folder):
    print "Biplist exists...Skipping"
    pass
else:
    create_biplist = os.mkdir(Biplist_folder)
    print "biplist folder created"
if os.path.isfile(word_file):
    os.chmod(word_file,511)
    print "word file exists...Skipping"
    pass
else:
    copy_words = shutil.copy(word_List,word_file)
    print "Word list copied to Files Folder"

change_temp = os.chdir(Temp_folder)
print "Changing Directory"

if os.path.isfile(source_file):
    print "biplist exists...Skipping"
    pass
else:
    print "Downloading biplist from bitbucket Repo"
    download_module = subprocess.Popen(["git", "clone", Biplist_url])
time.sleep(3)

print "Moving biplist to Modules"
file_copy = shutil.copy(source_file,Biplist_folder)
print "Done"
empty_temp = shutil.rmtree(removal_temp)
print "Cleaning up... Done"
print "All done, off you go!"
