import pytest

from pages.login_page import LoginPage
from pages.produtos_page import ProdutosPage
from pages.carrinho_page import CarrinhoPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def carrinho(driver):
    """Faz login, adiciona a mochila e abre o carrinho, pronto para o checkout."""
    login = LoginPage(driver)
    login.abrir()
    login.fazer_login("standard_user", "secret_sauce")

    produtos = ProdutosPage(driver)
    produtos.adicionar_ao_carrinho("sauce-labs-backpack")
    produtos.abrir_carrinho()
    return CarrinhoPage(driver)


def test_checkout_completo(driver, carrinho):
    """Fluxo completo: dados válidos levam à confirmação do pedido."""
    carrinho.iniciar_checkout()

    checkout = CheckoutPage(driver)
    checkout.preencher_dados("Ana", "Silva", "12345")
    checkout.continuar()
    checkout.finalizar()

    assert "Thank you for your order" in checkout.obter_mensagem_confirmacao()
    assert "checkout-complete" in driver.current_url


@pytest.mark.parametrize(
    "nome, sobrenome, cep, erro_esperado",
    [
        ("", "Silva", "12345", "First Name is required"),
        ("Ana", "", "12345", "Last Name is required"),
        ("Ana", "Silva", "", "Postal Code is required"),
    ],
    ids=["nome_vazio", "sobrenome_vazio", "cep_vazio"],
)
def test_checkout_dados_invalidos(driver, carrinho, nome, sobrenome, cep, erro_esperado):
    """Campos obrigatórios vazios mostram o erro certo e bloqueiam o avanço."""
    carrinho.iniciar_checkout()

    checkout = CheckoutPage(driver)
    checkout.preencher_dados(nome, sobrenome, cep)
    checkout.continuar()

    assert erro_esperado in checkout.obter_mensagem_erro()
    assert "checkout-step-two" not in driver.current_url