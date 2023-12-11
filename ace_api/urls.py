from django.urls import path
from ace_api.views import AceList

urlpatterns = [
    path('index', AceList.as_view(), name='index'),
]
