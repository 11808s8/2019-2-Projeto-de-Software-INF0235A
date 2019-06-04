# 2019-2-Projeto-de-Software-INF0235A

Para a execução do projeto, é necessário executar inicialmente o arquivo createvirtualenv.sh .
Para prosseguir para a instalação, é necessário executar o comando:
```sh
	source .venv/bin/activate
```
Após isto, é necessário executar o comando
```sh
	pip3 install -r requirements.txt
```
Este comando irá instalar o wagtail e todas as suas dependências.


Para sair do ambiente virtual, é necessário dar o comando:
```sh
	deactivate
```

###!Important:
Os comandos *source* e *deactivate* precisam ser executados toda vez para entrar e sair, respectivamente, do ambiente virtual.
Isto permite que os pacotes instalados dentro do ambiente virtual fiquem disponíveis somente nele, sem interferir com pacotes globais de sua máquina :-) .
