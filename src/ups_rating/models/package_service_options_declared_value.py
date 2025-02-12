# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"currency_code": "CurrencyCode", "monetary_value": "MonetaryValue"})
class PackageServiceOptionsDeclaredValue(BaseModel):
    """Declared Value Container.

    :param currency_code: The IATA currency code associated with the declared value amount for the package.  Required if a value for the package declared value amount exists in the MonetaryValue tag. Must match one of the IATA currency codes. Length is not validated. UPS does not support all international currency codes. Refer to Currency Codes in the Appendix for a list of valid codes.
    :type currency_code: str
    :param monetary_value: The monetary value for the declared value amount associated with the package.  Max value of 5,000 USD for Local and 50,000 USD for Remote. Absolute maximum value is 21474836.47
    :type monetary_value: str
    """

    def __init__(self, currency_code: str, monetary_value: str):
        self.currency_code = currency_code
        self.monetary_value = monetary_value
