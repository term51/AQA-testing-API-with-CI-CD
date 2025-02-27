"""
    class Helper для отчетности


"""

import allure
import json
from allure_commons.types import AttachmentType


class Helper:
    # функция прикрепляет JSON из response к Allure отчету
    def attach_response(self, response):
        response = json.dumps(response, indent=4, ensure_ascii=False)  # ensure_ascii Отключаем ASCII-кодирование
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)
