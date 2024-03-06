from src.utils.json_crud import JsonManager


def select_vacancies():
    j_man = JsonManager()

    name = input('Название (Enter - пропустить): ')
    salary = input('Минимальная зарплата (Enter - пропустить): ')
    try:
        salary = int(salary)
    except ValueError:
        salary = 0
    town = input('Город (Enter - пропустить): ')

    return j_man.select(name=name, salary=salary, town=town)


def top_vacancies():
    j_man = JsonManager()

    num = input('Сколько выгружаем?\n')
    vacancies = j_man.select()
    try:
        num = int(num)
    except ValueError:
        num = None

    return j_man.top_salary(vacancies, num)


def update_vacancy():
    j_man = JsonManager()

    name = input('Введите название вакансии: ')
    salary = input('Введите новую зарплату: ')
    try:
        salary = int(salary)
    except ValueError:
        salary = 0

    j_man.update(name, salary=salary)


def delete_vacancy():
    j_man = JsonManager()

    name = input('Введите название вакансии (all - очистить файл): ')
    j_man.delete(name)
