from database.models import Messages


def ersteller_message_bei_neuer_korrektur(korrektur, student):
    """
    Creates a new message for the student when a new correction is made.

    Args:
        korrektur (Korrektur): The correction object.
        student (Student): The student object.

    Returns:
        bool: True if the message is successfully created and saved.
    """
    message = Messages(
        student=student,
        korrektur=korrektur,
        text=korrektur.beschreibung,
    )
    message.save()

    return True
