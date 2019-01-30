from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Notes
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def index(request):
    n = request.POST.get('note', False)
    if n:
        note_obj = Notes(note=n)
        note_obj.save()
    context = { "notes": Notes.objects.all() }
    return render(request, 'notes/index.html', context)

def delNote(request, index):
	try:
		Notes.objects.get(pk=index).delete()
	except DoesNotExist:
		raise Http404("does not exist")
	context = { "notes": Notes.objects.all() }
	return render(request, 'notes/index.html', context)

