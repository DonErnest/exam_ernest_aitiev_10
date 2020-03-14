from django.urls import path

from webapp.views import IndexView, FileDetailView
from webapp.views.shared_files_views import FileEditView, FileDeleteView, FileAddView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileDetailView.as_view(), name='file_detailed'),
    path('file/<int:pk>/edit/', FileEditView.as_view(), name='edit_file'),
    path('file/<int:pk>/delete/', FileDeleteView.as_view(), name='delete_file'),
    path('file/add/', FileAddView.as_view(), name='add_file'),
]

app_name='webapp'