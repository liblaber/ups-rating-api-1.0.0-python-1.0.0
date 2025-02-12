# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"account_number": "AccountNumber"})
class ShipmentChargeBillShipper(BaseModel):
    """Container for the BillShipper billing option.  This element or its sibling element, BillReceiver, BillThirdParty or ConsigneeBilledIndicator, must be present but no more than one can be present.

    :param account_number: UPS account number  Must be the same UPS account number as the one provided in Shipper/ShipperNumber.
    :type account_number: str
    """

    def __init__(self, account_number: str):
        self.account_number = account_number
