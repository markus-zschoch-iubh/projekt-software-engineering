import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from database.models import Korrektur, Student, Kurs, Kursmaterial
from messaging.helper import ersteller_message_bei_neuer_korrektur


def get_student_from_json(key):
    """
    Find a student object based on the email from the JSON.

    Args:
        key (str): The email of the student.

    Returns:
        Student or None: The student object if found, otherwise None.
    """
    try:
        student = Student.objects.get(email=key)
    except Exception as e:
        print(e)
        student = None

    return student


def get_kurs_from_json(key):
    """
    Retrieves a Kurs object based on the provided key.

    Args:
        key (str): The kurzname of the Kurs to retrieve.

    Returns:
        Kurs: The retrieved Kurs object, or None if not found.
    """
    try:
        kurs = Kurs.objects.get(kurzname=key)
    except Exception as e:
        print(e)
        kurs = None

    return kurs


def get_kursmaterial_from_json(kurs, typ):
    """
    Retrieves the kursmaterial object based on the provided kurs and typ.

    Args:
        kurs (object): The kurs object.
        typ (str): The typ value.

    Returns:
        Kursmaterial: The kursmaterial object if found, otherwise None.
    """
    try:
        kursmaterial = Kursmaterial.objects.get(kurs=kurs, typ=typ)
    except Exception as e:
        print(e)
        kursmaterial = None

    return kursmaterial


@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    """
    Handle incoming webhook requests. Creates new Korrektur objects
    based on the incoming JSON.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        JsonResponse: The response JSON.

    Raises:
        JSONDecodeError: If the request body contains invalid JSON.
    """

    if request.method == "POST":
        print("WEBHOOK ERKENNT POST")
        try:
            data = json.loads(request.body)
            print("Neue Meldung beim Webhook eingegangen: " + str(data))

            # Save received JSON temporarily
            with open("webhook/inbox.json", "w", encoding="utf-8") as inbox:
                json.dump(data, inbox, ensure_ascii=False, indent=4)

            # Find student by email
            student = get_student_from_json(data["ersteller-email"])
            print("Studentenobjekt des Senders: " + str(student))

            # Check reported course and get course instance
            kurs = get_kurs_from_json(data["kurs"])
            print("Kursobjekt: " + str(kurs))

            # Check reported course material and get course material instance
            kursmaterial = get_kursmaterial_from_json(
                kurs, data["kursmaterial"]
            )
            print("Kursmaterialobjekt: " + str(kursmaterial))

            # Check if student, course or course material is not found
            if student is None or kurs is None or kursmaterial is None:
                print("Student, Kurs oder Kursmaterial nicht gefunden")
                return JsonResponse(
                    {
                        "error": """Student, Kurs oder
                        Kursmaterial nicht gefunden"""
                    },
                    status=400,
                )

            # Create Korrektur-object
            print("Korrektur-Objekt erstellen...")
            korrektur = Korrektur.objects.create(
                ersteller=student,
                kurs=kurs,
                kursmaterial=kursmaterial,
                beschreibung=data["beschreibung"],
            )
            print("Korrektur-Objekt erstellt")

            # Generate initial message upon creation of the correction
            ersteller_message_bei_neuer_korrektur(korrektur, student)

            return JsonResponse(
                {"status": "Erfolgreich empfangen"}, status=200
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Ungueltiges JSON"}, status=400)
    else:
        return JsonResponse({"error": "Nur POST-Methode erlaubt"}, status=405)
