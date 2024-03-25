import os
from src.channel import Channel

if __name__ == '__main__':
    # Установите API ключ в переменные среды
    os.environ['YOUTUBE_API_KEY'] = 'AIzaSyDwuxvkIC_OTUYnAiBOAsgUDtAEBb6iuug'

    # ID канала, информацию о котором вы хотите получить
    channel_id = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'  # Замените на ваш канал

    # Создайте объект Channel и получите информацию о канале
    channel = Channel(channel_id)

    # Выведите информацию о канале в консоль
    print(f"Название канала: {channel.title}")
    print(f"Описание канала: {channel.description}")
    print(f"Количество подписчиков: {channel.subscriber_count}")
    print(f"Количество видео: {channel.video_count}")
    print(f"Общее количество просмотров: {channel.view_count}")

    # Сохраните информацию о канале в JSON файл
    channel.to_json('channel_info.json')
