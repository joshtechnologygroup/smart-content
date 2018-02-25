from libs import peers_utils


latest_block_req_url = "latestBlock/"
block_req_url = "block/"


def getLatestBlock():
		return peers_utils.request_from_peers("get", latest_block_req_url)


def get_block_state():
		block = getLatestBlock()
		return block.get("state")


def get_block(block_addr):
		return peers_utils.request_from_peers("get", block_req_url + str(block_addr))
