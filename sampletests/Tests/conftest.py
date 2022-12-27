import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome')


@pytest.fixture(scope='class')
def browser_open(request):

    choosebrowser = request.config.getoption('browser_name')
    if choosebrowser == 'chrome':
        d = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif choosebrowser == 'firefox':
        d = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif choosebrowser == 'edge':
        d = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    d.get("https://www.redbus.in/")
    d.implicitly_wait(10)
    d.maximize_window()
    request.cls.d = d
    yield
    d.close()
