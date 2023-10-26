from django.urls import path, include
from rest_framework import routers
from ace_api.viewsets import AceViewSet, AceListAllViewSet, AceRestoreViewSet

router = routers.DefaultRouter()
router.register(r'ace', AceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list', AceListAllViewSet.as_view({'get': 'list'}), name='list'),
    path('restore/<int:pk>/', AceRestoreViewSet.as_view(), name='restore'),
]
