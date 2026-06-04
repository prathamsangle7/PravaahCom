from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, FileResponse
from django.contrib import messages
import os

from .models import Document


# Allowed extensions and MIME types
ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.jpg', '.jpeg', '.png', '.xlsx'}
ALLOWED_MIME = {
	'application/pdf',
	'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
	'image/jpeg',
	'image/png',
	'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
}


def home(request):
	"""Redirect to documents list."""
	return redirect('list_documents')


def upload_document(request):
	"""Handle a file upload from a form and save it to the Document model.

	Expects form field name `file` and optional `title`.
	Accepts: PDF, DOCX, JPG, PNG, XLSX. Rejects other types with 400.
	"""
	if request.method == 'POST':
		uploaded_file = request.FILES.get('file')
		title = request.POST.get('title') or (uploaded_file.name if uploaded_file else '')

		if not uploaded_file:
			messages.error(request, 'No file uploaded.')
			return redirect(request.path)

		filename = uploaded_file.name
		ext = os.path.splitext(filename)[1].lower()
		content_type = uploaded_file.content_type

		# Validate extension and mime type
		if ext not in ALLOWED_EXTENSIONS or content_type not in ALLOWED_MIME:
			return HttpResponseBadRequest('Unsupported file type.')

		doc = Document(
			title=title,
			file_type=ext.lstrip('.'),
			file=uploaded_file,
			file_size_kb=(uploaded_file.size + 1023) // 1024,
			uploaded_by=(request.user if getattr(request, 'user', None) and request.user.is_authenticated else None),
		)
		doc.save()

		messages.success(request, 'File uploaded successfully.')
		return redirect(request.path)

	# GET -> render a simple upload form (template should exist)
	return render(request, 'documents/upload.html')


def download_document(request, doc_id):
	"""Download a document by ID, increment download_count, and serve the file."""
	doc = get_object_or_404(Document, id=doc_id)

	# Increment download count and save
	doc.download_count += 1
	doc.save()

	# Serve the file
	response = FileResponse(doc.file.open('rb'), as_attachment=True, filename=os.path.basename(doc.file.name))
	return response


def list_documents(request):
	"""List all documents in a table with optional filtering by related_module."""
	documents = Document.objects.all().order_by('-uploaded_at')
	
	# Filter by related_module if provided
	related_module = request.GET.get('related_module')
	if related_module:
		documents = documents.filter(related_module=related_module)
	
	# Get unique related_modules for dropdown
	modules = Document.objects.values_list('related_module', flat=True).distinct().exclude(related_module__isnull=True).exclude(related_module='')
	
	context = {
		'documents': documents,
		'modules': sorted(modules),
		'selected_module': related_module,
	}
	return render(request, 'documents/list.html', context)
