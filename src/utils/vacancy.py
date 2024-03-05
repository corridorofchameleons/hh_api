from src.utils.error import TypeErr


class Vacancy:
    name: str
    link: str
    salary: int
    description: str
    requirements: str

    def __init__(self, name, link, salary, description, requirements):
        self.name = name
        self.link = link
        self.salary = salary if salary > 0 else None
        self.description = description
        self.requirements = requirements

    @classmethod
    def create(cls, name, link, salary, description, requirements):
        return cls(name, link, salary, description, requirements)

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

    def __str__(self):
        return f"{self.name}, {self.description[:10]}..., {self.salary}, {self.link}, {self.requirements[:10]}..."