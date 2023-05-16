from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    #path('', views.cardiology_prediction, name="cardiology_prediction"),
    path('', views.index, name = "index"),
    path('result/', views.result, name = "result"),
    path('predict/',views.predict, name="predict"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

