from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from database.models import Student, Korrektur, Messages
from django.urls import reverse


def get_student(request):
    """
    Retrieves the student object based on the email of the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Student: The student object corresponding to the email of the authenticated user.
                Returns None if the student is not found or an exception occurs.
    """
    try:
        student = Student.objects.get(email=request.user.email)
    except Exception as e:
        print(e)
        student = None

    return student


def index(request):
    """
    This function handles the index page of the messaging portal.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The HTTP response containing the message for the index page.
    """
    return HttpResponse(
        "Hier entsteht das Messaging-Portal zum Austausch zwischen Studierenden und Tutoren."
    )


@login_required
def tutor_dashboard(request):
    """
    Renders the tutor dashboard page.

    Args:
        request: The HTTP request object.

    Returns:
        The rendered tutor dashboard page.
    """
    return render(request, "messaging/tutor_dashboard.html")


@login_required
def student_dashboard(request):
    """
    Renders the student dashboard page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered student dashboard page.
    """
    
    user = request.user
    email = user.email
    vorname = user.first_name
    nachname = user.last_name
    student = get_student(request)
    matrikelnummer = student.martrikelnummer

    print("---- Erfolgreicher Login von " + vorname + nachname + " ----")
   
    if matrikelnummer:
        # Retrieve all error messages for the matriculation number found
        fehlermeldungen = Korrektur.objects.filter(ersteller=matrikelnummer)
        # Conversion of enum numerical values into readable designations
        for fehlermeldung in fehlermeldungen:
            fehlermeldung.aktuellerStatus = (
                fehlermeldung.get_aktuellerStatus_display()
            )
    else:
        fehlermeldungen = []

    return render(
        request,
        "messaging/student_dashboard.html",
        {
            "email": email,
            "vorname": vorname,
            "nachname": nachname,
            "matrikelnummer": matrikelnummer,
            "fehlermeldungen": fehlermeldungen,
        },
    )


class CustomLoginView(LoginView):
    """
    A custom login view that redirects users based on their group.

    Overrides the `get_success_url` method to redirect users to different URLs
    based on their group membership. If the user is a member of the 'Tutor' group,
    they will be redirected to the 'tutor_index' URL. If the user is a member of
    the 'Student' group, they will be redirected to the 'student_dashboard' URL.
    If the user does not belong to any group, the default redirection URL will be used.
    """

    def get_success_url(self):
        user = self.request.user

        # Check user group and redirect accordingly
        if user.groups.filter(name='Tutor').exists():
            return reverse('tutor_index')
        elif user.groups.filter(name='Student').exists():
            return reverse('student_dashboard')

        # Default redirection if no group is found
        return super().get_success_url()
 

class CustomLogoutView(LogoutView):
    """
    A custom view for logging out users.
    """
    template_name = "registration/logout.html"


@login_required
def korrektur_messages(request, korrektur_id):
    """
    View function for displaying and handling messages related to a specific korrektur.

    Args:
        request (HttpRequest): The HTTP request object.
        korrektur_id (int): The ID of the korrektur.

    Returns:
        HttpResponse: The HTTP response object containing the rendered template.
    """
    student = get_student(request)
    korrektur = Korrektur.objects.get(id=korrektur_id)
    messages = Messages.objects.filter(korrektur=korrektur).order_by(
        "created_at"
    )
    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.korrektur = korrektur
            message.student = student
            message.tutor = korrektur.bearbeiter
            message.save()
            return redirect("korrektur_messages", korrektur_id=korrektur_id)

    context = {"korrektur": korrektur, "messages": messages, "form": form}
    return render(request, "messaging/korrektur_messages.html", context)
