from django.db import models


# Create your models here.

BOOK_TYPES=(
    ('regular','Regular'),
    ('novel','Novel'),
    ('fiction','Fiction')
)

class Book(models.Model):
    name = models.CharField(max_length=200, default='book')
    kind = models.CharField(max_length=200,null=True,blank=True,choices=BOOK_TYPES)
    def __str__(self):
        return self.name


class Rent(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    days = models.PositiveIntegerField()
    charges = models.FloatField(default=0)
    def calculate_cost(self):
        if self.book.kind == 'fiction':
            self.charges = self.days * 3
        else:
            self.charges = self.days * 1.5
        return self.charges
    def __str__(self):
        return self.book.name +'--'+str(self.charges)
