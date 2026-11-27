from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage
from pages.carrinho_page import CarrinhoPage


def test_adicionar_produto_ao_carrinho(driver):
    """Um produto adicionado atualiza o ícone do carrinho e aparece na página do carrinho."""
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("standard_user", "secret_sauce")

    produtos = ProdutosPage(driver)
    produtos.adicionar_ao_carrinho("sauce-labs-backpack")
    assert produtos.obter_quantidade_carrinho() == "1"

    produtos.abrir_carrinho()
    carrinho = CarrinhoPage(driver)
    assert carrinho.obter_nomes_itens() == ["Sauce Labs Backpack"]