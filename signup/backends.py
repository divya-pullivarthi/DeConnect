from django.contrib.auth.backends import BaseBackend
from signup.models import Member


class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Member.objects.get(email=username.lower())
            if user.check_password(password):
                return user
        except Member.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Member.objects.get(pk=user_id)
        except Member.DoesNotExist:
            return None