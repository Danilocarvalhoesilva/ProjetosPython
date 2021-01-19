import subprocess
import os

SOURCE_DIR="/root/"
BACKUP_DIR="/mnt/data/backups"

"""
#subprocess.call(["rsync", "-avP", "SOURCE_DIR", "--exclude", ".cache", "--exclude", ".*", "BACKUP_DIR"])

os.system('rsync -avP SOURCE_DIR --exclude ".cache" --exclude ".*" BACKUP_DIR')

import rsync

if __name__ == '__main__':
    rsync.file('/root', '/mnt/data/backups')
"""

import time

date =  time.strftime("%Y-%m-%d")

def createBkpFull():
        bkp = 'rsync -avP %s --exclude ".cache" --exclude ".*" %s' %(SOURCE_DIR,BACKUP_DIR)
        print(bkp)
        return bkp

def createLog():
        logFile = '%s-bkp-incremental.txt' % date
        pathLog = '/var/log/%s' % logFile
        return pathLog
