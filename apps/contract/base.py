from abc import ABCMeta, abstractmethod

from libs import finance_methods


class EntityValidationMixin:
    """
    """


class BaseContract(metaclass=ABCMeta):
    """
    Base Contract. Mainly Abstract Class which defines functions which all derived classed must explicitly define
    """

    SUCCESS_STATUS = True
    FAILURE_STATUS = False

    SUCCESS_MSG = {}

    ENTITY_CONTENT = "content"
    ENTITY_VERIFIER = "verifier"

    def __init__(self, addr):
        self.transactions = []
        self.address = addr

    @property
    def req_entities(self):
        return {self.ENTITY_CONTENT, self.ENTITY_VERIFIER}

    @property
    def verifier_cut(self):
        return 1

    @property
    def success_return(self):
        return self.SUCCESS_STATUS, self.SUCCESS_MSG, self.transactions

    def validate_entities_structure(self, entities):
        """
        :param entities:
        :return:
        """

        # Verify all required entities are present in contract
        if self.req_entities - set(entities.keys()):
            return self.FAILURE_STATUS, "One or more required entities is not present in the system"

    @abstractmethod
    def run(self, entities, *args, **kwargs):
        """
        This is the method which would be always executed first when Base Contract class is called.
        It will return a tuple:
            (<status>, <msg>, <transaction_list>)
        which indicates how contract execution went.

        Args:
            entities: List of entities who are involved in this content.
                      JSON Field, with key representing role, and value being list of addresses associated with that role

        A correct return is (SUCCESS_STATUS, SUCCESS_MSG, RELEVANT_TXNS)
        """

        return self.success_return

    def get_addr(self, entity, name):
        """
        Get address for the entity
        """
        return entity.get(name, {}).get("address")

    @staticmethod
    def transfer_money(sender, rcpt, amount):
        finance_methods.transfer_money(sender, rcpt, amount)

    def pay_verifier(self, verifier, value):

        if value > self.verifier_cut:
            self.transfer_money(self.address, verifier, self.verifier_cut)
            return value - self.verifier_cut
        else:
            return None
