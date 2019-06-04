# 2019-2-Projeto-de-Software-INF0235A

### Configuração do ambiente

Para a execução do projeto, é necessário executar inicialmente o arquivo createvirtualenv.sh .

Para prosseguir para a instalação, é necessário executar o comando (na mesma pasta que fica o README.md):
```sh
	$ source .venv/bin/activate
```
Após isto, é necessário executar o comando
```sh
	$ pip3 install -r requirements.txt
```
Este comando irá instalar o wagtail e todas as suas dependências.


Para sair do ambiente virtual, é necessário dar o comando:
```sh
	$ deactivate
```

### Rodando o servidor

Executar os comandos:
```sh
    $ ./manage.py migrate
    $ ./manage.py runserver
```

Usuário administrador: admin
Senha administrador: admin123

Endereço para acessar a página de administração do site:
http://127.0.0.1:8000/admin

## Tutorial Wagtail

(Link do tutorial)[http://docs.wagtail.io/en/v2.0/getting_started/tutorial.html]


## !Important:
Os comandos *source* e *deactivate* precisam ser executados toda vez para entrar e sair, respectivamente, do ambiente virtual.
Isto permite que os pacotes instalados dentro do ambiente virtual fiquem disponíveis somente nele, sem interferir com pacotes globais de sua máquina :-) .
