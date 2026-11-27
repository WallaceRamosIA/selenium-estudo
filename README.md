# Selenium Estudo

[![Testes automatizados](https://github.com/WallaceRamosIA/selenium-estudo/actions/workflows/teste.yml/badge.svg)](https://github.com/WallaceRamosIA/selenium-estudo/actions/workflows/teste.yml)

Projeto de automação de testes web com **Python, Selenium e Pytest**, usando o site de prática [SauceDemo](https://www.saucedemo.com).

## O que está coberto

- Login com sucesso e cenários inválidos (parametrizados)
- Adicionar produto ao carrinho e validar o carrinho
- Ordenação de produtos (dropdown)
- Checkout completo e validação de campos obrigatórios
- Page Object Model (POM)
- Execução headless, relatório HTML e screenshot automático em falhas
- Execução automática no GitHub Actions (CI)

## Estrutura

```
pages/              # Page Objects (login, produtos, carrinho, checkout)
tests/              # Testes automatizados
estudos/            # Scripts de estudo (exemplos iniciais de Selenium)
.github/workflows/  # Pipeline de CI (GitHub Actions)
conftest.py         # Fixture do driver, opção --headless e screenshot em falhas
pytest.ini          # Configuração do Pytest
requirements.txt    # Dependências
```

## Como executar

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

pytest -v                      # com janela do navegador
pytest -v --headless           # sem janela
pytest -v --html=reports/relatorio.html --self-contained-html
```

## Integração contínua

A cada push na branch `main`, o GitHub Actions roda os testes em modo headless e guarda o relatório HTML (e os screenshots, em caso de falha) como artifact da execução.