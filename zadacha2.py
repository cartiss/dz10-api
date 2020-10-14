import requests
import os
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        #url = 'https://cloud-api.yandex.net/v1/disk/resources/publish'
        url2 = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        file = {'path': file_path}
        headers = {'Authorization': f'OAuth {self.token}', 'Content-Type': 'application/json', 'Accept': 'application/json'}
        get_response = requests.get(url2, params=file, headers=headers)
        put_response = requests.put(get_response.json()['href'], headers=headers, files = {'file': open(os.path.join(os.getcwd(), file_path), 'rb')})
        print(put_response.json())


if __name__ == '__main__':
    uploader = YaUploader('XXXXXXXXXXXXXXXXXXXX')
    uploader.upload('zadacha1.py')