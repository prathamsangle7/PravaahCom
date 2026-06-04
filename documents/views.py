import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import DocumentUploadForm


@login_required
def home(request):
    return redirect('document_list')


@login_required
def upload_document(request):
    form = DocumentUploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        doc = form.save(commit=False)
        doc.uploaded_by  = request.user
        doc.file_type    = os.path.splitext(str(doc.file_url))[1].lstrip('.')
        doc.file_size_kb = request.FILES['file_url'].size // 1024
        doc.save()
        return redirect('document_list')
    return render(request, 'documents/upload.html', {'form': form})


@login_required
def download_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    doc.download_count += 1
    doc.save()
    return FileResponse(doc.file_url.open('rb'), as_attachment=True,
                        filename=os.path.basename(doc.file_url.name))


@login_required
def document_list(request):
    qs = Document.objects.all()
    if request.GET.get('module'): qs = qs.filter(related_module=request.GET['module'])
    if request.GET.get('type'):   qs = qs.filter(file_type=request.GET['type'])
    if request.GET.get('q'):      qs = qs.filter(title__icontains=request.GET['q'])
    return render(request, 'documents/list.html', {'documents': qs})
