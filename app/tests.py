from django.test import TestCase, Client

class ViewTest(TestCase):
    def setUp(self):
        pass

    def test_clinet(self):
        c = Client()
        data = c.get("")
        print(data)