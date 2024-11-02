import requests
from bs4 import BeautifulSoup

def get_video_list(user_id):
    url = f'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    
    video_list = []
    for video in soup.find_all('div', class_='l-item'):
        video_title = video.find('a', class_='title').text
        video_url = video.find('a', class_='title')['href']
        video_list.append({'title': video_title, 'url': video_url})
    
    return video_list

user_id = 123456789
videos = get_video_list(user_id)
for video in videos:
    print(video['title'], video['url'])