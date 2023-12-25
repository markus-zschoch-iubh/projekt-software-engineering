from django.urls import path
from webhook.views import webhook, fehler_list_view, fehler_edit_view, bestaetigungsseite_view

urlpatterns = [
    #path('', views.webhook, name='webhook'),
    path('', webhook),
    path('fehlerliste/', fehler_list_view, name='fehlerliste'),
    path('fehler/bearbeiten/<int:id>/', fehler_edit_view, name='fehler_bearbeiten'),
    path('bestaetigung/<int:id>/', bestaetigungsseite_view, name='bestaetigungsseite'),

]
