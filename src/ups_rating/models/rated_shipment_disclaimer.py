# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class RatedShipmentDisclaimer(BaseModel):
    """RatedShipmentDisclaimer

    :param code: Code representing type of Disclaimer. Refer to the Appendix for possible code values.
    :type code: str
    :param description: Disclaimer description. Please refer to Appendix for possible descriptions.
    :type description: str
    """

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description
