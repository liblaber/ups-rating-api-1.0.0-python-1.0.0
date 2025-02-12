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
class BillThirdPartyAddress(BaseModel):
    """Container for additional information for the third party UPS accounts address.

    :param address_line: The origin street address including name and number (when applicable)., defaults to None
    :type address_line: List[str], optional
    :param city: Origin city., defaults to None
    :type city: str, optional
    :param state_province_code: Origin state code., defaults to None
    :type state_province_code: str, optional
    :param postal_code: Origin postal code. The postal code must be the same as the UPS account pickup address postal code. Required for United States and Canadian UPS accounts and/or if the UPS account pickup address has a postal code. If the UPS account's pickup country or territory is US or Puerto Rico, the postal code is 5 or 9 digits. The character '-' may be used to separate the first five digits and the last four digits. If the UPS account's pickup country or territory is CA, the postal code is 6 alphanumeric characters whose format is A#A#A# where A is an uppercase letter and # is a digit., defaults to None
    :type postal_code: str, optional
    :param country_code: Origin country or territory code. Refer to the Supported Country or Territory Tables located in the Appendix.
    :type country_code: str
    """

    def __init__(
        self,
        country_code: str,
        address_line: List[str] = None,
        city: str = None,
        state_province_code: str = None,
        postal_code: str = None,
    ):
        if address_line is not None:
            self.address_line = address_line
        if city is not None:
            self.city = city
        if state_province_code is not None:
            self.state_province_code = state_province_code
        if postal_code is not None:
            self.postal_code = postal_code
        self.country_code = country_code
