import pytest

from src.utils.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return (Vacancy('name1', 'town', 50000, 'desc', 'req'),
            Vacancy('name2', 'town', 40000, 'desc', 'req'),
            Vacancy('name3', 'town', 50000, 'desc', 'req'))
