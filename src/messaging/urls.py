from django.urls import path
from .views import CustomLoginView
from . import views
from .views import tutor_dashboard
from .views import student_dashboard


urlpatterns = [
    path("", views.index),
    path('accounts/login/', CustomLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('tutor_dashboard/', tutor_dashboard, name='tutor_dashboard'),
    path('student_dashboard/', student_dashboard, name='student_dashboard')
]