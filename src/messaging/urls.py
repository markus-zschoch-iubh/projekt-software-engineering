from django.urls import path
from .views import index, CustomLoginView, tutor_dashboard, student_dashboard, chat_view
# from .views import form_valid


urlpatterns = [
    path("", index),
    path('accounts/login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('tutor_dashboard/', tutor_dashboard, name='tutor_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('chat_view/', chat_view, name='chat_view'),
]