from user.repository.repository_django_orm import Repository


class UseCase(Repository):

    def __init__(self, repository):
        self.repository = repository

    def getById(self, userId):
        return self.repository.getById(userId)

    def getAll(self):
        result = self.repository.getAll()
        return result

    def authenticate(self, email, password):
        user, error = self.repository.authenticate(email, password)
        return user, error

    def create(self, name, phone, email, password):
        error = self.repository.create(name, phone, email, password)
        return error
