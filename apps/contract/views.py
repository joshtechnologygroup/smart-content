import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from apps.account import utils as account_utils
from apps.content import utils as content_utils
from apps.contract import utils as contract_utils, contract_maps


@csrf_exempt
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
		req_action["payload"] = json.loads(request.body)

		account_utils.update_account_by_addr(content_addr, content=content)

		account_utils.broadcast_updated_content(content)

		return JsonResponse(200, {})


@require_POST
@csrf_exempt
def execute_contract(request, *args, **kwargs):

		data = json.loads(request.body)

		contract_addr = data.pop("contract", "")

		if not contract_addr:
				return JsonResponse(status=400, data={"msg": "Contract Key Missing"})

		# Extract Contract
		contract = contract_utils.get_contract(contract_addr)

		if not contract:
				return JsonResponse(status=404, data={"msg": "Contract Not Found"})

		contract_type = contract.contract.get("name")

		contract_obj = contract_maps.get_contract(contract_type)

		if not contract_obj:
				return JsonResponse(status=400, data={"msg": "Invalid Contract"})

		contract_instance = contract_obj(contract.address)

		# Hardcoded for testing, must fix
		entities = {
				"content": {
					"address": ["Content-1"]
				},
				"content_owner": {
					"req": True,
					"address": ["Account-1"]
				},
				"buyer": {
					"required": False,
					"address": ["Buyer-1"]
				},
				"verifier": {
						"required": False,
						"address": ["VER-1"]
				}
		}
		data.pop("entities")

		res = contract_maps.run_contract(contract_instance, entities, **data)

		if not res[0]:
				return JsonResponse(status=400, data={"msg": res[1], "txns": res[2]})

		return JsonResponse(status=200, data={"txns": res[2]})
