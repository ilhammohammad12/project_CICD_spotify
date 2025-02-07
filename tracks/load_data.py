import json

with open('/app/tracks/all_songs_json.json') as f:
    data = json.load(f)
    tracks = data['tracks']
