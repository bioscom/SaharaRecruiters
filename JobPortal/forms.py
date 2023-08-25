from django.forms import ModelForm
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ApplyForm(ModelForm):
    class Meta:
        model=Candidates
        fields="__all__"
        

class JobPostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model=CompanyOld
        #fields="__all__"
        #fields=('user', 'name', 'position', 'description', 'salaryfrom', 'salaryto', 'salaryterms', 'experience', 'Location', 'JobType',)
        fields=('name', 'position', 'description', 'salaryfrom', 'salaryto', 'salaryterms', 'experience', 'Location', 'JobType',)

        # widgets = {
        #     'description': forms.Textarea(attrs={'rows':5, 'cols':10}),
        #     # 'eventtype': forms.Select(attrs={'placeholder': 'In person or virtual?', 'class': 'form-control'}),
        #     # 'virtual_type':forms.RadioSelect(choices=[(1, 'Zoom'), (2, 'Google Meet'), (3, 'Skype'), (4, 'TeamViewer'), (5, 'Free Conference Call')]),
        # }