from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm

# Create your views here.

def index(request):
	return render(request, 'main/index.html')

def cut(request):
	error = ''
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		else:
			error = 'неверный тип данных'
	form = ImageForm()

	data={
		'form': form
	}
	return render(request, 'main/cut.html',data)