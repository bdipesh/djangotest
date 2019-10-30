
from products import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    ]

