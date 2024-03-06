from src.utils.hh_api import HeadHunter
from src.utils.json_crud import JsonManager
from src.utils.vacancy import Vacancy


hhapi = HeadHunter()
jsonmgr = JsonManager()
jsonmgr.delete('all')
vacs = hhapi.get_vacancies(text='python', per_page=5, location='москва')
jsonmgr.add(vacs)
vacs = jsonmgr.search(salary=10000)
vacs = jsonmgr.top_salary(vacs, 3)

for vac in vacs:
    print(vac)


