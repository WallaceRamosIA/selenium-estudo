from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Registra a opção --headless na linha de comando do Pytest."""
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Executa o Chrome sem abrir a janela",
    )


@pytest.fixture
def driver(request):
    """Abre o Chrome para cada teste e o fecha no final, mesmo se o teste falhar."""
    opcoes = Options()

    if request.config.getoption("--headless"):
        opcoes.add_argument("--headless=new")
        # Sem janela, o Chrome usaria uma tela minúscula e esconderia elementos.
        opcoes.add_argument("--window-size=1920,1080")

    d = webdriver.Chrome(options=opcoes)

    if not request.config.getoption("--headless"):
        d.maximize_window()

    yield d
    d.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Quando um teste falha, tira um screenshot e o anexa ao relatório HTML."""
    outcome = yield
    relatorio = outcome.get_result()

    # Só age na execução do teste ("call") e apenas se ele falhou.
    if relatorio.when == "call" and relatorio.failed:
        driver = item.funcargs.get("driver")
        if driver is None:
            return  # teste que não usa navegador

        # 1) Foto anexada ao relatório HTML
        imagem_base64 = driver.get_screenshot_as_base64()
        extras = getattr(relatorio, "extras", [])
        extras.append(pytest_html.extras.png(imagem_base64))
        relatorio.extras = extras

        # 2) Foto salva como arquivo em reports/screenshots/
        pasta = Path("reports") / "screenshots"
        pasta.mkdir(parents=True, exist_ok=True)
        # Os colchetes do nome do teste parametrizado não são bons em nome de arquivo.
        nome_arquivo = item.name.replace("[", "_").replace("]", "")
        driver.save_screenshot(str(pasta / f"{nome_arquivo}.png"))