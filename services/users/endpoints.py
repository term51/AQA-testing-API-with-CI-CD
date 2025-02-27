"""


"""

import os

# настройка для 2х стендов (dev и release)
HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ['STAGE'] == 'qa' \
    else 'https://release-gs.qa-playground.com/api/v1'

print("HOST-->", HOST)


class Endpoints:
    create_user = f"{HOST}/users"
    get_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"  # пример: get_user_by_id("123") = {HOST}/users/123
