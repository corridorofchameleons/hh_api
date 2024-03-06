from src.utils.hh_api import HeadHunter
from src.utils.json_crud import JsonManager
from src.utils.vacancy import Vacancy


hhapi = HeadHunter()
jsonmgr = JsonManager()
jsonmgr.delete('all')
vacs = hhapi.get_vacancies(text='таролог', per_page=100)
print(len(vacs))
jsonmgr.add(vacs)
jsonmgr.add(Vacancy.create('1', '2', 10000, '', ''))
jsonmgr.delete('1')
print(len(jsonmgr.search()))

