# Atividade ETL

Para iniciar a atividade criei uma conta no [https://home.openweathermap.org/](https://home.openweathermap.org/) para assim conseguir pegar minha chave para API.

Após isso iniciei o VSCode e segui os seguintes passos:

1. Criei o HTML que irá ser a visualização da tarefa chamado `weather_table.html`
2. Criei o `api.py` , neste arquivo criei as funções que irão pegar os dados da api, fazer o processo de ETL e conectar tudo isso no HTML para visualização.
3. Criei um banco de dados simples SQLite chamado `database.db` onde serão armazenados os dados retirados da API do OPENWEATHERMAP.
4. Por fim criei os testes da aplicação no arquivo `teste.py`onde consigo testar todas as funções e saber se o código apresenta inconsistências e onde elas estão para conseguir conserta-las.

## Instruções para funcionamento api.py:

1. Para instalar o flasck na minha máquina no VSCode foi preciso:
    1. Criar um ambiente virtual usando a paleta de comandos (`View > Command Palette` ). Em seguida, selecionei o comando `Python: Create Environment` para criar um ambiente virtual selecionei `venv` e depois o ambiente Python que eu desejava.
    2. Para dar continuidade tive que ativar o ambiente virtual e executei `Terminal: Create New Terminal` .
    3. Agora para instalar o Flask, no terminal, execute o comando `pip install flask` para instalar Flask em seu ambiente virtual.
2. Após instalar o flask é preciso instalar:

```python
pip install flask_sqlalchemy
pip install datetime
pip install pytz
```

Agora em `api_key = 'd13a18996616513b72952410f7ecd170’` adicione a api_key do seu usuário

Por fim clique para depurar e de irá aparecer uma rota, bem você irá abri-la no navegador e ira adicionar `/weather_data` no final da mesma. Assim será carregado o HTML e a conexão com a api será bem sucedida.

## Instruções para funcionamento teste.py:

1. Antes de testar é preciso instalar:

```python
pip install pytest
pip install responses
pip install api
pip install app
pip install db
pip install WeatherData
```

2. Agora para rodar os testes é preciso digitar: `python -m pytest teste.py`

## Explicação das funções api.py:

A aplicação inicia com `app = Flask(name)`.

A conexão com a base de dados SQLite é feita usando `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///etl_database.db'`

Definição de fuso horário `= pytz.timezone('America/Sao_Paulo')` 

A função ETL realiza uma solicitação GET para cada cidade, extrai o JSON dos dados recebidos e os insere na base de dados.

A rota `/weather_data` serve para analisar os dados coletados em um HTML.

A função `db.create_all()` é usada para criar, com flask, tabelas baseadas nos modelos definidos.

## Explicação das funções teste.py:

Os testes são definidos nos blocos que começam com `assert` e foram definidos alguns como do tipo dos dados, que deve ser openweather, e do tamanho do array que deve ser igual a 3 e o segundo teste verifica a última coluna de dados.
