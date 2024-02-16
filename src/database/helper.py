from django.core.mail import send_mail

def sende_email_an_studenten(message, previous_message):
    subject = "Änderung Ihrer Korrektureingabe"
    aenderung_tutor = True if message.tutor != previous_message.tutor else False
    aenderung_status = True if message.status != previous_message.status else False
    hat_nachricht = True if message.text is not None and len(message.text) > 0 else False
    
    text = f"""
        Hallo {message.student.vorname},
        Es gibt Neuigkeiten zu deinem Ticket.
    """
    text_html = f"""
        <p>Hallo {message.student.vorname},</p>
        <p>Es gibt Neuigkeiten zu deinem Ticket.</p>
    """

    text_aenderung_tutor = f"""
        Dein Ticket ist jetzt
        {message.tutor.vorname} {message.tutor.nachname} zugeordnet.
    """
    text_aenderung_tutor_html = f"""
        <p>Dein Ticket ist jetzt
        {message.tutor.vorname} {message.tutor.nachname} zugeordnet.</p>
    """

    text_aenderung_status = f"""
        Der Status deines Tickets ist jetzt: {message.get_status_display()}.
    """
    text_aenderung_status_html = f"""
        <p>Der Status deines Tickets ist jetzt: {message.get_status_display()}.</p>
    """
    
    text_nachricht = f"""
        {message.tutor.vorname} {message.tutor.nachname} hat
        dir eine Nachricht geschicht:
        {message.text}
    """
    text_nachricht_html = f"""
        <p>{message.tutor.vorname} {message.tutor.nachname} hat
        dir eine Nachricht geschicht:
            <blockquote>{message.text}</blockquote>
        </p>
    """
    
    link = f"""
        Details findest du hier:
        http://localhost:8000/messaging/korrektur/{message.korrektur.pk}/messages/
    """
    link_html = f"""
        <p>
        Details findest du
        <a href=\"http://localhost:8000/messaging/korrektur/{message.korrektur.pk}/messages/\">
        hier...
        </a>
        </p>
    """
   
    email_text = text
    email_text_html = text_html
    if aenderung_status:
        email_text = email_text + text_aenderung_status
        email_text_html = email_text_html + text_aenderung_status_html
    if aenderung_tutor:
        email_text = email_text + text_aenderung_tutor
        email_text_html = email_text_html + text_aenderung_tutor_html
    if hat_nachricht:
        email_text = email_text + text_nachricht
        email_text_html = email_text_html + text_nachricht_html
    email_text = email_text + link
    email_text_html = email_text_html + link_html
    
    send_mail(
        subject=subject,
        message=email_text,
        from_email="projektsoftwareengineering.iubh@gmail.com",
        recipient_list=[message.korrektur.ersteller.email],
        fail_silently=False,
        html_message=email_text_html
    )
    print(f"Mail sent to {message.korrektur.ersteller.email}")

    return True