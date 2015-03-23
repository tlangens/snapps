from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from sangbok.models import *
from sangbok.forms import *

# Create your views here.
def home(request):
	return render(request, 'base.html')

def song(request, song):
	try:
		s = Snapsvisa.objects.get(id=song)
	except Snapsvisa.DoesNotExist:
		raise Http404
	context = {"song": s}
	return render(request, 'song.html', context)

def editsong(request, song):
	context = {}
	songobj = Snapsvisa.objects.get(id=song)
	form = SongForm(data=request.POST or None, instance=songobj)
	if(request.method == 'POST'):
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect('/')
	context['form'] = form
	context['existing'] = True
	return render(request, 'edit.html', context)

def addsong(request):
	context = {}
	form = SongForm(data=request.POST or None)
	if(request.method == 'POST'):
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	context['form'] = form
	context['existing'] = False
	return render(request, 'edit.html', context)

def deletesong(request, song):
	Snapsvisa.objects.get(id=song).delete();
	return HttpResponseRedirect('/')

def list(request):
	form = CategorySelectForm(data=request.GET)

	selected_categories = request.GET.getlist('c')
	if not selected_categories:
		cobj = Category.objects.all()
	else:
		cobj = Category.objects.filter(id__in=selected_categories)
	categories = []
	for c in cobj:
		s = Snapsvisa.objects.filter(category=c)
		t = [c, s]
		categories.append(t)
	context = {"songs": s, "form": form, "categories": categories}
	return render(request, 'category_list.html', context)