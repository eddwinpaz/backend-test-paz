To install Application.

Please type following command:

```
docker-compose build && docker-compose up -d
```

then enter the docker container and type following command:

```
python manage.py makemigrations && python manage.py migrate
```

# Normal user URLS

login user:

http://localhost:7000/user/login

logout user:

http://localhost:7000/user/logout/

see today's menu

http://localhost:7000/menu/today/

create order based on menu item

http://localhost:7000/order/create/1

see single menu item details

http://localhost:7000/menu/1

# Admin user URLS

see all orders:

http://localhost:7000/order/

see all users:

http://localhost:7000/user/

create menu item

http://localhost:7000/menu/create

list all menu items

http://localhost:7000/menu/list

delete menu item

http://localhost:7000/menu/delete/1

update menu item

http://localhost:7000/menu/update/1

send slack notifications

http://localhost:7000/menu/slack-broadcast

whatsapp notifiations

http://localhost:7000/menu/whatsapp-broadcast