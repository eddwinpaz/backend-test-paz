from order.repository.repository_django_orm import Repository


class UseCase(Repository):

    def __init__(self, repository):
        self.repository = repository

    def getById(self, orderId, userId):
        return self.repository.getById(orderId, userId)
    
    def getAllById(self, userId):
        result = self.repository.getAllById(userId)
        return result

    def getMenuNameById(self,menuId):
        result = self.repository.getMenuNameById(menuId)
        return result

    def getAll(self):
        result = self.repository.getAll()
        return result

    def createOrder(self, userId, menuId, customization):
        result = self.repository.createOrder(userId, menuId, customization)
        if result:
            return True
        else:
            return False
