import pytest
from API_disk import create_folder


TOKEN = ""

test_cases = [
    ('Test', "0c4181a7c2cf4521964a72ff57a34a07", 'Неверный токен'),
    ('Test', TOKEN, 'Папка создана'),
    ('Test', TOKEN, 'Папка с таким именем существует'),
]

@pytest.mark.parametrize('name_folder, token, expected', test_cases)
def test_create_folder(name_folder, token, expected):
    assert create_folder(name_folder, token) == expected