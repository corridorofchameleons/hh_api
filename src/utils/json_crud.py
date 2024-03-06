import json
from abc import ABC, abstractmethod

from src.settings import FILE
from src.utils.vacancy import Vacancy


class JSONABC(ABC):
    '''
    Абстрактный класс для реализации CRUD
    '''
    @abstractmethod
    def add(self, vacancy):
        raise NotImplementedError

    @abstractmethod
    def search(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, name, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, query):
        raise NotImplementedError


class JsonManager(JSONABC):
    def __init__(self):
        pass

    @staticmethod
    def __read_json(file=FILE):
        with open(file, 'r', encoding='utf8') as f:
            data = json.load(f)
        return data

    @staticmethod
    def __write_json(data, file=FILE):
        with open(file, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)

    @staticmethod
    def __search_target(name: str, vacancies: list[dict]) -> dict:
        target = None
        for vacancy in vacancies:
            if vacancy.get('name') == name:
                target = vacancy
                del vacancy
        return target

    def add(self, vacancy: Vacancy) -> None:
        vacancies = self.__read_json()

        new = {'name': vacancy.name,
               'town': vacancy.town,
               'salary': vacancy.salary,
               'description': vacancy.description,
               'requirements': vacancy.requirements
               }
        vacancies.append(new)

        self.__write_json(vacancies)

    def search(self, **kwargs) -> list[dict]:
        '''
        Возвращает список вакансий, удовлетворяющих заданным требованиям
        '''
        result = []
        vacancies = self.__read_json()

        for vacancy in vacancies:
            suitable = True
            for param, value in kwargs.items():

                if param == 'salary' and int(value) > int(vacancy.get('salary')):
                    suitable = False
                if param != 'salary' and value not in vacancy.get(param).lower():
                    suitable = False
            if suitable:
                result.append(vacancy)

        return result

    def update(self, name: str, **kwargs) -> None:
        '''
        Обновляет данные вакансии
        '''
        vacancies = self.__read_json()
        for vacancy in vacancies:
            if vacancy.get('name') == name:
                for k, v in kwargs.items():
                    vacancy[k] = v

        self.__write_json(vacancies)

    def delete(self, name):
        vacancies = self.__read_json()
        for vacancy in vacancies:
            if vacancy.get('name') == name:
                vacancies.remove(vacancy)
        print(vacancies)
        self.__write_json(vacancies)
