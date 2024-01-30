from django.urls import path

from webhook.views import webhook

urlpatterns = [
    path('', webhook, name='webhook')
]
