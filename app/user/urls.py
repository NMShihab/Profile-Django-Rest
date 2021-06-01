from django.urls import path
from django.urls import path

from . import views

urlpatterns =[
    path("dummy-view/",views.DummyApiView.as_view()),
]