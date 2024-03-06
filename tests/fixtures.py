import pytest

from src.utils.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return (Vacancy('name', 'town', 50000, 'desc', 'req'),
            Vacancy('name', 'town', 40000, 'desc', 'req'),
            Vacancy('name', 'town', 50000, 'desc', 'req'))
