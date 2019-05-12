from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def first(request):
    return render(request, 'first.html')

def second(request):
    return render(request, 'second.html')

def third(request):
    return render(request, 'third.html')

def fourth(request):
    return render(request, 'fourth.html')

def event_show(request):
    return render(request, 'event_show.html')

def search(request):
    return render(request, 'search.html')

def csvsave(request):
    return render(request, 'csvsave.html')

def episode(request):
    return render(request, 'episode.html')

def passs(request):
    return render(request, 'passs.html')