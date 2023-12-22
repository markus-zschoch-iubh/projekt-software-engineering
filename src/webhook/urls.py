from django.urls import path

from . import views

urlpatterns = [
    path('', views.webhook)
    #path('', views.index)
]

# urlpatterns = [
#     path('webhook/', webhook, name='webhook')
# ]