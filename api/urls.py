from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('detail', views.BankViewset, basename='ifsc_detail')
router.register('list', views.BankListViewset, basename='branch_list')


urlpatterns = [
    path('', include(router.urls)),
]