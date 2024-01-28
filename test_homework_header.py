import requests
import pytest

class TestWorkHeader:
    def test_work_heade(self):
        data = {
            'email':"vinkotov@example",
            'password':'1234'
        }

        response1 = requests.post('https://playground.learnqa.ru/api/homework_header',data=data)

        assert response1.status_code == 200, "Wrong response code "

        response_headers = response1.headers
        assert response_headers is not None, "There is not field headers"

        print()
        print("answer=", dict(response1.headers))