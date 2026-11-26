from pathlib import Path

import pytest
import pytest_html
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


@pytest.hookimpl(hookwrapper=True)                           # ← NOVO (função inteira abaixo)
def pytest_runtest_makereport(item, call):
    outcome = yield
    relatorio = outcome.get_result()

    if relatorio.when == "call" and relatorio.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return

        # 1) Foto anexada ao relatório HTML
        imagem_base64 = driver.get_screenshot_as_base64()
        extras = getattr(relatorio, "extras", [])
        extras.append(pytest_html.extras.png(imagem_base64))
        relatorio.extras = extras

        # 2) Foto salva como arquivo em reports/screenshots/
        pasta = Path("reports") / "screenshots"
        pasta.mkdir(parents=True, exist_ok=True)
        nome_arquivo = item.name.replace("[", "_").replace("]", "")
        driver.save_screenshot(str(pasta / f"{nome_arquivo}.png"))
