import pytest
from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage


def test_login_com_sucesso(driver):
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("standard_user", "secret_sauce")

    produtos = ProdutosPage(driver)
    assert produtos.obter_titulo() == "Products"
    assert "inventory" in driver.current_url


@pytest.mark.parametrize(
    "usuario, senha, erro_esperado",
    [
        ("standard_user", "senha_errada", "do not match"),
        ("locked_out_user", "secret_sauce", "locked out"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
    ids=["senha_invalida", "usuario_bloqueado", "usuario_vazio", "senha_vazia"],
)
def test_login_invalido(driver, usuario, senha, erro_esperado):
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login(usuario, senha)

    assert erro_esperado in login.obter_mensagem_erro()
    assert "inventory" not in driver.current_url