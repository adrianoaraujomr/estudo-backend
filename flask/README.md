# Dependências

* Python
* Pyenv
* Pyvirtualenv

# Criar Projeto

## Criar virtual env

* Criar um virtual env

```
$ pyenv install [python version]
$ pyenv virtualenv [python version] [virtualenv name]
```

* Ativar o virtual env

```
$ pyenv activate [virtualenv name]
```

## Instalar bibliotecas python

```
$ pip install flask
```

## Adicionar um code formatter

```
$ pip install black
```

## Criar arquivo gitignore

* Usar como base as referências

## Criar arquivo para environments variables (.env)

```
$ pip install python-dotenv
```

## Criar aplicação flask (bem básico)

* Criar um arquivo principal (ex.: main.py) que instanciara a aplicação (```app = Flask(__name__)```)
* Criar um diretório de rotas (ex.: routes/) para cada arquivo no routes uma blueprint deve ser criada e depois registrada no main.py

## Integração com banco de dados relacional

* Obs.: Para uma integração com banco de dados é bom usar um biblioteca de abstração de banco de dados, como o sqlalchemy, pois assim facilita no caso de ocorrer uma troca de qual banco de dados usar.

### Docker compose para rodar um container com o banco de dados escolhido

* Criar o arquivo docker-compose.yml com o banco escolhido
* Rodar o banco

```
$ docker compose up
```

### Instalar dependências de bibliotecas

```
$ pip install SQLAlchemy
$ pip install pg8000 # adaptador de banco de dados postgres
```

## Adicionar testes automatizados

```
$ pip install pytest
```

## Criar arquivo de dependências

```
$ pip freeze > requirements.txt
```

## Criar docker

* Criar um arquivo Docker
* Lembrar de no run adicionar o host, para a aplicação não ficar so no local do container
* Gerar imagem

```
$ docker build -t [nome] .
```

# Rodar aplicação

* Dev para testes

```
$ flask --app main --debug run
```

* Cenário de produção ?

# TO DO

* Autenticação

# Referências

[pyenv](https://github.com/pyenv/pyenv)  
[pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv)  
[blueprint](https://flask.palletsprojects.com/en/2.3.x/blueprints/)  
[docker postgres](https://hub.docker.com/_/postgres)  
[docker compose postgres](https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/)  
[sqlalchemy](https://www.sqlalchemy.org/)  
[sqlalchemy suporte banco de dados](https://docs.sqlalchemy.org/en/20/dialects/index.html)  
[pg8000 adapter](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.pg8000)  
[sqlalchemy flask](https://flask.palletsprojects.com/en/2.3.x/patterns/sqlalchemy/)
[sqlalchemy delete](https://qiita.com/nskydiving/items/eedd5cea88b5afdbfc49)
[sqlalchemy update](https://shigeblog221.com/python-sqlalchemy-update/)
[flask route params](https://stackoverflow.com/questions/24892035/how-can-i-get-the-named-parameters-from-a-url-using-flask)
[http status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
[vscode black configuration](https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0)
[python importing local module](https://fortierq.github.io/python-import/)
[pytest separte test directory](https://stackoverflow.com/questions/37816820/pytest-how-to-make-dedicated-test-directory)
[python gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
[flask gitignore](https://github.com/pallets/flask/blob/main/.gitignore)
[sqlalchemy delete all rows from table](https://stackoverflow.com/questions/16573802/flask-sqlalchemy-how-to-delete-all-rows-in-a-single-table)
[python environment variables](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1)