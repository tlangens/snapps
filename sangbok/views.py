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
	context['catclass'] = 'c%d'%s.category.id
	return render(request, 'song.html', context)

def editsong(request, song):
	context = {}
	songobj = Snapsvisa.objects.get(id=song)
	form = SongForm(data=request.POST or None, instance=songobj)
	if(request.method == 'POST'):
		if(not songobj.protected and form.is_valid()):
			form.save()
			return HttpResponseRedirect('/%d'%songobj.id)
	context['form'] = form
	context['song'] = songobj
	return render(request, 'edit.html', context)

def addsong(request):
	context = {}
	form = SongForm(data=request.POST or None)
	if(request.method == 'POST'):
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	context['form'] = form
	context['song'] = None
	return render(request, 'edit.html', context)

def deletesong(request, song):
	s = Snapsvisa.objects.get(id=song)
	if not s.protected:
		s.delete();
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

def random(request):
	s = Snapsvisa.objects.order_by('?')[0].id
	return HttpResponseRedirect('/%d'%s)

def next(request, id):
	try:
		s = Snapsvisa.objects.get(id=id)
	except Snapsvisa.DoesNotExist:
		raise Http404

	n = Snapsvisa.objects.next(s)
	return HttpResponseRedirect('/%d'%n.id)

def prev(request, id):
	try:
		s = Snapsvisa.objects.get(id=id)
	except Snapsvisa.DoesNotExist:
		raise Http404

	p = Snapsvisa.objects.prev(s)
	return HttpResponseRedirect('/%d'%p.id)