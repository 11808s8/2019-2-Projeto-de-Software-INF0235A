# Sistema de Educação Financeira

Projeto realizado para a disciplina Projeto de Software - INF0235A do curso de Ciência da Computação da Universidade de Caxias do Sul.<br>
Autores: [Adriano Gomes da Silva](https://github.com/11808s8), [Bruno Caregnato](https://github.com/brunocaregnato), [Leopoldo Reginato](https://github.com/leocreginato) e [Venicius Bregalda](https://github.com/venicius12).

## Informações:
O projeto consiste em um sistema que calcula rendas/despesas do mês, com base em categorias cadastradas por um administrador do sistema e exibe os resultados do cálculo em gráficos, para auxiliar com o controle financeiro do usuário.
Há também um blog de acesso simplificado para que o usuário possa receber mais informações sobre educação financeira através de textos, imagens e vídeos.

## Imagens do Projeto:
![Página inicial do projeto](https://github.com/11808s8/2019-2-Projeto-de-Software-INF0235A/blob/master/artefatos/imagens-github/home.png)
<hr>

![Página com o formulário de cálculo de despesas financeiras](https://github.com/11808s8/2019-2-Projeto-de-Software-INF0235A/blob/master/artefatos/imagens-github/form.png)
<hr>

![Página com o blog de Educação Financeira](https://github.com/11808s8/2019-2-Projeto-de-Software-INF0235A/blob/master/artefatos/imagens-github/blog.png)
<hr>

![Página com exemplo de publicação no Blog de Educação financeira](https://github.com/11808s8/2019-2-Projeto-de-Software-INF0235A/blob/master/artefatos/imagens-github/blogpost.png)
<hr>


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

Instalar o wagtail se necessário:
```sh
    $ pip3 install wagtail 
```

### Rodando o servidor

Executar os comandos:
```sh
    $ python3 manage.py migrate
    $ python3 manage.py runserver
```

Usuário administrador: admin
Senha administrador: admin123

Endereço para acessar a página de administração do site:
http://127.0.0.1:8000/admin

### Tutorial Wagtail

[Link do tutorial](http://docs.wagtail.io/en/v2.0/getting_started/tutorial.html)


#### !Important:
Os comandos *source* e *deactivate* precisam ser executados toda vez para entrar e sair, respectivamente, do ambiente virtual.
Isto permite que os pacotes instalados dentro do ambiente virtual fiquem disponíveis somente nele, sem interferir com pacotes globais de sua máquina :-) .
