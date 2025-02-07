from django.shortcuts import render
import json

def track_list(request):
    with open('/app/output_jsons/songdetails_final.json') as f:
        data = json.load(f)
        artists = []

        for track_data in data:
            artist_names = [artist['name'] for artist in track_data['artists']]
            artisit_info = {
                "name": track_data['name'],
                'artists': artist_names

            }
            artists.append(artisit_info)
    return render(request, 'track_list.html', {'artists': artists})

def artistic_top_tracks(request):
    with open('/app/output_jsons/all_songs_json.json') as file:
        datas = json.load(file)
        arsts = []
        for track in datas['tracks']:
            artsts = []
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
    return render(request, 'arts.html', {'artists':arsts})

"""def search_albums(request):
    with open(' spotify/spotify/search_data.json', 'r') as searchdata:
        search_album_data = json.load(searchdata)
        
    return render(request,'search_data.html',{'playlist_data':search_album_data})
        """
from django.shortcuts import render

def playlist_detail(request):
    with open('/app/output_jsons/search_data.json', 'r') as outputfile:
        data = json.load(outputfile)
    
    album_list_info = []
    
    for records in data['albums']['items']:
        artist = []
        for artists in records['artists']:
            arts_info = {
                'artist_name' : artists['name'],
                'id': artists['id'],
                'external_url' : artists['external_urls']['spotify']
            }
            artist.append(arts_info)
        album_info = {
            'name' : records['name'],
            'images' : records['images'][1],
            'uri' : records['uri'],
            'artistinfo' : artist
        }
        album_list_info.append(album_info)
         
    return render(request, 'playlist_detail.html', {'playlist_data': album_list_info})

def all_album_tracks(request):
    with open('/app/output_jsons/album_all_data_final.json','r') as all:
        album_data = json.load(all)
    album_details = []
    image_details = []
    
    all_data = []
    for records_1 in album_data:
        track_all_data =[]
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
    return render(request, 'all_album_template.html', {'all_data': all_data})
    
