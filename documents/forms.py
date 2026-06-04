from django import forms
from .models import Document

ALLOWED_TYPES = [
    'application/pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'image/jpeg',
    'image/png',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
]
MAX_SIZE_KB = 5120  # 5 MB

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model  = Document
        fields = ['title', 'file_url', 'related_module', 'related_id']

    def clean_file_url(self):
        f = self.cleaned_data['file_url']
        if f.content_type not in ALLOWED_TYPES:
            raise forms.ValidationError('Only PDF, DOCX, JPG, PNG, XLSX allowed.')
        if f.size > MAX_SIZE_KB * 1024:
            raise forms.ValidationError('File must be under 5 MB.')
        return f
