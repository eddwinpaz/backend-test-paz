from menu.entitiy.menu_entity import Menu
from menu.models import Menu as Orm
import datetime

from user.entity.user_entity import User
from user.models import User as OrmUser


class Repository:

    def getById(self, menuId):
        try:
            menu = Orm.objects.get(pk=menuId)
            obj = Menu(uuid=menu.uuid,
                       menu_id=menu.pk,
                       name=menu.name,
                       description=menu.description,
                       expire_date=menu.expiration_date)
            return obj
        except Exception:
            return None

    def getAll(self):
        try:
            results = Orm.objects.all()
            return [Menu(uuid=menu.uuid,
                         menu_id=menu.pk,
                         name=menu.name,
                         description=menu.description,
                         expire_date=menu.expiration_date) for menu in results]
        except Exception:
            return []

    def clientsPhoneBook(self):
        try:
            results = OrmUser.objects.all()
            return [User(user_id=user.pk,
                         name=user.name,
                         phone=user.phone,
                         email=user.email,
                         password=user.password,
                         admin=user.admin) for user in results]
        except Exception:
            return []

    def getTodayMenu(self, exp_hour):
        try:
            today_date = datetime.datetime.now()
            results = Orm.objects.filter(expiration_date__day=today_date.day,
                                         expiration_date__month=today_date.month,
                                         expiration_date__year=today_date.year,
                                         expiration_date__hour__lte=exp_hour,
                                         )
            print('-----------------------------------------------------------')
            print('broadcast slack has {} menus for today'.format(len(results)))

            return [Menu(uuid=menu.uuid,
                         menu_id=menu.pk,
                         name=menu.name,
                         description=menu.description,
                         expire_date=menu.expiration_date) for menu in results]
        except Exception as e:
            print(e)
            return []

    def add(self, name, description, expire_date):
        try:
            obj = Orm(name=name,
                      description=description,
                      expiration_date=expire_date)
            obj.save()
            return True
        except Exception:
            return False

    def update(self, menuId, name, description, expire_date):
        try:
            obj = Orm.objects.get(pk=menuId)
            obj.name = name
            obj.description = description
            obj.expire_date = expire_date
            obj.save()
            return True
        except Exception:
            return False

    def delete(self, menuId):
        try:
            obj = Orm.objects.get(pk=menuId)
            obj.delete()
            return True
        except Exception:
            return False
