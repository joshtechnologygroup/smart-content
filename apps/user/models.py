import unicodedata

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(PermissionsMixin, AbstractBaseUser):
    """
        User Model.
        This model serves only two purposes:
            1. Stores Unique Identifier for USER across complete system
            2. Authenticate user

        Only the fields which serve purpose in Authentication must exist here

        For general interaction with user, use Profile Model
    """

    USERNAME_FIELD = "username"

    username = models.CharField(_("Authentication Username"), max_length=50, unique=True)
    request_to_verify = models.BooleanField(default=False)
    verification_signature = models.TextField(null=True)


class Profile(models.Model):
    """
        Stores all information related to user
        This is the general model which would be used when interacting with APIs
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_("Associated User"))
    full_name = models.TextField(_("Preferred full name"))
    short_name = models.CharField(_("Preferred short name"), max_length=100)

    def normalize(self, field_name):
        field_val = getattr(self, field_name)
        return unicodedata.normalize('NFKC', field_val) if field_val else field_val

    def clean_full_name(self):
        setattr(self, "full_name", self.normalize("full_name"))

    def clean_short_name(self):
        setattr(self, "short_name", self.normalize("short_name"))

    def __str__(self):
        return self.full_name
