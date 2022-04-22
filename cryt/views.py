from PyPDF2 import PdfFileReader, PdfFileWriter

from http.client import HTTPResponse
from urllib.robotparser import RequestRate
from django.core.files.base import ContentFile, File
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.static import serve

from .forms import SignDocForm, VerifyDocForm

from django.contrib.auth.models import User
from .models import Document, UserProfile

from .Gio import Gio

# Index page. Creates and receives sign document form.
@login_required
def index(request):
    if request.method == 'POST':
        form = SignDocForm(request.POST, request.FILES)
        if form.is_valid():
            #Confirm password is valid
            user = User.objects.get(username=request.user.username)
            if user.check_password(form.cleaned_data['password']):
                #Include metadata in document prior to hashing
                file = request.FILES['file']
                reader =  PdfFileReader(file.open('wb+'))
                writer = PdfFileWriter()
                

                writer.appendPagesFromReader(reader)
                metadata = reader.getDocumentInfo()
                writer.addMetadata(metadata)

                writer.addMetadata({"/Username": user.username})

                writer.write(file)
                
                #Sign document here
                profile = UserProfile.objects.get(user=user)

                gio = Gio()
                signature = gio.firmala(file, profile.private_key)
                

                with open('s', 'wb+') as s:
                    s.write(signature)
                
                    #Upload to datalake here. Also register share relationships.
                    Document.objects.create(document=file, owner=user, signature=File(s))
                file.close()
                 
                return HttpResponse(signature)
            else:
                return HttpResponse('Incorrect password')
        else:
            return HttpResponse('Invlid form')
    else:
        form = SignDocForm()
        return render(request, 'index.html', {'form': form, 'user': request.user})
        
@login_required
def mydocs(request):
    docs = Document.objects.filter(owner=request.user)
    return render(request, 'my_docs.html', {'docs': docs})

@login_required
def shared(request):
    docs = Document.objects.filter(shared_with=request.user)
    return render(request, 'shared.html', {'docs': docs})

@login_required
def verify(request):
    if request.method == 'POST':
        form = VerifyDocForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            #Read file metadata to fetch user to compare against
            try:
                reader =  PdfFileReader(file.open())
                metadata = reader.getDocumentInfo()
                username = metadata['/Username']
                user = User.objects.get(username=username)
            except:
                return HttpResponse('Could not read file metadata. File is possibly corrupt.')
            
            #Verify signature for given user
            try:
                profile = UserProfile.objects.get(user=user)
                doc = Document.objects.get(document=file.name)
                gio = Gio()
                res = gio.verificala(file, doc.signature, profile.public_key)
                return HttpResponse(res)
            except:
                return HttpResponse('Signature could not be verified.')

        else:
            return HttpResponse('Invalid form')
    else:
        form = VerifyDocForm()
        return render(request, 'verify.html', {'form': form})


#Serves documents depending on user credentials.
#It is pending to select specific user authorization. In the meantime, user has to be logged in.
@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    #Validate requested doc
    
    return serve(request, path, document_root, show_indexes)

