from django.http import JsonResponse

from apps.content import utils as content_utils
from django.views.decorators.http import require_POST
from libs import blockchain_utils, peers_utils


content_action_url = ""


def content_discovery_view(request):
    state = blockchain_utils.get_block_state()
    content_addresses = state.get("contents").keys()

    contents = []

    for block_address in content_addresses:
        contents.append(content_utils.get_content(block_address))

    return JsonResponse(contents)


@require_POST
def content_action_view(request, *args, **kwargs):

    content = content_utils.get_content(kwargs['content_id'])

    payload = {
        "content": content.get("address"),
        "action": kwargs["action"],
        "entities": content.get("entities"),
        "payload": request.POST.get()
    }
    peers_utils.broadcast_to_peers("post", content_action_url, data=payload)
