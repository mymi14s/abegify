from allauth.account.adapter import DefaultAccountAdapter
from django.http import Http404

class NoSignupAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        # Completely disable signups
        return False

    def respond_user_inactive(self, request, user):
        # Optional: handle inactive users differently
        raise Http404
