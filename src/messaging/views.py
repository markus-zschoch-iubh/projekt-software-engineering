from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return HttpResponse(
        "Hier entsteht das Messaging-Portal zum Austausch zwischen Studierenden und Tutoren."
    )

# The Login View for the Tutors
@login_required
def tutor_dashboard(request):
    return HttpResponse("This is the Tutor Dashboard")

#The Login View for the Students
@login_required
def student_dashboard(request):
    return HttpResponse("This is the Student Dashboard")


# The logic for the Login View
class CustomLoginView(LoginView):
    # Add custom logic if needed
     def form_valid(self, form):
        response = super().form_valid(form)
        # Check user group and redirect accordingly
        if self.request.user.groups.filter(name='Tutor').exists():
            return redirect('tutor_dashboard')  
        elif self.request.user.groups.filter(name='Student').exists():
            return redirect('student_dashboard')  
        return response
     

     