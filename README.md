# Conversor de Moedas

O **Conversor de Moedas** é um projeto em Python criado para praticar conceitos de consumo de APIs REST, integração entre sistemas e tratamento de respostas HTTP.

O programa consulta a cotação atual de uma moeda por meio da [AwesomeAPI Economy](https://docs.awesomeapi.com.br/api-de-moedas) e informa o valor de compra (`bid`) da conversão solicitada.

Atualmente, o exemplo realiza a conversão de **Bitcoin (BTC)** para **Real brasileiro (BRL)**.

## Funcionalidades

- Consulta uma cotação por requisição HTTP
- Integra o projeto a uma API externa
- Extrai o valor de compra da resposta JSON
- Trata o caso em que o par de moedas não existe

## Tecnologias utilizadas

- Python 3.14 ou superior
- [Requests](https://requests.readthedocs.io/)
- [Poetry](https://python-poetry.org/)
- AwesomeAPI

## Pré-requisitos

Antes de começar, instale:

- Python 3.14 ou superior
- Poetry
- Git

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/DeyvedAntonio/conversor_moeda.git
cd conversor_moeda
```

2. Instale as dependências do projeto com o Poetry:

```bash
poetry install
```

O `poetry install` cria o ambiente virtual do projeto e instala a biblioteca `requests`.

## Como executar

Execute o programa dentro do ambiente gerenciado pelo Poetry:

```bash
poetry run python main.py
```

Com a configuração atual, o terminal exibirá o valor de compra de 1 BTC em BRL.

Exemplo de saída:

```text
350000.00
```

O valor exibido é dinâmico e pode variar de acordo com a cotação atual da API.

## Alterando as moedas

Para consultar outro par de moedas, altere os argumentos da função `conversor` no arquivo `main.py`:

```python
print(conversor('USD', 'BRL'))
```

O primeiro argumento representa a moeda de origem e o segundo representa a moeda de destino.

## Execução alternativa

Caso não queira usar o Poetry, é possível criar um ambiente virtual e instalar a dependência manualmente:

```bash
python -m venv .venv
source .venv/bin/activate
pip install requests
python main.py
```

No Windows PowerShell, a ativação do ambiente virtual deve usar:

```powershell
.venv\Scripts\Activate.ps1
```

## Estrutura do projeto

```text
conversor_moeda/
├── main.py            # Consulta da API e conversão da moeda
├── pyproject.toml     # Configuração e dependências do projeto
├── poetry.lock        # Versões exatas das dependências
├── .env.example       # Modelo de arquivo de ambiente
└── README.md
```

## API utilizada

Este projeto utiliza a AwesomeAPI Economy, que fornece as cotações no formato JSON.

Exemplo de endpoint:

```text
https://economia.awesomeapi.com.br/last/BTC-BRL
```

Para mais informações sobre pares disponíveis e formatos de resposta, consulte a documentação oficial da API.

## Licença

Este projeto está sob a licença MIT.
