from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from database.models import Student, Korrektur


# Create your views here.
def index(request):
    return HttpResponse(
        "Hier entsteht das Messaging-Portal zum Austausch zwischen Studierenden und Tutoren."
    )

# The Login View for the Tutors
@login_required
def tutor_dashboard(request):
    return render(request, 'messaging/tutor_dashboard.html')

#The Login View for the Students
#@login_required
#def student_dashboard(request):
#    return render(request, 'messaging/student_dashboard.html')

#Angepasstes Dashboard Student
@login_required
def student_dashboard(request):
    user = request.user
    email = user.email
    vorname = user.first_name
    nachname = user.last_name
    print("Erfolgreicher Login von " + vorname + nachname)

    try:
        # Den Studenten anhand der E-Mail finden
        student = Student.objects.get(email=email)
        # Matrikelnummer des Studenten erhalten
        matrikelnummer = student.martrikelnummer
    except Student.DoesNotExist:
        # Behandlung, falls kein Student mit dieser E-Mail existiert
        matrikelnummer = None

    if  matrikelnummer:
        # Alle Fehlermeldungen für die gefundene Matrikelnummer abrufen
        fehlermeldungen = Korrektur.objects.filter(ersteller=matrikelnummer)
    else:
        fehlermeldungen = []

    return render(
        request, 
        'messaging/student_dashboard.html',
        {'email': email, 
        'vorname': vorname, 
        'nachname': nachname, 
        'matrikelnummer':matrikelnummer,
        'fehlermeldungen': fehlermeldungen
        }
    )

# The logic for the custom Login View
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
     
# The Class for the log out view
class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html' 



# Chat View
def chat_view(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message_text = form.cleaned_data['message']
            # Logik zum Senden der Nachricht
    return render(request, 'messaging/chat.html', {'form': form})


     