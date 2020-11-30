class Order:
    def __init__(self, order_id, menu, user, customization, created_date, status):
        self.order_id = order_id
        self.menu = menu
        self.user = user
        self.customization = customization
        self.created_date = created_date
        self.status = status
