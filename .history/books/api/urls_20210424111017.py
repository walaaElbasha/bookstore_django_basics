from fjango.urls import path
from . import views


urlpatterns=[
    path("",views.index),
    path("list",views.create),
    ]