"""
    для поднятия окружения (Что необходимо для данного API. Делается 1 раз перед прогоном всех тестов)
    "Sets up API, cleans DB and populates with sample data"

"""
import os
from dotenv import load_dotenv
import requests
import pytest

# подгрузка .env
load_dotenv()

# настройка для 2х стендов (dev и release)
HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ['STAGE'] == 'qa' \
    else 'https://release-gs.qa-playground.com/api/v1'


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.post(
        url=f"{HOST}/setup",
        headers={
            "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
        }
    )
    assert response.status_code == 205, "Init failed"
