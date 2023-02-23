from django.shortcuts import render

# Create your views here.

#pass name of the template
def index(request):
    return render(request, 'entries/index.html')

def add(request):
    return render(request, 'entries/add.html')