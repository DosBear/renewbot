RenewBot - telegram бод для информирования о выходе новых версий таможенных программы.

## Использование

Программа может быть запущена
```
$ ./python start.py

## Установка

Установка необходимых пакетов:
```
$ sudo apt-get update
$ sudo apt-get install python3-pip python3-dev
```

Установка необходимых модулей с помощью пакетного менеджера из файла`requirements.txt`:
```
$ pip3 install --user -r requirements.txt
```

Cоздать и сохранить в каталоге программы файл secrets.json со следующим содержимым
```
{
    "telegram": {
        "token": "tokeid",
        "public_users": [  "user1","user2"],
        "private_users": [ "puser1","puser2"],
        "proxy_ip": "",
        "proxy_port": ""
    }
}
```

Где:
 * tokeid - идентификатор вашего бота;
 * user - идентификатор публичного пользователя или чата;
 * puser - идентификатор приватного пользователя или чата;