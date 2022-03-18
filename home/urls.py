from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('', index),

]
# urlpatterns += staticfiles_urlpatterns()
