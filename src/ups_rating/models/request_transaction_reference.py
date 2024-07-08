# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"customer_context": "CustomerContext"})
class RequestTransactionReference(BaseModel):
    """TransactionReference identifies transactions between client and server.

    :param customer_context: May be used to synchronize request/response pairs. Information in the request element is echoed back in the response., defaults to None
    :type customer_context: str, optional
    """

    def __init__(self, customer_context: str = None):
        if customer_context is not None:
            self.customer_context = customer_context
