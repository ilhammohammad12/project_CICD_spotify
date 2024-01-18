import json

data = 'C:/Users/Mohammed Ilham/Documents/DataAnalysis project/Project spotify/spotify/top_tracks_artists_final.json'

with open(data,'r') as f:
    data =json.load(f)
arsts = [] 
artsts = []
for track in data['tracks']:
    #print(track['album']['artists'])
    for artist in track['album']['artists']:
        
        artistname = {
            'name' : artist['name']
        }
        artsts.append(artistname)
    artis = {
        'name' : track['album']['name'],
        'image' : track['album']['images'][0],
        'artistname' : artsts

    }
    arsts.append(artis)

print(arsts)
