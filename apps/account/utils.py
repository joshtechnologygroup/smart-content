import requests

verify_broadcast_url = ""
new_contract_url = ""
new_content_url = ""


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
        requests.post(verify_broadcast_url, data=payload)


def broadcast_new_contract(contract):
    """
    :param contract:
    :return:
    """

    payload = {
        "address": contract.address,
        "contract": contract.contract
    }
    requests.post(new_contract_url, data=payload)


def broadcast_new_content(content):
    """
    :param content:
    :return:
    """

    payload = {
        "address": content.address,
        "contract": content.contract
    }
    requests.post(new_contract_url, data=payload)
