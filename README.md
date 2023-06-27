# Exercícios

Repositório para testes e exercícios.

## Estrutura de dados

### `testes_django`

Diretório para exercícios e testes usando django

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

