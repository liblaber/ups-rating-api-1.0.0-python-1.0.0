# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"currency_code": "CurrencyCode", "monetary_value": "MonetaryValue"})
class TransportationChargesGrossCharge(BaseModel):
    """Gross Transportation Charges Container

    :param currency_code: The IATA currency code associated with the transportation costs for the shipment.
    :type currency_code: str
    :param monetary_value: Total charges Monetary value. Valid values are from 0 to 9999999999999999.99
    :type monetary_value: str
    """

    def __init__(self, currency_code: str, monetary_value: str):
        self.currency_code = currency_code
        self.monetary_value = monetary_value
