from .views import Login
from django.conf.urls import url 

urlpatterns = [
    url('login/', Login.as_view(), name = 'login')
]