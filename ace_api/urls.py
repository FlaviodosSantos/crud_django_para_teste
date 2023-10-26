from django.urls import path, include
from rest_framework import routers
from ace_api.viewsets import AceViewSet

router = routers.DefaultRouter()
router.register(r'ace', AceViewSet)

urlpatterns = [
    path('',include(router.urls))
]