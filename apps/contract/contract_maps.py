from apps.contract import direct_contracts

CONTRACT_MAP = {
		"buy": direct_contracts.BuyContract
}


def get_contract(contract_name):
		return CONTRACT_MAP.get(contract_name)


def run_contract(contract, *args, **kwargs):
		return contract.run(*args, **kwargs)
