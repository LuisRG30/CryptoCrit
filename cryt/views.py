from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .forms import SignDocForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = SignDocForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse(form)
        else:
            return HttpResponse('Invlid form')
        #Sign document here

        #Upload to datalake here 
        pass
    else:
        form = SignDocForm()
        return render(request, 'index.html', {'form': form})
        