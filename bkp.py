#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import subprocess
from subprocess import Popen


SOURCE_DIR="/root/"
BACKUP_DIR="/mnt/data/backups"

date =  time.strftime("%d-%m-%Y")
command = 'rsync -avP %s --exclude "default.*" --exclude ".cache" --exclude ".*" %s' %(SOURCE_DIR,BACKUP_DIR)

logFile = '%s-sync-incremental.txt' % date
LOG = '/var/log/%s' % logFile

def registerLog(startTime, command, LOG):
    date = (time.strftime('%d-%m-%Y'))
    r = open(LOG,"w+")
    log_message = 'LOG REGISTRADO\nDATA: %s\nHORA INICIO: %s\nARQUIVOS SICRONIZADO: %s\n' % (date,startTime,command)
    r.write(log_message)
    r.close()

def full():
    startTime =  time.strftime("%H:%M:%S")
    log = ' >> %s' % LOG
    #out = subprocess.call([BKP + log], shell=True)
    p = subprocess.Popen([command + log], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.communicate()
    print(output)
    registerLog(startTime, command, LOG)

full() 

