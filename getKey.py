import requests
from dotenv import load_dotenv
import os


keyMap = {-1: None, 0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}

def getTrackKey(track_id):
    endpoint = 'https://api.spotify.com/v1/audio-features/' + track_id
    headers = {"Authorization": "Bearer " + getAPIKey()}
    response = requests.get(endpoint,headers=headers)
    if response.status_code == 200:
        return keyMap[response.json()['key']]
    else:
        return keyMap[-1]


def getTrackId(trackName):
    pass

def getAPIKey():
    load_dotenv()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    endpoint = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    
    print(client_id)
    print(client_secret)

    response = requests.post(endpoint, data=data)

    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None
        
    
def main():
    print(getTrackKey('4SgcE7RxpK3ydWrjoAQH1K'))

if __name__ == "__main__":
    main()
    
###
# 4SgcE7RxpK3ydWrjoAQH1K
# 
# ###

