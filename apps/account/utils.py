from apps.account import models as account_models
from libs import peers_utils

verify_broadcast_url = ""
new_contract_url = ""
new_content_url = ""
updated_content_url = ""


def broadcast_new_user_account(account):
    """
    :param account:
    :return:
    """

    if account.profile.user.request_to_verify:
        payload = {
            "user": account.profile.username,
            "address": account.address,
            "verification_signature": account.profile.user.verification_signature
        }
        peers_utils.broadcast_to_peers("post", verify_broadcast_url, data=payload)


def broadcast_new_contract(contract):
    """
    :param contract:
    :return:
    """

    payload = {
        "address": contract.address,
        "contract": contract.contract
    }
    peers_utils.broadcast_to_peers("post", new_contract_url, data=payload)


def broadcast_content(content, url):
    """
    :param content:
    :return:
    """
    entities = content.content.get("entities")
    req_trusted_entities = []

    for value in entities.values():
        is_required = value.get("role")
        if is_required:
            req_trusted_entities.extend(value.get("address", []))

    payload = {
        "address": content.address,
        "entities": req_trusted_entities,
        "content": content.content
    }
    peers_utils.broadcast_to_peers("post", url, data=payload)


def broadcast_new_content(content):
    """
    :param content:
    :return:
    """
    broadcast_content(content, new_content_url)


def broadcast_updated_content(content):
    """
    :param content:
    :return:
    """
    broadcast_content(content, updated_content_url)


def find_account_by_addr(addr):
    """
    Stub to hit the account and get relevant details
    Right now mocked to hit and get from PostgreSQL
    :param addr: 
    :return: 
    """
    return account_models.Account.objects.filter(address=addr).first()


def update_account_by_addr(addr, **kwargs):
    account_models.Account.objects.filter(address=addr).update(**kwargs)
