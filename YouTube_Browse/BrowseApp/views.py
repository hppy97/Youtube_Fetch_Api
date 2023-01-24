import requests
import asyncio

from isodate import parse_duration
from django.conf import settings
from asgiref.sync import sync_to_async
from BrowseApp.video.models import Video
from django.shortcuts import render
from django.db.models import Q

#ef index(request):

@sync_to_async
def fetch_data(request):

    t=100;
    while(t):
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
        'part' : 'snippet',
        'q' : request.POST['search'],
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'maxResults' : 9,
        'type' : 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        video_ids = []

        for result in results:
            video_ids.append(result['id']['videoId'])


        video_params = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults' : 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        
        for result in results:
            video_data = Video(
                title = result['snippet']['title'],
                id = result['id'],
                url = f'https://www.youtube.com/watch?v={ result["id"] }',
                duration = int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                upload_time = result['snippet']['publishedAt'],
                thumbnail = result['snippet']['thumbnails']['high']['url']
            )
        video_data.save()

        #videos.append(video_data)

        t=t-1



async def index(request):
    
    
    asyncio.ensure_future(fetch_data(request))
    
    
    item = []
    
    if request.method == 'POST':
        item = Video.objects.filter(
            Q(title__contains=request.POST['search'])
        )

    context = {"videos": item}
    

    return render(request, "browse/index.html", context)
