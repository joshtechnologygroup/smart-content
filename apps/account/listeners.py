from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from apps.account import models as account_models, utils as account_utils


broadcast_map = {
    account_models.Account.USER: account_utils.broadcast_new_user_account,
    account_models.Account.CONTRACT: account_utils.broadcast_new_contract,
    account_models.Account.CONTENT: account_utils.broadcast_new_content,
}


@receiver(post_save, sender=account_models.Account)
def broadcast_new_account(sender, instance, is_created, **kwargs):
    """
    Broadcast new account being created
    """

    if is_created:

        if instance.category == account_models.Account.USER:
            broadcast_map.get(instance.category)(instance)
