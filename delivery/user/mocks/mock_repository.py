from user.entity.user_entity import User


class MockRepository:

    def getById(self, userId):
        obj = User(
            user_id=userId,
            name="John Doe",
            phone="56933375029",
            admin=False,
            email="john@example.com",
            password="password",
        )
        return obj

    def getAll(self):
        return [User(
            user_id=123,
            name="John Doe",
            phone="56933375029",
            admin=False,
            email="john@example.com",
            password="password",
        )]

    def authenticate(self, email, password):
        if password == 'password':
            obj = User(
                user_id=123,
                name="John Doe",
                phone="56933375029",
                admin=False,
                email=email,
                password="password",
            )
            return obj, False
        else:
            return None, True
