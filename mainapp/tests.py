from django.test import TestCase
from django.urls import reverse
from .models import Book,Rent

# request test
class AppTest(TestCase):
    url = reverse("index-page")

    def text_get(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        resp = self.client.post(self.url,{'name':'book name','days':5,'kind':'fiction'})
        self.assertEqual(resp.status_code, 200)


class RentTestCase(TestCase):
    def setUp(self):
        book = Book.objects.create(name="test book",kind="fiction")
        Rent.objects.create(book=book,days=5, charges=5,)

    def test_renting(self):
        book = Book.objects.get(name="test book")
        rent1 = Rent.objects.get(book=book)
        self.assertEqual(rent1.__str__(),"{}--{}".format(book.name,rent1.charges))
        self.assertEqual(book.__str__(), book.name)
