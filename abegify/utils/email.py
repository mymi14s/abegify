from django.tasks import task
from django.core.mail import EmailMessage
from django.conf import settings


@task
def send_email(subject, recipients, body, cc=None, body_type='html'):
    """
    Send an email using Django's EmailMessage.

    Parameters:
    - subject: str - Subject of the email
    - recipients: list[str] - List of recipient email addresses
    - body: str - Email body
    - cc: list[str] or None - Optional CC recipients
    - body_type: str - 'text' or 'html' (default: 'text')
    """
    if not recipients:
        raise ValueError("Recipients list cannot be empty.")

    if cc is None:
        cc = []

    email = EmailMessage(
        subject=subject,
        body=body,
        from_email=f"Abegify <{getattr(settings, 'DEFAULT_FROM_EMAIL')}>",
        to=recipients,
        cc=cc,
    )

    if body_type.lower() == 'html':
        email.content_subtype = 'html'

    email.send(fail_silently=False)
