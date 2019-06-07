from django.test import TestCase
from django.urls import reverse
from mainapp.models import Rent,Book

# request test
class AppTest(TestCase):
    url = reverse("index-page")

    def text_get(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        resp = self.client.post(self.url,{'name':'book name','days':5})
        self.assertEqual(resp.status_code, 200)

# models test
class RentTestCase(TestCase):
    def setUp(self):
        book = Book.objects.create(name="test book")
        Rent.objects.create(book=book,days=5, charges=5,)

    def test_renting(self):
        book = Book.objects.get(name="test book")
        rent1 = Rent.objects.get(book=book)
        self.assertEqual(rent1.calculate_cost(),rent1.days*1)
        self.assertEqual(book.__str__(), book.name)