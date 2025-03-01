# Тестовые функции должны начинаться с test_,
# и если вы хотите использовать классы, они также должны начинаться с Test
# pytest запустит все файлы формы test_*.py или *_test.py в текущем каталоге и его подкаталогах.
import json

import pytest
import requests


def func(x):
    return x + 1


def test_func():
    assert func(2) != 4


def f():
    raise SystemExit(1)


def test_f():
    """вызывает ли f(), указанное в аргументах."""
    with pytest.raises(SystemExit):
        f()


# При группировании тестов внутри классов следует помнить,
# что каждый тест имеет уникальный экземпляр класса.

class TestClass:
    def test_one(self):
        x = "This"
        assert 'h' in x

    # def test_two(self):
    #     x = "hello"
    #     assert hasattr(x, "hello")


# атрибуты, добавленные на уровне класса, являются атрибутами класса ,
# поэтому они будут общими для разных тестов.

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    # def test_two(self):
    #     assert self.value == 1


def test_ping(client):
    url = requests.get(url="http://0.0.0.0:8000/ping/")
    response = client.get(url)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content["ping"] == "pong!"
