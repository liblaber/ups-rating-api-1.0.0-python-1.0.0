# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .frs_payment_information_type import FrsPaymentInformationType
from .frs_payment_information_address import FrsPaymentInformationAddress


@JsonMap({"type_": "Type", "account_number": "AccountNumber", "address": "Address"})
class ShipmentFrsPaymentInformation(BaseModel):
    """UPS Ground Freight Pricing (GFP) Payment Information container.  Required only for GFP and when the FRSIndicator is present.

    :param type_: GFP Payment Information Type container.  GFP only.
    :type type_: FrsPaymentInformationType
    :param account_number: UPS Account Number., defaults to None
    :type account_number: str, optional
    :param address: Payer Address Container.  Address container may be present for FRS Payment Information type = 02 and required when the FRS Payment Information type = 03., defaults to None
    :type address: FrsPaymentInformationAddress, optional
    """

    def __init__(
        self,
        type_: FrsPaymentInformationType,
        account_number: str = None,
        address: FrsPaymentInformationAddress = None,
    ):
        self.type_ = self._define_object(type_, FrsPaymentInformationType)
        if account_number is not None:
            self.account_number = account_number
        if address is not None:
            self.address = self._define_object(address, FrsPaymentInformationAddress)
