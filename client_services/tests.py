import datetime

from django.test import TestCase
from .models import client


# Setup
class modelTests(TestCase):
    def setUp(self):
        client.objects.create(first_name="David", last_name="Welgus",
                              birth_date="1982-06-09", address="909 W. Buena Ave.",
                              city="Chicago", zip_code=60613)

    def test_client_content(self):
        cl = client.objects.get(id=1)
        expected_first_name = "David"
        expected_last_name = "Welgus"
        expected_birth_date = "1982-06-09"
        expected_address = "909 W. Buena Ave."
        expected_city = "Chicago"
        expected_zip = 60613

        # Convert date to string
        cl.birth_date = cl.birth_date.strftime("%Y-%m-%d")

        self.assertEquals(expected_birth_date, cl.birth_date)
        self.assertEquals(expected_first_name, cl.first_name)
        self.assertEquals(expected_last_name, cl.last_name)
        self.assertEquals(expected_address, cl.address)
        self.assertEquals(expected_city, cl.city)
        self.assertEquals(expected_zip, cl.zip_code)
