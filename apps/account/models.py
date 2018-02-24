from django.contrib.postgres.fields import JSONField
from django.db import models

from apps.user import models as user_models


class Account(models.Model):
    """
        Stub for externally owned Accounts services
    """

    CONTENT = 1
    CONTRACT = 2
    USER = 3

    CATEGORY_CHOICES = (
        (CONTENT, "Content"),
        (CONTRACT, "Contract"),
        (USER, "User")
    )

    address = models.TextField(null=False, blank=False)
    category = models.PositiveIntegerField(choices=CATEGORY_CHOICES)

    # User Account Settings
    profile = models.ForeignKey(user_models.Profile, null=True, on_delete=models.CASCADE)

    # Contract Account Settings
    contract = JSONField(null=True, default={})

    # Content Settings
    content = JSONField(null=True, default={})
