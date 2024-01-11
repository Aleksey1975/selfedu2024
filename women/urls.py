from django.urls import path, re_path
from women.views import *

urlpatterns = [

    path('', index),
    path('cats/<int:cat_id>', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),


]
