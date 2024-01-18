from django.shortcuts import render
import json

def track_list(request):
    with open('C:/Users/Mohammed Ilham/Documents/DataAnalysis project/Project spotify/output_jsons/songdetails_final.json') as f:
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
    with open('C:/Users/Mohammed Ilham/Documents/DataAnalysis project/Project spotify/output_jsons/all_songs_json.json') as file:
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
    with open('C:/Users/Mohammed Ilham/Documents/DataAnalysis project/Project spotify/spotify/search_data.json', 'r') as searchdata:
        search_album_data = json.load(searchdata)
        
    return render(request,'search_data.html',{'playlist_data':search_album_data})
        """
from django.shortcuts import render

def playlist_detail(request):
    with open('C:/Users/Mohammed Ilham/Documents/DataAnalysis project/Project spotify/test_functions/test.json', 'r') as outputfile:
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
