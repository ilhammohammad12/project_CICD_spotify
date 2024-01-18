import re
import requests
import json 
data = [{
        'name': 'New Hit Songs Of 2023 Playlist Instrumentals',
        'uri': 'spotify:album:3fZ1aGbIF6Mtj6n3HYBqZJ',
        'artistinfo': [{
                'artist_id': '1najORT7ZKHSbaGiAfW8ct'
            }, {
                'artist_id': '3Rt4qtMRPzdBLU2cU1Q5aO'
            }, {
                'artist_id': '4OxfghTTEa7wIa1GcXtWVD'
            }
        ]
    }, {
        'name': 'New Global Pop Hits 2023 | Hot Hits International',
        'uri': 'spotify:album:0FB4HsrHZCx39ajuAyok8o',
        'artistinfo': [{
                'artist_id': '0LyfQWJT6nXafLPZqxe9Of'
            }
        ]
    }, {
        'name': 'Top Billboard Songs Of 2023',
        'uri': 'spotify:album:4nxYa4l1OZ0ZbQI6IqVy2q',
        'artistinfo': [{
                'artist_id': '4OxfghTTEa7wIa1GcXtWVD'
            }, {
                'artist_id': '1najORT7ZKHSbaGiAfW8ct'
            }, {
                'artist_id': '3Rt4qtMRPzdBLU2cU1Q5aO'
            }
        ]
    }, {
        'name': 'Trending Now Hindi â€“ Top Songs India (Love, Sadness, Bolly Wood, Movies OST)',
        'uri': 'spotify:album:77WGJcdFOAtDRGimkO77se',
        'artistinfo': [{
                'artist_id': '0fdpSsYQvHfaNCNW9nWd2d'
            }, {
                'artist_id': '006E9y7AizqWR01oRWagrY'
            }, {
                'artist_id': '74kd8l3AEfk5YHYYbnl2fV'
            }
        ]
    }, {
        'name': 'Indie Hits',
        'uri': 'spotify:album:0GlSLkCH8JGN5SEHI5fP5V',
        'artistinfo': [{
                'artist_id': '0LyfQWJT6nXafLPZqxe9Of'
            }
        ]
    }, {
        'name': 'Top 20 Most Viewed Songs Of The Decade (2010-2019)',
        'uri': 'spotify:album:1T96ULZl0RFzkAAiFEMonG',
        'artistinfo': [{
                'artist_id': '0LyfQWJT6nXafLPZqxe9Of'
            }
        ]
    }, {
        'name': 'Trending Songs 2021',
        'uri': 'spotify:album:1SbBh0wMxNNxqD59cN6L6u',
        'artistinfo': [{
                'artist_id': '0LyfQWJT6nXafLPZqxe9Of'
            }
        ]
    }, {
        'name': 'Top Songs Of 2024',
        'uri': 'spotify:album:1rAboACrVvBUkQdc0tUv5R',
        'artistinfo': [{
                'artist_id': '6UE1TvbbosOhY8SFGp2B0n'
            }, {
                'artist_id': '173A1DNdClvMfxvlfW4ncW'
            }, {
                'artist_id': '2lY7IRyiaIDfNxgIhU5Mvt'
            }
        ]
    }, {
        'name': 'Bollywood Trap Mix',
        'uri': 'spotify:album:0qcvMU9wm0F5HvH1YVQWYy',
        'artistinfo': [{
                'artist_id': '0LyfQWJT6nXafLPZqxe9Of'
            }
        ]
    }, {
        'name': 'Viral Hits: August 2023',
        'uri': 'spotify:album:55r5w2Rv1NjipfrtSH1kYb',
        'artistinfo': [{
                'artist_id': '0LyfQWJT6nXafLPZqxe9Of'
            }
        ]
    }, {
        'name': '2023 Hit Songs Playlist Music Radio Mix',
        'uri': 'spotify:album:3em8fAvdK5h7tr7jf6wyAM',
        'artistinfo': [{
                'artist_id': '6MGnOdzzXNoGcUgfxMcSwA'
            }, {
                'artist_id': '7haeSqCyAAF7Zw5XRAllvJ'
            }
        ]
    }, {
        'name': '#1 Trending Hits',
        'uri': 'spotify:album:2dItXypmeMVli42NpaHWbN',
        'artistinfo': [{
                'artist_id': '0LyfQWJT6nXafLPZqxe9Of'
            }
        ]
    }, {
        'name': 'Top Hits Today Top Hits Music Playlist 2023',
        'uri': 'spotify:album:4FVQ5bT83zpxtQyVZNQ5NW',
        'artistinfo': [{
                'artist_id': '6MGnOdzzXNoGcUgfxMcSwA'
            }, {
                'artist_id': '7haeSqCyAAF7Zw5XRAllvJ'
            }
        ]
    }, {
        'name': 'Top Hit Songs Of 2023',
        'uri': 'spotify:album:2L6pvTyUQzCtkkRXhOI0yR',
        'artistinfo': [{
                'artist_id': '6MGnOdzzXNoGcUgfxMcSwA'
            }, {
                'artist_id': '7haeSqCyAAF7Zw5XRAllvJ'
            }
        ]
    }, {
        'name': 'New Hit Songs Of 2023 Playlist Instrumental Music',
        'uri': 'spotify:album:3UFvEdbw8RA4gkX6cMKjNA',
        'artistinfo': [{
                'artist_id': '7qgJkqICsYsUtU8a5SwG9b'
            }, {
                'artist_id': '50KjEpBOQcIEWa0sOi0sji'
            }, {
                'artist_id': '4WIRa3FZcayVSVSPOcmVti'
            }
        ]
    }, {
        'name': 'Top Hits Radio 2023',
        'uri': 'spotify:album:5BofEHArDx10Crph9L7ZXH',
        'artistinfo': [{
                'artist_id': '4WIRa3FZcayVSVSPOcmVti'
            }, {
                'artist_id': '50KjEpBOQcIEWa0sOi0sji'
            }, {
                'artist_id': '7qgJkqICsYsUtU8a5SwG9b'
            }
        ]
    }, {
        'name': 'New Hit Songs Of 2023',
        'uri': 'spotify:album:1hnrCSPSJLUtWZeMYl9zAt',
        'artistinfo': [{
                'artist_id': '6hhgyoKVX6lJl3hdeivtU4'
            }, {
                'artist_id': '3h34J1AiEBRK4XvTqvEam0'
            }, {
                'artist_id': '2CjbvYSZpd7wCTsaovnjNB'
            }
        ]
    }, {
        'name': 'Best Hits Year End 2023',
        'uri': 'spotify:album:61017tFezEY4XDyWtGN1SD',
        'artistinfo': [{
                'artist_id': '7qgJkqICsYsUtU8a5SwG9b'
            }, {
                'artist_id': '50KjEpBOQcIEWa0sOi0sji'
            }, {
                'artist_id': '4WIRa3FZcayVSVSPOcmVti'
            }
        ]
    }, {
        'name': 'Top Trending Hits Vol.5',
        'uri': 'spotify:album:1kviuKCn7SaRHnUlaqfbfV',
        'artistinfo': [{
                'artist_id': '0LyfQWJT6nXafLPZqxe9Of'
            }
        ]
    }, {
        'name': '2020 Indian Restaurant: Relaxing Background Music from India',
        'uri': 'spotify:album:2FPO1BH6IV9BKgXwdDqpRp',
        'artistinfo': [{
                'artist_id': '1hUujSRQatoporxnDDKs1W'
            }
        ]
    }
]

uris = []
complete_data = []
artist_id = []
for records in data:
    pulling_uri = records['uri']
    for artistic in records['artistinfo']:
        artist_id.append(artistic.get('artist_id'))
    uri = re.search(r":([^:]+)$", pulling_uri)
    uri_full = uri.group(1)
    uris.append(uri_full)

for uri in uris:
    #print(uri)
    urls = "https://api.spotify.com/v1/albums/"+uri+"/tracks?market=IN&limit=50"
    headers = {
    "Authorization": f"Bearer  BQBqn3E3k9aqmU74MHOx0AWmo7pF-LrUFB2ovIm93S09hJ5-ne46qI9ndGOFpsfCjikyRrn5ql9eCS-z-_d9QiVzmNHoaR6LG-7M35cpPBaAW8d-BKQ",    
    "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.get(urls,headers=headers)

    if response.status_code == 200:
        data = response.json()
        complete_data.append(data)
    else:
        print(response.status_code)

output_file_path = "album_list_tracks_final.json"
with open(output_file_path, "w") as output_file:
    json.dump(complete_data, output_file, indent=2)