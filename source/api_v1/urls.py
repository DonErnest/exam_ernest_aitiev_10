from django.urls import path

from api_v1.views import UserProvideAccessView, DepriveUserAccessView, DownloadCounterIncrement

urlpatterns = [
    path('file/<int:pk>/access/provide', UserProvideAccessView.as_view(), name='provide_access'),
    path('file/<int:pk>/access/deprive', DepriveUserAccessView.as_view(), name='deprive_access'),
    path('file/<int:pk>/increment', DownloadCounterIncrement.as_view(), name='count_downloads')
]

app_name='api_v1'