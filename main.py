from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes for read-only access to Google Photos
SCOPES = ['https://www.googleapis.com/auth/photoslibrary.readonly']

def authenticate_google_photos():
    """Authenticate the user and return a Google Photos service object."""
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    service = build('photoslibrary', 'v1', credentials=credentials)
    return service

def list_photos(service):
    """List the user's first 10 media items."""
    results = service.mediaItems().list(pageSize=10).execute()
    items = results.get('mediaItems', [])
    if not items:
        print('No media items found.')
    else:
        for item in items:
            print(f"Filename: {item['filename']}, Creation Time: {item['mediaMetadata']['creationTime']}")

if __name__ == '__main__':
    # Authenticate and get service
    service = authenticate_google_photos()
    # List media items
    list_photos(service)
