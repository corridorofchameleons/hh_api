from src.utils.vacancy import Vacancy
from tests.fixtures import vacancy


def test_create():
    vac_1 = Vacancy.create('name', 'town', 50000, 'desc', 'req')
    assert vac_1.name == 'name'
    assert vac_1.town == 'town'
    assert vac_1.salary == 50000
    assert vac_1.description == 'desc'
    assert vac_1.requirements == 'req'

    vac_2 = Vacancy.create('name', 'town', -5, 'desc', 'req')
    assert vac_2.name == 'name'
    assert vac_2.town == 'town'
    assert vac_2.salary == 0
    assert vac_2.description == 'desc'
    assert vac_2.requirements == 'req'

    vac_3 = Vacancy.create('name', 'town', 'string', 'desc', 'req')
    assert vac_3.name == 'name'
    assert vac_3.town == 'town'
    assert vac_3.salary == 0
    assert vac_3.description == 'desc'
    assert vac_3.requirements == 'req'


def test_comparison(vacancy):
    assert vacancy[0] == vacancy[2]
    assert vacancy[1] < vacancy[0]
    assert vacancy[2] > 10000
