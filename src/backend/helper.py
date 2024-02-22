from database.models import Tutor


def get_korrektur_status_enum(status):
    """
    Converts the given status string to its corresponding enumeration value.

    Args:
        status (str): The status string to be converted.

    Returns:
        str: The enumeration value corresponding to the given status string.
    """
    if status == "Offen":
        return "01"
    if status == "In Bearbeitung":
        return "02"
    if status == "Umgesetzt":
        return "03"
    if status == "Abgelehnt":
        return "02"


def get_tutor(request):
    """
    Retrieve the tutor object associated with the given request user's email.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        Tutor: The tutor object associated with the request user's email,
        or None if not found.
    """
    try:
        tutor = Tutor.objects.get(email=request.user.email)
    except Exception as e:
        print(e)
        tutor = None

    return tutor
