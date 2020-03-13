from django.urls import path

from accounts.views import SignUpUserView, UserLogoutView, UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('signup/', SignUpUserView.as_view(), name='sign_up')
]

app_name='accounts'