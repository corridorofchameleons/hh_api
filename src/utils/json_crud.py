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
    def find(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self):
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
            print(data)
        return data

    @staticmethod
    def __write_json(data, file=FILE):
        with open(file, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)

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

    def find(self, name: str | None = None, town: str | None = None,
             salary: int | float | None = None, query: str | None = None) -> list[dict]:
        pass

    def update(self):
        pass

    def delete(self, query):
        pass
