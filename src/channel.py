import os
from googleapiclient.discovery import build
import json


class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.info = self.get_channel_info()
        if self.info:
            self.title = self.info['items'][0]['snippet']['title']
            self.description = self.info['items'][0]['snippet']['description']
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.subscriber_count = int(self.info['items'][0]['statistics']['subscriberCount'])
            self.video_count = int(self.info['items'][0]['statistics']['videoCount'])
            self.view_count = int(self.info['items'][0]['statistics']['viewCount'])
        else:
            self.title = None
            self.description = None
            self.url = None
            self.subscriber_count = None
            self.video_count = None
            self.view_count = None

    @classmethod
    def get_service(cls):
        api_key = os.getenv('YOUTUBE_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def get_channel_info(self):
        try:
            youtube = self.get_service()
            request = youtube.channels().list(
                part='snippet,statistics',
                id=self.channel_id
            )
            response = request.execute()
            return response
        except Exception as e:
            print(f"An error occurred while fetching channel info: {e}")
            return None

    def to_json(self, filename):
        data = {
            'id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def save_channel_info(channel_id, filename):
        """
        Метод для сохранения информации о канале в формате JSON
        :param channel_id: ID канала на YouTube
        :param filename: Имя файла для сохранения информации
        """
        os.environ['YOUTUBE_API_KEY'] = 'AIzaSyDwuxvkIC_OTUYnAiBOAsgUDtAEBb6iuug'
        channel = Channel(channel_id)
        channel.to_json(filename)


if __name__ == "__main__":
    # Пример использования класса
    Channel.save_channel_info("UC-lHJZR3Gqxm24_Vd_AJ5Yw", "channel_info.json")

