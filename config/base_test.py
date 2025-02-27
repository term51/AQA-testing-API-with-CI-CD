"""
   Базовый класс для инициализации всех сервисов, для доступности во всех тестах
"""
from services.users.api_users import UsersAPI


class BaseTest:
    def setup_method(self):
        self.api_users = UsersAPI()
