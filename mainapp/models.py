from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200, default='book')
    def __str__(self):
        return self.name


class Rent(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    days = models.PositiveIntegerField()
    charges = models.PositiveIntegerField()
    def calculate_cost(self):
        self.charges = self.days * 1
        return self.charges
    def __str__(self):
        return self.book +'--'+self.charges
