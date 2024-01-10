from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from database.models import Student, Korrektur, Messages


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

        # Umwandlung der Enum-Zahlenwerte in lesbare Bezeichnungen
        for fehlermeldung in fehlermeldungen:
            fehlermeldung.typ = fehlermeldung.get_typ_display()
            fehlermeldung.aktuellerStatus = fehlermeldung.get_aktuellerStatus_display()

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

# Studentenobjekt des aktuellen Benutzers erhalten
def get_student(request):
    try:
        user = request.user
        email = user.email
        # Den Studenten anhand der E-Mail finden
        student = Student.objects.get(email=email)
    except Exception as e:
        print(e)
        student = None

    return student 

# The Chat View for the Students
def korrektur_messages(request, korrektur_id):
    student = get_student(request)
    korrektur = Korrektur.objects.get(id=korrektur_id)
    messages = Messages.objects.filter(korrektur=korrektur).order_by('-created_at')
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.korrektur = korrektur
            message.student = student
            message.tutor = korrektur.bearbeiter
            message.save()
            return redirect('korrektur_messages', korrektur_id=korrektur_id)

    context = {'korrektur': korrektur, 'messages': messages, 'form': form}
    return render(request, 'messaging/korrektur_messages.html', context)




     