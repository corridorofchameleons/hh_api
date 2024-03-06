import requests

from abc import ABC, abstractmethod
from src.utils.vacancy import Vacancy
from src.settings import URL


class HhABC(ABC):
    @abstractmethod
    def get(self, **kwargs):
        raise NotImplementedError

    def post(self, **kwargs):
        raise NotImplementedError

    def put(self, **kwargs):
        raise NotImplementedError

    def delete(self, **kwargs):
        raise NotImplementedError


class HeadHunter(HhABC):
    '''
    Класс для отправки запросов
    '''
    __slots__ = ['__url', '__file']

    def __init__(self, url=URL):
        self.__url = url

    def __modify_url(self, kwargs: dict) -> str:
        '''
        Добавляет параметры в запрос
        '''
        url = self.__url + '?'
        for k, v in kwargs.items():
            if k == 'per_page' and v > 50:
                v = 50
            url += f'{k}={v}&'
        return url

    @staticmethod
    def __create_vacancy(item):
        '''
        Извлекает данные вакансии в соответствии со структурой класса Vacancy
        Возвращает экземпляр класса Vacancy
        '''

        name = item.get('name')

        try:
            town = item.get('area').get('name')
        except AttributeError:
            town = None

        try:
            salary = item.get('salary').get('from')
        except AttributeError:
            salary = 0

        try:
            description = item.get('snippet').get('responsibility')
        except AttributeError:
            description = None

        try:
            requirements = item.get('snippet').get('requirements')
        except AttributeError:
            requirements = None

        vacancy = Vacancy.create(name, town, salary, description, requirements)

        return vacancy

    def get(self, **kwargs) -> list[Vacancy]:
        '''
        Получает вакансии в соответствии с запросом
        Возвращает список объектов Vacancy
        '''
        result = []
        if kwargs:
            self.__url = self.__modify_url(kwargs)

        data = requests.get(self.__url)
        if data.status_code == 200:
            try:
                for item in data.json().get('items'):
                    vacancy = self.__create_vacancy(item)
                    result.append(vacancy)
            except AttributeError as err:
                print(f'An error occurred: {err}\n')
            else:
                print('Вакансии получены\n')
        else:
            print(f'{self.__url}: Query parameters error\n')

        return result

    def post(self, **kwargs):
        pass

    def put(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
