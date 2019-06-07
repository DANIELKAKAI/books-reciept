from django.test import TestCase
from django.urls import reverse
from .models import Book, Rent


# request test
class AppTest(TestCase):
    url = reverse("index-page")

    def text_get(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        resp = self.client.post(self.url, {'name': 'book name', 'days': 5, 'kind': 'fiction'})
        self.assertEqual(resp.status_code, 200)



class RentTestCase(TestCase):
    def setUp(self):
        book1 = Book.objects.create(name="test fiction", kind="fiction")
        book12 = Book.objects.create(name="test regular", kind="regular")
        book13 = Book.objects.create(name="test novel", kind="novel")

    def test_renting(self):
        book = Book.objects.create(name="test book", kind="novel")
        rent1 = Rent.objects.create(book=book,days=3)
        self.assertEqual(rent1.__str__(), "{}--{}".format(book.name, rent1.charges))
        self.assertEqual(book.__str__(), book.name)

    def test_fiction(self):
        book = Book.objects.get(name="test fiction")
        rent = Rent(book=book, days=3)
        self.assertEqual(rent.calculate_cost(), 9.0)

    def test_novel(self):
        book = Book.objects.get(name="test novel")
        rent = Rent(book=book, days=3)
        self.assertEqual(rent.calculate_cost(), 4.5)

    def test_regular(self):
        book = Book.objects.get(name="test regular")
        rent = Rent(book=book, days=3)
        self.assertEqual(rent.calculate_cost(), 3.5)
