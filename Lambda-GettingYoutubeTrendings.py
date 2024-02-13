from dotenv import load_dotenv
import os
import json
from googleapiclient.discovery import build
from datetime import datetime
import unicodedata

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Defina suas credenciais da API do YouTube
DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
"AIzaSyA34Y_jgiRwdQrZo_zyMNjKsrPBDc5vtis"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Defina o país para o qual você deseja buscar os vídeos em tendência (BR para Brasil)
REGION_CODE = "BR"

# def normalize_text(text):
#     """
#     Função para normalizar texto removendo diacríticos e convertendo para UTF-8.
#     """
#     normalized_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
#     return normalized_text

def get_trending_videos():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    trending_videos = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        chart="mostPopular",
        regionCode=REGION_CODE,
        maxResults=10
    ).execute()

    trending_videos_list = []

    for video in trending_videos['items']:
        video_id = video['id']
        title = normalize_text(video['snippet']['title'])
        duration = video['contentDetails']['duration']
        channel_id = video['snippet']['channelId']
        likes = video['statistics']['likeCount']
        # dislikes = video['statistics']['dislikeCount']
        shares = video['statistics'].get('shareCount', 0)
        published_at = datetime.strptime(video['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
        # tags = [normalize_text(tag) for tag in video['snippet'].get('tags', [])]

        video_data = {
            'video_id': video_id,
            'title': title,
            'duration': duration,
            'channel_id': channel_id,
            'likes': likes,
            'shares': shares,
             'tags': tags,
            'published_at': published_at
        }
        trending_videos_list.append(video_data)

    return trending_videos_list

if __name__ == "__main__":
    # Chame a função para obter os 10 vídeos mais populares do YouTube no Brasil
    trending_videos = get_trending_videos()

    # Imprima os resultados
    print(json.dumps(trending_videos, indent=4))
