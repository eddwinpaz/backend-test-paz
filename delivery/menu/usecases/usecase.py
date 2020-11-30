from menu.repository.repository_django_orm import Repository


class UseCase(Repository):

    def __init__(self, repository):
        self.repository = repository

    def getById(self, menuId):
        return self.repository.getById(menuId)

    def getAll(self):
        result = self.repository.getAll()
        return result

    def getTodayMenu(self, exp_hour):
        result = self.repository.getTodayMenu(exp_hour)
        return result

    def add(self, name, description, expire_date):
        result = self.repository.add(name, description, expire_date)
        return result

    def update(self, menuId, name, description, expire_date):
        result = self.repository.update(menuId, name, description, expire_date)
        return result

    def delete(self, menuId):
        result = self.repository.delete(menuId)
        return result

    def clientsPhoneBook(self):
        result = self.repository.clientsPhoneBook()
        return result
