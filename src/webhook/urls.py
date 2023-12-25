from django.urls import path
from . import views

urlpatterns = [
    #path('', views.webhook, name='webhook'),
    path('', views.webhook),
    path('fehlerliste/', views.fehler_list_view, name='fehlerliste')
]
