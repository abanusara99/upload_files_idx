from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def welcome(request):
    return render(request, 'welcome.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['uploaded_file']:
        uploaded_file = request.FILES['uploaded_file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        return render(request, 'upload.html', {
            'url': url
        })
            
    return render(request, 'upload.html')

    if not uploaded_file:  # Check if no file is uploaded
            return render(request, '404.html')

def error(request):
    return render (request, '404.html')
     
