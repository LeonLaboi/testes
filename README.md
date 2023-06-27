# Exercícios

Repositório para testes e exercícios.

## Estrutura de dados

### `testes_django`

Diretório para exercícios e testes usando django


#### Comandos básicos do `django-admin`

```sh
python manage.py $AÇÃO
django-admin $AÇÃO
```

##### Criar novo app
```sh
python manage.py startapp $NOME_DO_APP
```

##### Criar migrações
```sh
python manage.py makemigrations
```

##### Aplicar migrações
```sh
python manage.py migrate
```

##### Iniciar servidor
```sh
python manage.py runserver
```

##### Criar super usuário
```sh
python manage.py createsuperuser
```

#### Configurações

A pasta `$BASE_PATH/testes_django/testes_django` mantém os arquivos de configurações do django, da uma lida nele.

Cada app criado, é necessário ser indicado na lista `INSTALLED_APPS`



### `logger` 

Scripts relacionados a tratamento de excessões e logs.

#### `basic_logging.py`

Exemplo de configuração de log e geração de registros.

Ao executar o script, mensagens de log são registradas no arquivo `basic_logging.log` no mesmo diretório do script.

Referencias: 

https://docs.python.org/3/library/logging.html


### Env Vars

Exemplo de variaveis de sistema usando `python-decouple`.

O `python-decouple` busca pelo arquivo `.env` na mesma pasta em que é executado, então o script deve ser chamado pela raíz do repositório.

### Git

Na raiz do repositório há um arquivo `.gitignore` este arquivo serve para informar ao git que arquivos devem ser ignorados do repositório, ex: arquivos com dados sensíveis, temporários, gerados automaticamente, etc.

