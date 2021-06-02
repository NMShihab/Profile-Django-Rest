from django.urls import path
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("dummy-viewset",views.DummyViewSet,basename="dummy-viewset")
router.register("profile",views.UserProfileViewSet)

urlpatterns =[
    path("dummy-view/",views.DummyApiView.as_view()),
    path("",include(router.urls)),
]