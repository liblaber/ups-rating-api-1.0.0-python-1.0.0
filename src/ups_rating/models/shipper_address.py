# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "address_line": "AddressLine",
        "city": "City",
        "state_province_code": "StateProvinceCode",
        "postal_code": "PostalCode",
        "country_code": "CountryCode",
    }
)
class ShipperAddress(BaseModel):
    """Address Container.  If the ShipFrom container is not present then this address will be used as the ShipFrom. If this address is used as the ShipFrom, the shipment will be rated from this origin address.

    :param address_line: Shipper's street address including name and number (when applicable).  Maximum Occurrence should be three. Length is not validated.
    :type address_line: List[str]
    :param city: Shipper's city.  Required if country or territory does not utilize postal codes. Length is not validated., defaults to None
    :type city: str, optional
    :param state_province_code: Shipper's state code.  Length is not validated., defaults to None
    :type state_province_code: str, optional
    :param postal_code: Shipper's postal code.  Length is not validated., defaults to None
    :type postal_code: str, optional
    :param country_code: Country or Territory code. Refer to the Supported Country or Territory Tables located in Appendix.
    :type country_code: str
    """

    def __init__(
        self,
        address_line: List[str],
        country_code: str,
        city: str = None,
        state_province_code: str = None,
        postal_code: str = None,
    ):
        self.address_line = address_line
        if city is not None:
            self.city = city
        if state_province_code is not None:
            self.state_province_code = state_province_code
        if postal_code is not None:
            self.postal_code = postal_code
        self.country_code = country_code
