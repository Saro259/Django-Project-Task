from django.urls import path
from .views import sign_up, employee_login, logout_view

app_name = 'userapp'

urlpatterns = [

    path('sign-up/', sign_up, name='sign_up'),
    path('login/', employee_login, name='login'),
    path('logout/', logout_view, name='logout'),
]
