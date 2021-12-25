# IllusionRO

## Documentação

#

### Objetivo

A API é responsável por criar, listar e deletar leads captados pela aplicação FrontEnd.

#

## Instalação

- Primeiro faça o fork deste [repositório](https://gitlab.com/gabrieldosprazeres/illusion-ro-project-backend).

- Em seguida faça um git clone para a sua maquina

- Crie um ambiente [virtual em python](https://docs.python.org/pt-br/3/tutorial/venv.html)

```
$ python -m venv venv --upgrade-deps
```

- Entre no ambiente virtual

```
$ source venv/bin/activate
```

- Instale as dependencias necessárias utilizando o `requirements.txt`

```
$ pip install -r requirements.txt
```

- Configure suas variáveis seguindo o `.env.example`

  - Não esqueça de criar o seu banco de dados e adicionar no .env

- Crie as tabelas no banco de dados através do comando

```
$ flask db upgrade
```

- Inicie a aplicação local através do comando

```
$ flask run
```

- A aplicação inicializará na rota http://127.0.0.1:5000/. Você deverá ver algo semelhante ao snippet logo abaixo no seu terminal:

```
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 112-925-941
```

#

## Documentação das rotas e retornos

Você poderá acessar a documentação das rotas em breve, pois a documentaçãp está em construção..

#

## Desenvolvedores responsáveis pelo projeto

- [Italo Domingos](https://www.linkedin.com/in/issdomingos/)
- [Guilherme Job](https://www.linkedin.com/in/guilherme-armesto-job/)
- [Gabriel dos Prazeres](https://www.linkedin.com/in/gabrieldosprazeres/)
- [Miqueias Carvalho](https://www.linkedin.com/in/miqueias-carvalho-dos-santos/)
