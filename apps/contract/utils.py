from apps.account import utils as account_utils


def get_contract(address):
		# Stubbed for now to return from local DB.
		# In actual, this would hit global service
    return account_utils.find_account_by_addr(address)
