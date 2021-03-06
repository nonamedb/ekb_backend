# coding: utf-8


""" Test for layer_business - physical.
    Using first.
"""


__author__ = 'Sidorov D.V.'


import pytest
import django

django.setup()

from layer_business.calculator import VacanciesCalculatorBL


@pytest.mark.run(order=0)
@pytest.mark.parametrize("spec,year,labor_coef,released_coef,delta_industry", [
    ('developer', 2021, 0.2, 0.9, 0.1),
    ('developer', 2023, 0.2, 0.9, 0.5),
    ('developer', 2024, 0.2, 0.9, 0.3),
    ('developer', 2025, 0.2, 0.9, 0.2)
])
def test_vacancies_calculator(spec, year, labor_coef, released_coef, delta_industry):
    calculator = VacanciesCalculatorBL()
    calc_result = calculator.calculate(spec, year, labor_coef=labor_coef, released_coef=released_coef, delta_industry=delta_industry)
    print(calc_result)
    assert True
