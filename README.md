# Youtube Search API

## Project Goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

The server fetches latest videos async after every 10 minutes and saves it to the db.

## Project Detail

- I utilized the power of Django to bring this project to life, utilizing the latest asynchronous views for optimal performance. 
- To organize the project, I created an "YouTube_Browse" app within the Django project, and within that app, I enabled the use of the latest async features in Django.
- Additionally, I crafted a model for "videos" that includes a GET API, allowing for easy retrieval of stored video data sorted by the published date and  time in descending order.

## Screenshots
![Screenshot 2023-01-23 at 10 30 00 PM](https://user-images.githubusercontent.com/41753714/214291144-956bbfcb-b824-4f5c-8f41-459a1665fcb3.png)
![Screenshot 2023-01-23 at 10 30 33 PM](https://user-images.githubusercontent.com/41753714/214291255-36b50a41-b646-412c-ba2a-5a1ea41344f5.png)


### Reference:

- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)
    - To fetch the latest videos you need to specify these: type=video, order=date, publishedAfter=<SOME_DATE_TIME>
    - Without publishedAfter, it will give you cached results which will be too old
