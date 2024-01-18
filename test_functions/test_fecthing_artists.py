import json 
data = 'output.json'

with open(data,'r') as data:
    json_data = json.load(data)


song_detail = []
artist_data = []

for record in json_data:
    for track in record.get("items",[]):
        art_info = []
        for artist in track.get("artists",[]):
            a_data = {
                "id": artist.get("id"),
                "name": artist.get("name"),
                "uri": artist.get("uri"),

            }
            art_info.append(a_data)
            artist_data.append(a_data)
            

        song_data = {
            "id" : track.get("id"),
            "name": track.get("name"),
            "duration_ms" : track.get("duration_ms"),
            "artists": art_info,
            "uri": track.get("uri"),
        }
        song_detail.append(song_data)

print(song_detail)
output_file_path = "songdetails_final.json"
with open(output_file_path, "w") as output_file:
    json.dump(song_detail, output_file, indent=2)