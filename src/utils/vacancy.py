from src.utils.error import TypeErr


class Vacancy:
    name: str
    town: str
    salary: int
    description: str
    requirements: str

    def __init__(self, name: str, town: str, salary: int | float, description: str, requirements: str):
        self.name = name
        self.town = town
        self.salary = salary if salary and salary > 0 else 0
        self.description = description
        self.requirements = requirements

    @classmethod
    def create(cls, name, town, salary, description, requirements):
        '''
        Создает экземпляр класса
        '''
        return cls(name, town, salary, description, requirements)

    def __str__(self):
        return (f"Вакансия: {self.name}\n"
                f"Город: {self.town}\n"
                f"Зарплата: {self.salary}\n"
                f"Описание: {'' if not self.description else self.description[:20] + '...'}\n"
                f"Требования: {'' if not self.requirements else self.requirements[:20] + '...'}\n")

    # 3 магических метода ниже необходимы для сортировки вакансий по зарплате

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        elif isinstance(other, (int, float)):
            return self.salary > other
        else:
            raise TypeErr(type(self), type(other))

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        elif isinstance(other, (int, float)):
            return self.salary < other
        else:
            raise TypeErr(type(self), type(other))

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        elif isinstance(other, (int, float)):
            return self.salary == other
        else:
            raise TypeErr(type(self), type(other))
