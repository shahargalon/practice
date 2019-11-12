#!/usr/bin/env python3
##########################
# the script use for add execute permiision to file, receive file_path (arg) from bash
# date: 31/10/19
###########################
import os , stat , sys
###function#####
def add_execute(file_path):
    if os.access(file_path , os.X_OK):     #check if the file has exe permission
        print("the file already have an execute permission")
    else:   
        filestat = os.stat(file_path)      #add exe permission
        os.chmod(file_path , filestat.st_mode | stat.S_IEXEC)
        print("execute permission was added")
################

try:
 file_path = sys.argv[1]          #receive arg from bash
except (IndexError , NameError):
    print("you don't enter a file path, try again")
    sys.exit(0)

add_execute(file_path) #call function



