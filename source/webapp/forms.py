from django import forms

from webapp.models import SharedFile


class NameSearchForm(forms.Form):
    in_article_name = forms.CharField(max_length=100, label='Название файла', required=False)


class SharedFileForm(forms.ModelForm):
    class Meta:
        model = SharedFile
        fields = ['name', 'file', 'sharing_type']


class SharedFileAnonymusForm(forms.ModelForm):
    class Meta:
        model = SharedFile
        fields = ['name', 'file']
