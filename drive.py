from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import os

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

fid = '1M-EOkIvZEt7JMsorXwwYvKoFWypUKs4S'

path = os.path.abspath('.')

file_metadata = {
    'name': "vscode.zip",
    "kind": "drive#file",
}
media = MediaFileUpload(path+"/vscode.zip", mimetype='application/zip')

service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
).execute()