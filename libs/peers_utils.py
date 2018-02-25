import requests

GET_ALL_PEERS_URL = ""


def get_all_peers():
		"""
		Stub for API for getting all Peers in network
		In actual implementations, we get use something similar to DNS Seeding for same
		"""

		# request = requests.get(GET_ALL_PEERS_URL)
		# return request.json()
		# Stubbing for now
		return ["http://192.168.0.180:3001/", "http://192.168.0.180:3002/", "http://192.168.0.180:3003/"]


def request_from_peers(req_method, url, **kwargs):
		"""
		Request some information from peers.
		"""

		# TODO: Make requests in parallel, and stop as soon as any response achieved

		peers = get_all_peers()

		for peer in peers:
				response = requests.request(req_method, peer + url, **kwargs)
				data = response.json()
				if data:
						return data


def broadcast_to_peers(req_method, url, **kwargs):
		"""
		Broadcast some information to all nodes in peer network
		"""

		peers = get_all_peers()

		for peer in peers:
				requests.request(req_method, peer + url, **kwargs)
