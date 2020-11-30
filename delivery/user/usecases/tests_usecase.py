from django.test import TestCase
from user.usecases.usecase import UseCase
from user.mocks.mock_repository import MockRepository


class UserUseCaseTestCase(TestCase):

    def setUp(self):
        self.mocked_repository = MockRepository()

    # Test getById

    def test_usecase_getById(self):
        use_case = UseCase(self.mocked_repository)
        result = use_case.getById(123)

        assert result.user_id == 123
        assert result.name == "John Doe"

    # Test GetAll

    def test_usecase_getAll(self):
        use_case = UseCase(self.mocked_repository)
        result = use_case.getAll()
        assert len(result) == 1

    # Test Authenticate

    def test_authenticate_ok(self):

        email = "pazeddwin@gmail.com"
        password = "password"

        use_case = UseCase(self.mocked_repository)
        user, error = use_case.authenticate(email, password)

        assert error is False

    def test_authenticate_fail(self):

        email = "pazeddwin@gmail.com"
        password = "badpassword"

        use_case = UseCase(self.mocked_repository)
        user, error = use_case.authenticate(email, password)

        assert error is True
        assert user is None
