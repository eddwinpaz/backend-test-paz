from datetime import datetime
# Entities
from user.entity.user_entity import User
from menu.entitiy.menu_entity import Menu
from order.entity.order_entity import Order
# ORM Models
from order.models import Order as OrmOrder
from user.models import User as OrmUser
from menu.models import Menu as OrmMenu


class Repository:

    def getMenuNameById(self, menuId):
        obj = OrmMenu.objects.get(pk=menuId)
        menu = Menu(
            menu_id=obj.pk,
            name=obj.name,
            description=obj.description,
            expire_date=obj.expiration_date,
        )
        return menu

    def getById(self, orderId, userId):
        order = OrmOrder.objects.get(pk=orderId, user__pk=userId)

        menu = Menu(
            menu_id=order.menu.pk,
            name=order.menu.name,
            description=order.menu.description,
            expire_date=order.menu.expiration_date,
        )

        user = User(
            user_id=order.user.pk,
            name=order.user.name,
            phone=order.user.phone,
            admin=order.user.admin,
            email=order.user.email,
            password=order.user.password,
        )

        obj = Order(order_id=order.pk,
                    menu=menu,
                    user=user,
                    customization=order.customization,
                    created_date=order.created_date,
                    status=order.get_status_display(),
                    )
        return obj

    def getAllById(self, userId):
        results = OrmOrder.objects.filter(user__pk=userId)
        rows = []
        for order in results:
            menu = Menu(
                menu_id=order.menu.pk,
                name=order.menu.name,
                description=order.menu.description,
                expire_date=order.menu.expiration_date,
            )

            user = User(
                user_id=order.user.pk,
                name=order.user.name,
                phone=order.user.phone,
                admin=order.user.admin,
                email=order.user.email,
                password=order.user.password,
            )

            obj = Order(order_id=order.pk,
                        menu=menu,
                        user=user,
                        customization=order.customization,
                        created_date=order.created_date,
                        status=order.get_status_display(),
                        )
            rows.append(obj)
        return rows

    def getAll(self):
        results = OrmOrder.objects.all()
        rows = []
        for order in results:
            menu = Menu(
                menu_id=order.menu.pk,
                name=order.menu.name,
                description=order.menu.description,
                expire_date=order.menu.expiration_date,
            )

            user = User(
                user_id=order.user.pk,
                name=order.user.name,
                phone=order.user.phone,
                admin=order.user.admin,
                email=order.user.email,
                password=order.user.password,
            )

            obj = Order(order_id=order.pk,
                        menu=menu,
                        user=user,
                        customization=order.customization,
                        created_date=order.created_date,
                        status=order.get_status_display(),
                        )
            rows.append(obj)
        return rows

    def createOrder(self, userId, menuId, customization):
        try:
            user = OrmUser.objects.get(pk=userId)
            menu = OrmMenu.objects.get(pk=menuId)
            # check if user__pk = userId can workout...

            order = OrmOrder(user=user,
                             menu=menu,
                             customization=customization,
                             delivered_date=datetime.now(),
                             status='1')
            order.save()
            return True

        except Exception as error:
            print(error)
            return False
