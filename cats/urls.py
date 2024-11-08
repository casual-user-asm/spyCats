from django.urls import include, path
from cats import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"cats", views.SpyCatsViewSet, basename="cats")
router.register(r"missions", views.MissionViewSet, basename="missions")
router.register(r"targets", views.TargetViewSet, basename="targets")


urlpatterns = [
    path("", include(router.urls)),
]
