import requests
import json
def make_api_request():

    """url = "https://api.spotify.com/v1/search?q=top+songs+2023+india&type=album&market=IN&limit=50&offset=10"
    

    headers = {
    "Authorization": f"Bearer {access_token}",    
    "Content-Type": "application/x-www-form-urlencoded"
    }
    print("received request to get search data")
    response = requests.get(url,headers=headers)"""
    with open('C:/Users/Mohammed Ilham/Documents/DataAnalysis project/Project spotify/test_functions/test.json', 'r') as outputfile:
        data = json.load(outputfile)
    
    album_list_info = []
    
    for records in data['albums']['items']:
        #print(records)
        artist = []
        for artists in records['artists']:
            arts_info = {
                #'artist_name' : artists['name'],
                'artist_id': artists['id'],
                #'external_url' : artists['external_urls']['spotify']
            }
            artist.append(arts_info)
        album_info = {
            'name' : records['name'],
            #'images' : records['images'][1],
            'uri' : records['uri'],
            'artistinfo' : artist
        }
        album_list_info.append(album_info)
    print(album_list_info)
"""    output_filepath = 'search_data.json'
    with open(output_filepath,'w') as output_data:
        json.dump(album_list_info,output_data, indent=2)
        print('done')"""
    
"""   if response.status_code == 200:
        data = response.json()
        for record in data['albums']['items']:
            print(record)
            album_info = {
            "name": record["name"],
            "release_date": record["release_date"],
            "uri": record["uri"]
                    }
            album_list_info.append(album_info)
        print(album_list_info)
        print("completed request to get search data")
        return album_list_info
    else:
        print("API Request Failed. Status Code:", response.status_code)
        print("Trigerring the regenerate token call")"""

#make_api_request("BQCSKQnM5HjjZ-kB7Rxr4FrhDwjoRniiov-pP1NCff0qSZOPr0ZkMdft43a1dZ4DdHTuY2QxFYNWUGECefzFCg6QtdBEs1Ug5LbwZMt8lVOaalLbX3E")

make_api_request()