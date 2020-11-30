from typing import Tuple, Type, Union

from user.entity.user_entity import User
from user.models import User as Orm


class Repository:

    def create(self, name, phone, email, password):
        try:
            user = Orm(name=name,
                       phone=phone,
                       admin=False,
                       email=email,
                       password=password,
                       )

            user.save()
            return True
        except Exception:
            return False

    def getById(self, userId):
        user = Orm.objects.get(pk=userId)
        obj = User(user_id=user.pk,
                   name=user.name,
                   phone=user.phone,
                   admin=user.admin,
                   email=user.email,
                   password=user.password,
                   )
        return obj

    def getAll(self):

        results = Orm.objects.all()
        return [User(user_id=q.pk,
                     name=q.name,
                     phone=q.phone,
                     admin=q.admin,
                     email=q.email,
                     password=q.password,
                     ) for q in results]

    def authenticate(self, email, password):
        try:
            user = Orm.objects.get(email=email, password=password)
            obj = User(user_id=user.pk,
                       name=user.name,
                       phone=user.phone,
                       admin=user.admin,
                       email=user.email,
                       password=user.password,
                       )
            return obj, False
        except Exception as e:
            print(e)
            return User, True
