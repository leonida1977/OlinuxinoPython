#!/usr/bin/python
__author__ = 'daniele'

import sys
import time
import select
import paramiko

# ssh
print("enter ssh")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # this will automatically add the keys
ssh.connect("192.168.2.108", username="root", password="powerdna")
# Run your commands
# example 1 : ls command
print("do a ls command")
try:
    (stdin, stdout, stderr) = ssh.exec_command("ls & cd tmp")
except:
   print("whoops")
   sys.exit()
print(stdout.readlines())
time.sleep(2)

ssh.close()

