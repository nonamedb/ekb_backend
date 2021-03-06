# coding: utf-8


""" Test for layer_business - physical.
    Using first.
"""


__author__ = 'Sidorov D.V.'


import requests
import pytest
import django

django.setup()


URL = 'http://localhost:8080'


def create_request(url, **params):
    res = requests.post(url, data=params)
    return res.json()


@pytest.mark.parametrize("spec,year,labor_coef,released_coef,delta_industry", [
    ('developer', 2021, 0.2, 0.9, 0.1),
    ('tutor', 2023, 0.2, 0.9, 0.5),
    ('lawyer', 2024, 0.2, 0.9, 0.3),
    ('cook', 2025, 0.2, 0.9, 0.2),
    ('painter', 2025, 0.2, 0.9, 0.2)
])
def test_vacancies_calculator(spec, year, labor_coef, released_coef, delta_industry):
    res = create_request('{}/{}/'.format(URL, 'calculator'), spec=spec, year=year, labor_coef=labor_coef, released_coef=released_coef, delta_industry=delta_industry)
    print(res)
    assert True
