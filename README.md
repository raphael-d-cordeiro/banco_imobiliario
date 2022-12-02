# Banco Imobiliário

### Pré-requisitos da Instalação
*  Instalar Make
> comando
```shell
$ sudo apt-get install make
```

* Instalar o Python3.10
> comandos
```shell
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
$ wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tar.xz
$ tar -xf Python-3.10.8.tar.xz
$ cd Python-3.10.8 && ./configure --enable-optimizations
$ make -j 2
# Note o (-j) corresponde ao número de núcleos em seu sistema para acelerar o tempo de construção
# Para descobrir quantos núcleos você tem em seu sistema, execute o seguinte código:
$ nproc
$ sudo make altinstall
$ python3.10 --version
```
### Caso precise de ajuda com os comandos
> comando
```shell
❯ make help
```
> resultado
```shell
Comandos - Banco Imobiliario
Ajuda

uso: make <sub comando>
Sub comandos:
    run                                         Rodar projeto
    run_test                                    Rodar teste de cobertura de codigo e pytest com modular fixture
```
### Rodar o projeto
> comando
```shell
❯ make run
```
### Rodar os testes
> comando
```shell
❯ make run_test
```