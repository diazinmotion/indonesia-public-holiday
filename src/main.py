from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime
import json
import os.path
import sys

SCOPES = ['https://www.googleapis.com/auth/calendar.events.readonly']
SERVICE_ACCOUNT_FILE = 'google-service-account.json'

def main():
    result = []

    if sys.argv[1] == '--help':
        print('Hari Libur Indonesia (Sumber Google Calendar API)')
        print('main.py <empat digit tahun>')
        exit()
    else:
        year = datetime.today().year if not sys.argv[1] else int(sys.argv[1])

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)

    startDate = datetime(year, 1, 1).isoformat() + 'Z'
    maxDate = datetime(year, 12, 31).isoformat() + 'Z'

    events_result = service.events().list(
        calendarId='id.indonesian#holiday@group.v.calendar.google.com',
        timeMin=startDate,
        timeMax=maxDate,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')

    for event in events:
        nama = event['summary']
        tggl = event['start'].get('date')
        status = event['status']
        
        if 'Diwali' in nama:
            continue

        data_temp = {
            'tanggal': tggl,
            'nama_hari': nama,
            'status': True if (status == 'confirmed') else False
        }
        result.append(data_temp)

    if not os.path.exists(os.path.join(os.getcwd(), "dist")):
        try:
            os.makedirs(os.path.join(os.getcwd(), "dist"))
        except:
            pass
    
    with open(os.path.join(os.getcwd(), "dist", "indo_pub_holiday_{}.json".format(year)), "w") as write_file:
        json.dump({'results': result}, write_file)


if __name__ == '__main__':
    main()