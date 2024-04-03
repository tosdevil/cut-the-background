from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageForm
from .models import ImageCut

# Create your views here.

def index(request):
	return render(request, 'main/index.html')

def cut(request):
	error = ''
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			if not request.session.session_key:
				return render(request, 'main/cut.html', {'form': form, 'error': 'простите, не можем идентифицировать вашу сессию. возможно, вы работаете в режиме инкогнито.'})
			session_key = request.session.session_key
			print(session_key)
			photo = form.save(commit=False)
			photo.uploader_session = session_key
			photo.save()
			# form.save()
			return redirect('cut_detail', pk=form.instance.pk)
		else:
			error = 'неверный тип данных'
			return redirect('cut')
	form = ImageForm()

	data={
		'form': form
	}
	return render(request, 'main/cut.html',data)

def cut_detail_view(request, pk):
    image = ImageCut.objects.get(pk=pk)
    return render(request, 'main/cut_result.html', {'image': image})