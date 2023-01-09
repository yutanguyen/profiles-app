from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register(
    "hello-viewset", views.HelloViewSet, basename="hello-viewset"
)  # Update new
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.UserProfileFeedViewSet)


urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("login", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
