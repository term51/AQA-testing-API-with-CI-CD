"""


"""

import os
from dotenv import load_dotenv

load_dotenv()


class Headers:
    # базовые хедеры
    basic = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "API-1"
    }
