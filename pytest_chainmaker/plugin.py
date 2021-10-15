from configparser import ConfigParser

import pytest


def pytest_addoption(parser):
    pass


@pytest.fixture(scope='session')
def contract(request):
    pass
    

@pytest.fixture(scope='session')
def block(request, conf):
    pass
