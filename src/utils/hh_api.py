import json
import requests

from abc import ABC, abstractmethod

URL = 'https://api.hh.ru/vacancies'
FILE = 'data/vacancies.json'


class HhABC(ABC):
    @abstractmethod
    def get_vacancies(self, **kwargs):
        raise NotImplementedError


class HeadHunter(HhABC):
    __slots__ = ['__url', '__file']

    def __init__(self, url=URL, file=FILE):
        self.__url = url
        self.__file = file

    def get_vacancies(self, **kwargs) -> None:
        '''
        Получает вакансии в соответствии с запросом и записывает данные в файл
        '''
        if kwargs:
            self.__url = self.__modify_url(kwargs)

        data = requests.get(self.__url)
        if data.status_code == 200:
            try:
                self.__write_vacancies(data.json())
            except AttributeError as err:
                print(f'An error occurred: {err}')
            else:
                print('Fetch successful')
        else:
            print(f'{self.__url}: Query parameters error')

    def __modify_url(self, kwargs: dict) -> str:
        '''
        Добавляет параметры в запрос
        '''
        url = self.__url + '?'
        for k, v in kwargs.items():
            url += f'{k}={v}&'
        return url

    def __write_vacancies(self, data):
        '''
        Записывает данные в файл
        '''
        with open(self.__file, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)
