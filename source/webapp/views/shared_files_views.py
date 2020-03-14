from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, UpdateView, CreateView

from webapp.forms import SharedFileForm
from webapp.models import SharedFile, ACCESS_CLOSED, ACCESS_PUBLIC
from webapp.views.base_views import SimpleSearchView


class IndexView(SimpleSearchView):
    template_name = 'index.html'
    queryset = SharedFile.objects.filter(sharing_type=ACCESS_PUBLIC)
    context_object_name = 'sharedfiles'
    paginate_by = 10
    paginate_orphans = 2
    ordering = ['-uploaded']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        print(context)
        return context

    def get_query(self):
        return Q(name__icontains=self.search_query)


class FileDetailView(DetailView):
    model = SharedFile
    template_name = 'file/detail.html'


class FileEditView(UserPassesTestMixin, UpdateView):
    model = SharedFile
    form_class = SharedFileForm
    template_name = 'file/update.html'

    def get_form_class(self):

    def get_success_url(self):
        return reverse('webapp:file_detailed', kwargs={'pk': self.object.pk})

    def get_file(self):
        file_pk = self.kwargs['pk']
        file = get_object_or_404(SharedFile, pk=file_pk)
        return file

    def test_func(self):
        file = self.get_file()
        if file.user_id:
            return file.user_id == self.request.user or self.request.user.has_perm('webapp.change_sharedfile')
        else:
            return self.request.user.has_perm('webapp.change_sharedfile')

class FileDeleteView(UserPassesTestMixin, View):
    def get_file(self):
        file_pk = self.kwargs['pk']
        file = get_object_or_404(SharedFile, pk=file_pk)
        return file

    def get(self, request, *args, **kwargs):
        file = self.get_file()
        file.delete()
        return HttpResponseRedirect(reverse('webapp:index'))

    def test_func(self):
        file = self.get_file()
        if file.user_id:
            return file.user_id == self.request.user or self.request.user.has_perm('webapp.change_sharedfile')
        else:
            return self.request.user.has_perm('webapp.change_sharedfile')

class FileAddView(CreateView):
    model = SharedFile
    form_class = SharedFileForm
    template_name = 'file/create.html'

    def get_success_url(self):
        return reverse('webapp:file_detailed', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            if request.user.is_authenticated:
                self.object.user_id = request.user
                self.object.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)