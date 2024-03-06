from src.utils.hh_api import HeadHunter
from src.utils.json_crud import JsonManager
from src.utils.vacancy import Vacancy

# vac = Vacancy('Python', 'link', 50000, 'Very long description', '...' )
# vac2 = Vacancy('Python', 'link', 40000, '...', '...' )
#
# print(vac)

hhapi = HeadHunter()
hhapi.get_vacancies(text='таролог')

vacancy = Vacancy('1', '2', 50, '', '')

j = JsonManager()

j.add(vacancy)
j.update('1', salary=150000)
print(j.search(name='1', salary=1))
j.delete('1')
print(j.search(name='1'))