# django-realtime

Implementação de websockets para aplicação de chat

### Instalação
`
    pip install requirements.txt
`

É preciso ter o servidor redis na maquina, visite [Site Oficial](https://redis.io/), ou, caso tenha o docker instalado em sua maquina, insira os seguintes comandos:

`
$ sudo docker pull redis
`


`
$ docker run -d -p 6379:6379 --name redis-container redis
`

Depois é só testar:

`
python manage.py runserver
`
