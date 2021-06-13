from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'login$', login_user ),
    url(r'register$', register ),
    url(r'room$', room ),
    url(r'show_game$', show_game ),
]