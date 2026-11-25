import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Executa o Chrome sem abrir a janela",
    )


@pytest.fixture
def driver(request):
    opcoes = Options()

    if request.config.getoption("--headless"):
        opcoes.add_argument("--headless=new")
        opcoes.add_argument("--window-size=1920,1080")

    d = webdriver.Chrome(options=opcoes)

    if not request.config.getoption("--headless"):
        d.maximize_window()

    yield d
    d.quit()