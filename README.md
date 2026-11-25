# Estudos de Selenium com Python

Projeto de aprendizado de automação de testes web com Python, Selenium WebDriver e
pytest. Os exemplos usam o [SauceDemo](https://www.saucedemo.com) e evoluem de
interações básicas com o navegador para testes organizados com o padrão Page
Object.

## Pré-requisitos

- Python 3.10 ou superior.
- Google Chrome instalado.
- Acesso à internet para abrir o SauceDemo e, na primeira execução, permitir que
  o Selenium Manager obtenha o driver compatível com o navegador.

## Configuração

Na raiz do projeto, crie e ative um ambiente virtual e instale as dependências.

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Linux ou macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Dependências principais:

- `selenium`: controle do navegador.
- `pytest`: execução e organização dos testes.
- `pytest-html`: geração de relatórios HTML.

## Executar os testes

Na raiz do projeto, execute a suíte completa:

```bash
python -m pytest
```

O pytest descobre os testes dentro de `tests/`. Para executar sem abrir a janela
do Chrome:

```bash
python -m pytest --headless
```

Para executar um arquivo ou teste específico:

```bash
python -m pytest tests/test_login.py
python -m pytest tests/test_carrinho.py::test_adicionar_produto_ao_carrinho
```

O fixture `driver`, definido em `conftest.py`, inicializa o Chrome para cada
teste e encerra o navegador ao final. A opção `--headless` ativa o modo sem
interface gráfica.

### Relatório HTML

Com `pytest-html` instalado, crie a pasta de relatórios e gere um relatório
autocontido:

```bash
python -c "from pathlib import Path; Path('reports').mkdir(exist_ok=True)"
python -m pytest --html=reports/relatorio.html --self-contained-html
```

Os arquivos em `reports/` são ignorados pelo Git.

## Exemplos de estudo

Os scripts em `estudos/` são exercícios independentes. Execute-os a partir da
raiz; eles abrem o Chrome e acessam o SauceDemo:

```bash
python estudos/primeiro_teste.py
python estudos/localizando.py
python estudos/login.py
python estudos/esperas.py
```

`localizando.py`, `login.py` e `esperas.py` aguardam que o usuário pressione
Enter antes de fechar o navegador. Esses exemplos servem para exploração manual;
os testes automatizados estão em `tests/`.

## Estrutura do projeto

```text
.
├── estudos/                   # Exercícios básicos de automação
├── pages/                     # Page Objects do SauceDemo
│   ├── carrinho_page.py
│   ├── login_page.py
│   └── produtos_page.py
├── tests/                     # Testes automatizados com pytest
│   ├── test_carrinho.py
│   └── test_login.py
├── conftest.py                # Fixture do WebDriver e opção --headless
├── pytest.ini                 # Configuração de descoberta e execução
├── requirements.txt           # Dependências do projeto
└── README.md
```

## Escopo atual de QA

A suíte cobre o login bem-sucedido, cenários de login inválido (credenciais
incorretas, usuário bloqueado e campos obrigatórios) e a inclusão de um produto
no carrinho. Os testes usam esperas explícitas nos Page Objects para sincronizar
com elementos da página.

Os testes são de ponta a ponta e dependem do SauceDemo, do Chrome e da conexão de
rede; indisponibilidade ou mudanças no site podem afetar os resultados. No
momento, o projeto não configura ferramentas de lint, formatação, cobertura ou
pipeline de integração contínua.

## Dependências

As versões estão fixadas em [`requirements.txt`](requirements.txt). Para atualizar
ou adicionar uma dependência, ajuste esse arquivo e reinstale com
`python -m pip install -r requirements.txt`.