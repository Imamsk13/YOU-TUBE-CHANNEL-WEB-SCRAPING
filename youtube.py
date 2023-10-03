import requests
import pandas as pd
from googleapiclient.discovery import build
from bs4 import BeautifulSoup
from IPython.display import JSON
api_key='AIzaSyCnCk4pJ4UAyZYexcj0gPyHG8qr5v4dt08'
channel_ids=['UCq-Fj5jknLsUf-MWSy4_brA',]


api_service_name = "youtube"
api_version = "v3"
    

    # Get credentials and create an API client
    
youtube = build( api_service_name, api_version, developerKey=api_key)

# request = youtube.channels().list(
#         part="snippet,contentDetails,statistics",
#         id=','.join(channel_ids)
#     )
# response = request.execute()

# # print(response)

def get_channel_stats(youtube, channel_ids):

    all_data =[]

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    response = request.execute()

    for item in response['items']:
        data = {'channelName': item['snippet']['title'],
                'subscribers': item['statistics']['subscriberCount'],
                'views': item['statistics']['viewCount'],
                'Totalvideos': item['statistics']['videoCount'],
                'playlistId': item['contentDetails']['relatedPlaylists']['uploads'],
        }
        
        all_data.append(data)

    return(pd.DataFrame(all_data))

channel_stats=get_channel_stats(youtube, channel_ids)
   
print(channel_stats)

# request = youtube.playlistItems().list(
#     part="snippet,contentDetails",
#     playlistId="UCq-Fj5jknLsUf-MWSy4_brA"
# )
# response = request.execute()

# print(response)




