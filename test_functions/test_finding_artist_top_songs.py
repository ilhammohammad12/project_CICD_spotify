import json
import requests 
data = "C:/Users/Mohammed Ilham/Documents/DataAnalysis project/Project spotify/songdetails_final.json"

with open(data,'r') as json_file:
    json_data = json.load(json_file)

def allsongs():   
    artistis_information = []    
    for artist in json_data:
        for artisti_info in artist.get('artists'):
            art = {
                "id":artisti_info.get('id'),
                "name":artisti_info.get('name')
                }
            artistis_information.append(art)
    """output = 'artists.json'
    with open(output, "w") as outpust:
        json.dump(artistis_information,outpust, indent=2)"""
    headers = {
            "Authorization": f"Bearer  BQC_zvFQM6oEF_8DhOcI_olH1U_wV3pHZSmt4ucXF_MIF3HvMZZVnrF74gJIIP8y4L-sfY7V14ATGAXrtqHmbgy65a2uf-Mn-q3yZQgJrlv6uu2UWg8",    
            "Content-Type": "application/x-www-form-urlencoded"
        }
    arts_data = []
    for art in artistis_information:
        ids = art.get('id')
        url = 'https://api.spotify.com/v1/artists/'+ids+'/top-tracks?market=IN'
    
        response = requests.get(url,headers=headers)

        if response.status_code == 200:
            artists_output = response.json()
            arts_data.append(artists_output)
        else:
            print("the error in the api call",response.status_code)

    output = 'top_tracks_artists_final.json'
    with open(output, "w") as output_file:
        json.dump(artists_output, output_file, indent=2)
allsongs()