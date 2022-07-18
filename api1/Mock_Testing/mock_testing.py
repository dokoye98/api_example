from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import request_mock

from application import application

class TestBase(TestCase):
    def create_app(self):
        return app 

class TestRandom(TestBase):
    def test_dog(self):
        with patch('random.randint') as r:
            r.return_value = 0
            response = self.client.get(url_for('get_animal'))
            self.assertIn(b'Cat', response.data)

    def test_cat(self):
        with patch('random.randint') as r:
            r.return_value = 1
            response = self.client.get(url_for('get_animal'))
            self.assertIn(b'Dog',response.data)