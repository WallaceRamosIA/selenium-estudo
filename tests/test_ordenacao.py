import pytest

from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage


@pytest.fixture
def produtos(driver):
    """Faz login e devolve a página de produtos, pronta para os testes."""
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("standard_user", "secret_sauce")
    return ProdutosPage(driver)


def test_ordenar_nome_az(produtos):
    """A ordenação 'Name (A to Z)' deixa os nomes em ordem alfabética."""
    produtos.ordenar_por("az")
    nomes = produtos.obter_nomes_produtos()
    assert nomes == sorted(nomes)


def test_ordenar_nome_za(produtos):
    """A ordenação 'Name (Z to A)' deixa os nomes em ordem alfabética inversa."""
    produtos.ordenar_por("za")
    nomes = produtos.obter_nomes_produtos()
    assert nomes == sorted(nomes, reverse=True)


def test_ordenar_preco_menor_para_maior(produtos):
    """A ordenação 'Price (low to high)' deixa os preços em ordem crescente."""
    produtos.ordenar_por("lohi")
    precos = produtos.obter_precos_produtos()
    assert precos == sorted(precos)


def test_ordenar_preco_maior_para_menor(produtos):
    """A ordenação 'Price (high to low)' deixa os preços em ordem decrescente."""
    produtos.ordenar_por("hilo")
    precos = produtos.obter_precos_produtos()
    assert precos == sorted(precos, reverse=True)