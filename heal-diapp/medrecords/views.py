# myapp/views.py
from django.shortcuts import render, redirect
from .forms import DocumentUploadForm
from .models import Documents
from django.contrib.auth.decorators import login_required

#@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():            
            form.instance.uploaded_by = request.user  # Set the uploaded_by field to the current user
            form.instance.patient_name = request.user
            form.save()
            return redirect('medrecords')  # Redirect to the document list view
    else:
        form = DocumentUploadForm()

    return render(request, 'upload_document.html', {'form': form})

def medrecords(request):
    documents = Documents.objects.all()
    return render(request, 'medrecords.html',  {'documents': documents})