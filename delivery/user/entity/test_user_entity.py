from django.test import TestCase
from user.entity.user_entity import User


class UserEntityTestCase(TestCase):

    def setUp(self):
        self.user = User(user_id=1,
                         name="mike",
                         phone="1234",
                         admin=False,
                         email="mike@example.com",
                         password="password",
                         )

    def test_user_entity_ok(self):

        assert self.user.user_id == 1
        assert self.user.name == "mike"
        assert self.user.phone == "1234"
        assert self.user.admin is False
        assert self.user.email == "mike@example.com"
        assert self.user.password == "password"

    def test_user_entity_error(self):

        self.user.name = "jhon"

        assert self.user.user_id == 1
        assert self.user.name != "mike"
        assert self.user.phone == "1234"
        assert self.user.admin is False
        assert self.user.email == "mike@example.com"
        assert self.user.password == "password"
