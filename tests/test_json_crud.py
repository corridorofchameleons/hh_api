from tests.fixtures import vacancy
from src.utils.json_crud import JsonManager

TEST_FILE = 'test_data/test_vacancies.json'
json_test = JsonManager(TEST_FILE)
json_test.delete('all')


def test_insert(vacancy):
    json_test.insert(vacancy)
    vacs = json_test.select()
    assert len(vacs) == 3
    json_test.delete('all')


def test_select(vacancy):
    json_test.insert(vacancy)
    vacs = json_test.select(salary=45000)
    assert len(vacs) == 2
    json_test.delete('all')


def test_update(vacancy):
    json_test.insert(vacancy)
    json_test.update('name1', salary=100000)
    vacs = json_test.select()
    assert vacs[0].salary == 100000
    assert vacs[1].salary == 40000
    json_test.delete('all')


def test_delete(vacancy):
    json_test.insert(vacancy)
    json_test.delete('name1')
    vacs = json_test.select()
    assert len(vacs) == 2
    json_test.delete('all')
