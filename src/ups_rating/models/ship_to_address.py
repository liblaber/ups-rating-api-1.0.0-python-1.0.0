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
        "residential_address_indicator": "ResidentialAddressIndicator",
    }
)
class ShipToAddress(BaseModel):
    """Address Container.

    :param address_line: Destination street address including name and number (when applicable).  Max Occurrence can be 3. Length is not validated.
    :type address_line: List[str]
    :param city: Destination city.  Required if country or territory does not utilize postal codes. Length is not validated., defaults to None
    :type city: str, optional
    :param state_province_code: Destination state code., defaults to None
    :type state_province_code: str, optional
    :param postal_code: Destination postal code.  Required if country or territory utilizes postal codes (i.e. US and PR)., defaults to None
    :type postal_code: str, optional
    :param country_code: Destination country or territory code. Refer to the Supported Country or Territory Tables located in the Appendix.
    :type country_code: str
    :param residential_address_indicator: Residential Address flag. This field is a flag to indicate if the destination is a residential location. True if ResidentialAddressIndicator tag exists; false otherwise. This element does not require a value and if one is entered it will be ignored. Note: When requesting TimeInTransit information, this indicator must be passed to determine if Three Day Select or Ground shipment is eligible for Saturday Delivery at no charge. If this indicator is not present, address will be considered as commercial. Empty Tag. , defaults to None
    :type residential_address_indicator: str, optional
    """

    def __init__(
        self,
        address_line: List[str],
        country_code: str,
        city: str = None,
        state_province_code: str = None,
        postal_code: str = None,
        residential_address_indicator: str = None,
    ):
        self.address_line = address_line
        if city is not None:
            self.city = city
        if state_province_code is not None:
            self.state_province_code = state_province_code
        if postal_code is not None:
            self.postal_code = postal_code
        self.country_code = country_code
        if residential_address_indicator is not None:
            self.residential_address_indicator = residential_address_indicator
