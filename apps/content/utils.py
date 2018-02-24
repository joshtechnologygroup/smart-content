from libs import blockchain_utils


def get_content(block_address):
    return  blockchain_utils.get_block(block_address)
