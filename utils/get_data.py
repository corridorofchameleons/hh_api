from abc import ABC, abstractmethod


class HhABC(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunter(HhABC):
    def __init__(self):
        pass

    def get_vacancies(self):
        pass
