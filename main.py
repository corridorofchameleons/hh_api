from src.utils.hh_api import HeadHunter
from src.utils.json_crud import JsonManager
from src.utils.vacancy import Vacancy


hhapi = HeadHunter()
jsonmgr = JsonManager()
jsonmgr.delete('all')
vacs = hhapi.get(text='разработчик', per_page=20, area=3)
jsonmgr.insert(vacs)
vacs = jsonmgr.select()
vacs = jsonmgr.top_salary(vacs, 5)

for vac in vacs:
    print(vac)


