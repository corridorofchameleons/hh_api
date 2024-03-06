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
    def delete(self, name):
        raise NotImplementedError

    @abstractmethod
    def top_salary(self, vacancies, num):
        raise NotImplementedError


class JsonManager(JSONABC):
    def __init__(self):
        pass

    @staticmethod
    def __read_json(file=FILE):
        with open(file, encoding='utf8') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []
        return data

    @staticmethod
    def __write_json(data, file=FILE):
        with open(file, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)

    @staticmethod
    def __from_dict_to_vacancy(item: dict) -> Vacancy:
        return Vacancy.create(item.get('name'), item.get('town'),
                              item.get('salary'), item.get('description'),
                              item.get('requirements'))

    def add(self, vacancies: Vacancy | list[Vacancy]) -> None:
        if isinstance(vacancies, Vacancy):
            vacancies = [vacancies]
        records = self.__read_json()
        if not records:
            records = []

        for vacancy in vacancies:
            new = {'name': vacancy.name,
                   'town': vacancy.town,
                   'salary': vacancy.salary,
                   'description': vacancy.description,
                   'requirements': vacancy.requirements
                   }
            records.append(new)

        self.__write_json(records)
        print('Вакансии успешно добавлены')

    def search(self, **kwargs) -> list[Vacancy]:
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
                result.append(self.__from_dict_to_vacancy(vacancy))

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
        print('Вакансия обновлена')

    def delete(self, name):
        vacancies = self.__read_json()
        if name == 'all':
            vacancies = []
        else:
            for vacancy in vacancies:
                if vacancy.get('name') == name:
                    vacancies.remove(vacancy)

        self.__write_json(vacancies)
        print('Вакансия удалена')

    def top_salary(self, vacancies: list[Vacancy], num: int = None) -> list[Vacancy]:
        if not num:
            num = len(vacancies)

        return sorted(vacancies, reverse=True)[:num]
