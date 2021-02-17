import requests
from pprint import pprint


class YandexMap:
    def __init__(self, centercoords, scale):
        self.api_server = 'http://static-maps.yandex.ru/1.x/'
        self.centercoords = centercoords
        self.scale = scale
        self.type = 'map'
        self.points = []

    def get_map(self):
        params = {'ll': ','.join([str(i) for i in self.centercoords]),
                  'spn': ','.join([str(i) for i in self.scale]),
                  'l': self.type}

        for i in self.points:
            point = ','.join([str(j) for j in i]) + ',org'
            if 'pt' not in params:
                params['pt'] = point
            else:
                params['pt'] += '~' + point
        response = requests.get(self.api_server, params=params)
        return response.content

    def set_centercoords(self, centercoords):
        self.centercoords = centercoords

    def set_scale(self, scale):
        if 0.1 < scale[0] <= 15 and 0.1 < scale[1] <= 15:
            self.scale = scale

    def change_type(self, type):
        self.type = type

    def find_object(self, toponym_to_find):
        geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}

        response = requests.get(geocoder_api_server, params=geocoder_params)
        # Преобразуем ответ в json-объект
        json_response = response.json()
        # Получаем первый топоним из ответа геокодера.
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]

        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]

        # получаем адрес и почтовый код по координатам
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": ','.join(toponym_coodrinates.split()),
            "format": "json"}

        address = requests.get(geocoder_api_server, params=geocoder_params).json()
        address = address['response']['GeoObjectCollection']['featureMember'][0]['GeoObject'][
            'metaDataProperty']['GeocoderMetaData']['Address']\

        # координаты у нас есть всегда, но вот адреса или почтового кода может не быть
        res = [toponym_coodrinates]

        if 'formatted' in address:
            res.append(address['formatted'])
        else:
            res.append('')

        if 'postal_code' in address:
            res.append(address['postal_code'])
        else:
            res.append('')

        return res

    def add_point(self, coords):
        self.points.append(coords)

    def clear_points(self):
        self.points = []
