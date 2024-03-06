import json
from abc import ABC, abstractmethod

from src.settings import FILE
from src.utils.vacancy import Vacancy


class JSONABC(ABC):
    '''
    Абстрактный класс для реализации CRUD
    '''
    @abstractmethod
    def create_table(self):
        raise NotImplementedError

    @abstractmethod
    def insert(self, vacancy):
        raise NotImplementedError

    @abstractmethod
    def select(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, name, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, name):
        raise NotImplementedError


class JsonManager(JSONABC):
    '''
    Класс для работы с JSON
    '''
    def __init__(self):
        pass

    @staticmethod
    def __read_json(file=FILE) -> list[dict]:
        '''
        Получает данные из файла
        '''
        with open(file, encoding='utf8') as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []
        return data

    @staticmethod
    def __write_json(data: list[dict], file=FILE) -> None:
        '''
        Записывает данные в файл
        '''
        with open(file, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)

    @staticmethod
    def __from_dict_to_vacancy(item: dict) -> Vacancy:
        '''
        Преобразует объект dict в объект Vacancy
        '''
        return Vacancy.create(item.get('name'), item.get('town'),
                              item.get('salary'), item.get('description'),
                              item.get('requirements'))

    def create_table(self):
        pass

    def insert(self, vacancies: Vacancy | list[Vacancy]) -> None:
        '''
        Добавляет вакансию (список вакансий) в файл
        '''
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

    def select(self, **kwargs) -> list[Vacancy]:
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
                if param != 'salary' and value.lower() not in vacancy.get(param).lower():
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
        '''
        Удаляет из файла вакансию с заданным названием
        '''
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
        '''
        Возвращает топ вакансий по зарплате
        '''
        if not num:
            num = len(vacancies)

        return sorted(vacancies, reverse=True)[:num]
