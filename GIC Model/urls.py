from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.PredictView)
urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('Display/Renewal', views.display_predict_renewal, name = "file"),
    path('Display/Purchase', views.display_predict_purchase, name = "file"),
    path('Download/Renewal', views.download_predict_renewal, name = "file"),
    path('Download/Purchase', views.download_predict_purchase, name = "file"),
]