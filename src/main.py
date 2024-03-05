from utils.hh_api import HeadHunter
from utils.vacancy import Vacancy

# vac = Vacancy('Python', 'link', 50000, 'Very long description', '...' )
# vac2 = Vacancy('Python', 'link', 40000, '...', '...' )
#
# print(vac)

hhapi = HeadHunter()
hhapi.get_vacancies(salary=100000, text='таролог')