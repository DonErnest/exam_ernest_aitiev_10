from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from webapp.models import SharedFile


class IndexView(ListView):
    template_name = 'index.html'
    queryset = SharedFile.objects.all()
    context_object_name = 'sharedfiles'
