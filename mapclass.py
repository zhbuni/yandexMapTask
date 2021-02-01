import requests
from io import BytesIO


class YandexMap:
    def __init__(self):
        self.api_server = 'http://static-maps.yandex.ru/1.x/'

    def get_map(self, coords, scale):
        params = {'ll': ','.join([str(i) for i in coords]),
                 'spn': ','.join([str(i) for i in scale]),
                 'l': 'map'}
        response = requests.get(self.api_server, params=params)
        return BytesIO(response.content)
