# myapp/forms.py
# myapp/forms.py
from django import forms
from .models import Documents

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ['title', 'file']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = self.instance.uploaded_by  # Set owner to the user who uploaded the document
        if commit:
            instance.save()
        return instance