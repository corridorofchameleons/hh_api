from src.utils.hh_api import HeadHunter
from src.utils.json_crud import JsonManager
from src.utils.vacancy import Vacancy


def get_vacancies():
    j_man = JsonManager()
    hh_api = HeadHunter()

    name = input('Введите ключевое слово: ')
    salary = input('Введите минимальную зарплату: ')
    try:
        salary = int(salary)
    except ValueError:
        salary = 0
    town = input('Введите город (1 - Москва, 2 - Питер): ')
    try:
        town = int(town)
    except ValueError:
        town = 1
    if town != 2:
        town = 1

    vacancies = hh_api.get(text=name, salary=salary, area=town)
    j_man.insert(vacancies)


def add_vacancy():
    j_man = JsonManager()

    name = input('Введите название вакансии: ')
    town = input('Введите город: ')
    salary = input('Введите зарплату: ')
    try:
        salary = int(salary)
    except ValueError:
        salary = 0
    description = input('Введите описание: ')
    requirements = input('Введите требования: ')

    vac = Vacancy.create(name, town, salary, description, requirements)
    j_man.insert(vac)