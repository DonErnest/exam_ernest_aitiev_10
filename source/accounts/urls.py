from django.urls import path

from accounts.views import SignUpUserView, UserLogoutView, UserLoginView, UserDetailView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', SignUpUserView.as_view(), name='sign_up'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='view_user_files')
]

app_name='accounts'