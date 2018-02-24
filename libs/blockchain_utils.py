import requests

blockchain_req_url = ""
block_req_url = ""


def getLatestBlock():
    return requests.get(blockchain_req_url).json()


def get_block_state():
    block = getLatestBlock()
    return block.get("state")


def get_block(block_addr):
    req_url = block_req_url + block_addr
    block = requests.get(req_url).json()
    return block.get("payload", {})
