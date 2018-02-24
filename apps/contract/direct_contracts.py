from .base import BaseContract


class BuyContract(BaseContract):
    """
    Seller sets a specific price, and buyer pays for that price
    """

    ENTITY_BUYER = "buyer"
    ENTITY_CONTENT_OWNER = "content_owner"

    TX_TYPE_CONTENT_TRANSFER = "content_transfer"

    @property
    def req_entities(self):
        return super().req_entities() | {self.ENTITY_BUYER, self.ENTITY_CONTENT_OWNER}

    def run(self, entities, *args, **kwargs):

        self.validate_entities_structure(entities)

        value = kwargs.get("price")

        buyer_addr = self.get_addr(entities, self.ENTITY_BUYER)

        # Get the Money from Buyer
        self.get_money(buyer_addr, value)

        # First payment is to Verifier
        value = self.pay_verifier(self.get_addr(entities, self.ENTITY_VERIFIER), value)

        if value is None:
            return self.FAILURE_STATUS, "Value is set lower than verifier cut"

        # Pay content owner
        self.pay_content_owner(self.get_addr(entities, self.ENTITY_CONTENT_OWNER), value)

        # Transfer content to buyer
        self.transfer_content_to_buyer(self.get_addr(entities, self.ENTITY_CONTENT), buyer_addr)

        return self.success_return

    def get_money(self, buyer, value):
        self.transfer_money(buyer, self.address, value)

    def pay_content_owner(self, content_owner, value):
        self.transfer_money(self.address, content_owner, value)
        return value

    def transfer_content_to_buyer(self, content, buyer):

        self.transactions.append(
            {
                "to": buyer,
                "from": self.address,
                "value": content,
                "tx_type": self.TX_TYPE_CONTENT_TRANSFER
            }
        )
