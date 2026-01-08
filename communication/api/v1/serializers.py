from rest_framework import serializers


from communication.models import Waitlist, ContactForm

class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = ["email", "created_at"]
        read_only_fields = ["created_at"]



class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "subject", "message", "updated_at", "created_at"]
        read_only_fields = ["created_at", "updated_at"]
