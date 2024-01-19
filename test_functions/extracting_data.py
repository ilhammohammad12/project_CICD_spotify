import json

with open('album_all_data_final.json','r') as all:
    album_data = json.load(all)
album_details = []
image_details = []
track_all_data =[]
all_data = []
for records_1 in album_data:
    artist_data_ii = []
    for artist_data_1 in records_1['artists']:
        artist = artist_data_1['name']
        artist_data_ii.append(artist)
    for tracks in records_1['tracks']['items']:
        artist_data_iii = []
        for arts in tracks['artists']:
            track_artist = arts['name']
            artist_data_iii.append(track_artist)
        detail_tracks = {
            'name' : tracks['name'],
            'Duration' : tracks['duration_ms'],
            'external_url' : tracks['external_urls'],
            'song_url': tracks['preview_url'],
            'track_artist': artist_data_iii
        }
        track_all_data.append(detail_tracks)
    image_details = {
        'image': records_1['images'][1],
        'name' : records_1['name'],
        'tracks' : records_1['total_tracks'],
        'album_artist' : artist_data_ii,
        'Externalurl' : records_1['external_urls'],
        "track_details" : track_all_data
    }
    all_data.append(image_details)

print(all_data)