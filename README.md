# Crud Ace_api

Um crud para listar, editar, deletar uma lista de ACE(agente de combate a endemias).

Este crud segue este tutorial :
 
https://youtu.be/Xts8NmyAc8c?si=KIoaK2ywk9lF5LtD 

Um crud completo em django rest framework com toda documentação usando a biblioteca coreapi, seguindo a rota:

http://127.0.0.1:8000/docs/

para testar faça um clone desta pasta e instale o requirements.txt depois de criar e ativar a venv:

- criar e ativar a venv do windows: 


``` python -m venv venv ```

``` .\venv\Scripts\activate ```


- instalar o requirements:

``` pip install -r requirements.txt ```


# Documento de Visão

[Documento de visão](docs/documento_de_visao.md)


# Testes
### Videos:

https://www.youtube.com/watch?v=JIV6fcPN1tU


https://www.youtube.com/watch?v=pGWsUcDfVGA


https://www.youtube.com/watch?v=27-XNVUOPcMv

### Texto:

https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Testing



### Rodar testes unitarios e gerar um html com cobertura 

``` coverage run manage.py test | coverage html ```

### Rodar os testes de mutação

``` python manage.py muttest ace_api --modules ace_api.models ```

#### os alvos do muttest

``` python manage.py muttest ace_api --modules ace_api.models, ace_api.urls, ace_api.views ```
