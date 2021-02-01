import requests
from io import BytesIO


class YandexMap:
    def __init__(self, centercoords, scale):
        self.api_server = 'http://static-maps.yandex.ru/1.x/'
        self.centercoords = centercoords
        self.scale = scale


    def get_map(self):
        params = {'ll': ','.join([str(i) for i in self.centercoords]),
                 'spn': ','.join([str(i) for i in self.scale]),
                 'l': 'map',
                  'size':'800,800'}

        response = requests.get(self.api_server, params=params)
        return BytesIO(response.content)

    def set_centercoords(self, centercoords):
        self.centercoords = centercoords

    def set_scale(self, scale):
        self.scale = scale