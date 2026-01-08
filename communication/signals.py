from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.template import Template, Context
from django.template.loader import render_to_string

from abegify.utils.email import send_email
from .models import EmailTemplate
from .models import Waitlist, ContactForm

@receiver(post_save, sender=Waitlist)
def notify_waitlist(sender, instance, created, **kwargs):
    if created:
        email_template = EmailTemplate.objects.get(name='Waitlist Added')
        html_template = render_to_string('emails/waitlist.html', { "year": date.today().year })
        send_email.enqueue(email_template.subject, [instance.email], html_template)


@receiver(post_save, sender=ContactForm)
def notify_contact_form(sender, instance, created, **kwargs):
    if True:
        email_template = EmailTemplate.objects.get(name='Contact Form')
        html_template = render_to_string('emails/contact_form.html', { 
            "year": date.today().year, 
            "message": instance.message,
            "email": instance.email, 
            "name":instance.name,
            "subject": instance.subject
        })

        # send to company
        send_email.enqueue(instance.subject, [settings.DEFAULT_FROM_EMAIL], f"""<p>Name: {instance.name}</p><p>Email: {instance.email}</p>"""+instance.message)

        # send to customer
        template = Template(html_template)
        context = Context({})
        send_email.enqueue(email_template.subject, [instance.email], template.render(context))