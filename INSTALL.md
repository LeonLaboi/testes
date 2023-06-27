# Configuração de ambiente

## Download repositório


`Criação do diretório para o projeto`
```sh
mkdir $BASE_PATH 
cd $BASE_PATH 
```

Todos os passos a seguir devem ser executados na raiz do diretório definido como base.

`Download do repositório`
```sh
git clone https://github.com/LeonLaboi/testes.git .
```

`Setup VirtualEnvironment`
```sh
python3 -m venv venv

venv/Scripts/activate
```

`Install packages`
```sh
pip install -r requirements.txt
```

`Environment Vars`
```sh
cp .env_sample .env

# altere para algo que quiser
```