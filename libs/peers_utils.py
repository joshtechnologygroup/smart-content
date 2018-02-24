import requests

GET_ALL_PEERS_URL = ""


def get_all_peers():
    """
    Stub for API for getting all Peers in network
    In actual implementations, we get use something similar to DNS Seeding for same
    """
    request = requests.get(GET_ALL_PEERS_URL)
    return request.json()


def broadcast_to_peers(req_method, url, **kwargs):
    """
    Broadcast some information to all nodes in peer network
    """

    for peer in get_all_peers():
        requests.request(req_method, peer + url, **kwargs)
