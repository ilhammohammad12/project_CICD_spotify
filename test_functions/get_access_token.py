import requests
import json 
def generate_token():
    url = "https://accounts.spotify.com/api/token"

    client_id = "f4f8554077e84dc8a5fd740ea419bff8"
    client_secret = "afe443f1d33e46d6bbad9a7a319b4397"
    grant_type = "client_credentials"

    data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret
           }   

    headers = {
    "Content-Type": "application/x-www-form-urlencoded"
            }
    print('Recived client request to generate token')
    print("starting request to generate client token")
    response = requests.post(url, data=data, headers=headers)
    print("completed client request")
    if response.status_code == 200:
        print("status sucess",response.status_code)
        access_token = response.json().get("access_token")
        print("access token is generated")
        filepath = 'access_token.json'
        with open(filepath, "w") as json_file:
            json.dump(access_token,json_file, indent=2)
            print("completed handling saved the request")
            
    else:
        print("Error:", response.status_code, response.text)
    
generate_token()