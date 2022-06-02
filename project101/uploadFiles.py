import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def mainFunction():
    access_token = 'sl.BIwccWzcZB0beXtbyI3q8L9_wHf3eYM4fI8MKScslySD3zWNdcreBx6hoILC59hh-3v-T5AaRC3lC4JS-BcsDtffEXvl1Oh9M83aJ6VD4WhzM1SLvLGfLVLLqSQsnIr1NioeWUc'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("Enter the full path to transfer : - ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
#c:/Users/vishnu/Desktop/VishnuFolder/Whitehat.Jr/Python Whitehat/project98
#/Backup/project98
    transferData.upload_file(file_from,file_to)
    print("Your file has been backed up successfully!")

mainFunction()