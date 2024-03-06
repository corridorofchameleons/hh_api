from src.funcs.db_manipulations import add_vacancy, get_vacancies
from src.funcs.vacancies_queries import select_vacancies, top_vacancies, delete_vacancy, update_vacancy


def main():

    while True:
        print()
        ans = input('1 - Загрузить вакансии\n2 - Добавить вакансию\n3 - Изменить вакансию\n'
                    '4 - Удалить вакансию\n5 - Поиск по вакансиям\n6 - Топ вакансий\n7 - Выход\n')
        match ans:
            case '1':
                get_vacancies()
            case '2':
                add_vacancy()
            case '3':
                update_vacancy()
            case '4':
                delete_vacancy()
            case '5':
                vacancies = select_vacancies()
                for vac in vacancies:
                    print(vac)
            case '6':
                vacancies = top_vacancies()
                for vac in vacancies:
                    print(vac)
            case '7':
                break
            case _:
                continue


if __name__ == '__main__':
    main()
