#!/usr/bin/env python
from dropbox.files import WriteMode
import dropbox
access_token = 'Gip3hzPfydAAAAAAAAAAAXNfpXAraqEHz5EjC7IgOrjQGp7_TIYxLGwt5VfyKf4W'
file_from = '/home/danilo/teste.txt'  
file_to = '/home/danilo/teste.txt' 
def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    #dbx.files_delete_v2(file_to)
    dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite, autorename=False, mute=False, strict_conflict=False)
upload_file(file_from,file_to)


