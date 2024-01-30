from database.models import Messages


def ersteller_message_bei_neuer_korrektur(korrektur, student):
    message = Messages(
        student=student,
        korrektur=korrektur,
        text=korrektur.beschreibung,
    )
    message.save()

    return True
