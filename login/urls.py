from django.urls import path
from login.views import login_request, logout_request
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_request, name="login"),
    path('logout', LogoutView.as_view(template_name='./practicaMVT/templates/login/logout.html'), name = 'Logout'),

]
