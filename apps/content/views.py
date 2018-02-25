import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from apps.content import utils as content_utils
from libs import blockchain_utils, peers_utils


content_action_url = "executeContract/"


def content_discovery_view(request):
    state = blockchain_utils.get_block_state()
    content_addresses = state.get("content", {}).values()

    print("Content Addresses", content_addresses)

    contents = []

    for block_address in content_addresses:
        contents.append(content_utils.get_content(block_address))

    return JsonResponse(data=contents, status=200, safe=False)


@csrf_exempt
@require_POST
def content_action_view(request, *args, **kwargs):
    """
    Execute An Action for Content
    """

    content = content_utils.get_content(kwargs['content_id'])

    data = json.loads(request.body)
    buyer = data.get("buyer")
    entities = content.get("data", {}).get("content", {}).get("entities", {})

    buyer_entities = entities.get("buyer", {})

    if buyer_entities:
        buyer_entities["address"].append(buyer)

    else:
        entities["buyer"] = {
            "required": False,
            "address": [buyer]
        }

    payload = {
        "content": content.get("data", {}).get("address", ""),
        "action": kwargs["action"],
        "entities": entities,
        "payload": data
    }

    peers_utils.broadcast_to_peers("post", content_action_url, data=payload)

    return JsonResponse(status=200, data={})
