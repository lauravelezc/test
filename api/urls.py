from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'accounts', views.accountsViewSet, basename='Cuentas')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', views.createAccountsViewSet.as_view(), name='create'),
]