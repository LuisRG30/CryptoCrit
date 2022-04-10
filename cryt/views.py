from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.static import serve

from .forms import SignDocForm

# Index page. Creates and receives sign document form.
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
        

#Serves documents depending on user credentials.
#It is pending to select specific user authorization. In the meantime, user has to be logged in.
@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)

