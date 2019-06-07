from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		days = request.POST.get('days')
		book = Book(name=name)
		book.save()
		rent = Rent(book=book,days=days)
		rent.calculate_cost()
		rent.save()
	rented = Rent.objects.all()
	total = 0
	for rent in rented:
		total += rent.charges
	return render(request,"index.html",{'rented':rented,'total':total})