from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import addNotes
# Create your views here.

def index(request):
    viewnotes = addNotes.objects.all()
    return render(request,'index.html', {'vnotes':viewnotes})

def Add(request):
    new_notes =  addNotes(content = request.POST['content'])
    new_notes.save()
    return HttpResponseRedirect('/')

def Del(request, notes_id):
    del_notes =  addNotes.objects.get(id=notes_id)
    del_notes.delete()
    return HttpResponseRedirect('/')
