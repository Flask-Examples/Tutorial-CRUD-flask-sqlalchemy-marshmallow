# Tutorial-CRUD-flask-sqlalchemy-marshmallow
Tutorial from 'API de CRUD com flask, sqlalchemy e marshmallow' (Eduardo Mendes) by Marcus Mariano 

---

## Introduction

Make CRUD with Flask and your tools

- flask
- flask-sqlalchemy
- flask-migrate
- flask-marshmallow
- marshmallow-sqlalchemy 


---

## Installation

```sh
pipenv install

```
---

## How to Run

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

Make Magrations
```sh
flask db init 

flask db migrate

flask db upgrade
```
### On Ipython

testing
```sh
from requests import get

get('http://127.0.0.1:5000')
```

Cadastrar
```sh
from requests import post

dados = {'escritor': 'Marcus', 'livro': 'python'}

post('http://127.0.0.1:5000/cadastrar', json=dados).json()

get('http://127.0.0.1:5000/mostrar').json()
```

modificar
```sh

novo_dado = {'escritor': 'flask', 'livro': 'python3'}

get('http://127.0.0.1:5000/modificar/3', json=novo_dado).json()

```


---

## License

Code and documentation are available according to the GNU GENERAL PUBLIC LICENSE Version 3 (see [LICENSE](https://www.gnu.org/licenses/gpl.html)).
