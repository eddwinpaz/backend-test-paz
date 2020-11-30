from django.test import TestCase
from user.repository.repository_django_orm import Repository


class RepositoryTestCase(TestCase, Repository):

    def setUp(self):
        self.repository = Repository()
        self.repository.create('jhon', '56933375029', 'example@gmail.com', "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")

    # Test getbyId Integration

    def test_repository_getById(self):
        response = self.repository.getById(1)
        assert 'jhon' == response.name
        assert 'example@gmail.com' == response.email

    # Test GetAll

    def test_repository_getAll(self):
        result = self.repository.getAll()
        assert len(result) == 1

    # Test Authenticate

    def test_repository_authenticate_ok(self):
        user, error = self.repository.authenticate('example@gmail.com', '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8')
        assert error is False

    def test_repository_authenticate_fail(self):
        user, error = self.repository.authenticate('789', '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8')
        assert error is True

    def test_repository_create(self):
        error = self.repository.create('andrew', '5693375029', 'fake@gmail.com',
                                       '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8')
        assert error is True
