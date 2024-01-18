import json

with open('C:/Users/Mohammed Ilham/Documents/DataAnalysis project/Project spotify/spotify/tracks/all_songs_json.json') as f:
    data = json.load(f)
    tracks = data['tracks']
