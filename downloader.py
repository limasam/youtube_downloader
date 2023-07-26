from pytube import YouTube

def download_video(url, output_path=None):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()  # Выбираем наивысшее разрешение
        video_title = yt.title

        if output_path is None:
            output_path = video_title + ".mp4"

        print(f"Загрузка видео: {video_title}")
        video_stream.download(output_path)
        print("Скачивание завершено.")
    except Exception as e:
        print(f"Ошибка при скачивании видео: {e}")

if __name__ == "__main__":
    url = input("Введите URL видео на YouTube: ")
    download_video(url)
