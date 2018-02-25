from django.http import JsonResponse
from django.views.decorators.http import require_POST

from apps.account import utils as account_utils
from apps.content import utils as content_utils
from apps.contract import utils as contract_utils


@require_POST
def associate_action_with_contract_view(request, *args, **kwargs):

    content = content_utils.get_content(kwargs['content_id'])
    contract = contract_utils.get_contract(kwargs["contract_id"])

    content_addr = content.get("address")

    content_obj = account_utils.find_account_by_addr(content_addr)
    if not content_obj:
        return JsonResponse(404, {})

    actions = content_obj.content.get("actions")
    req_action = actions.get(kwargs['action'])

    if not req_action:
        actions[kwargs['action']] = {}

    req_action["contract"] = contract
    req_action["payload"] = request.POST.data

    account_utils.update_account_by_addr(content_addr, content=content)

    account_utils.broadcast_updated_content(content)

    return JsonResponse(200, {})
