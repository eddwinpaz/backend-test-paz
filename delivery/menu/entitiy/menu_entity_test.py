from django.test import TestCase
from menu.entity.menu_entity import Menu


class MenuEntityTestCase(TestCase):

    def setUp(self):
        self.menu = Menu(menu_id=1,
                         name="chicken salad",
                         description="chicken cheese salad",
                         expire_date=0)

    def test_order_entity_ok(self):
        # should be the same
        assert self.menu.menu_id == 1
        assert self.menu.name == "chicken salad"
        assert self.menu.description == "chicken cheese salad"
        assert self.menu.expire_date == 0

    def test_order_entity_error(self):
        # make if fail
        self.menu.menu_id = 2

        assert self.menu.menu_id == 1
        assert self.menu.name == "chicken salad"
        assert self.menu.description == "chicken cheese salad"
        assert self.menu.expire_date == 0
