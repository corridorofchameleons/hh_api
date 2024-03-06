from src.utils.hh_api import HeadHunter

test_api = HeadHunter()


def test_get():
    assert len(test_api.get(per_page=1)) == 1
