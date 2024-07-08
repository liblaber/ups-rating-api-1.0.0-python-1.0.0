# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class ShipmentServiceOptionsReturnService(BaseModel):
    """Container for type of Return Services.

    :param code: Code for type of Return shipment. Valid values are:'2' = UPS Print and Mail Return Label '3' =UPS One-Attempt Return Label'5' = UPS Three Attempt Return Label'8' = UPS Electronic Return Label'9' = UPS Print Return Label'10' = UPS Exchange Print Return Label                            '11' = UPS Pack & Collect Service 1-Attempt Box 1 '12' = UPS Pack & Collect Service 1-Attempt Box 2 '13' = UPS Pack & Collect Service 1-Attempt Box 3 '14' = UPS Pack & Collect Service 1-Attempt Box 4 '15' = UPS Pack & Collect Service 1-Attempt Box 5 '16' = UPS Pack & Collect Service 3-Attempt Box 1 '17' = UPS Pack & Collect Service 3-Attempt Box 2 '18' = UPS Pack & Collect Service 3-Attempt Box 3 '19' = UPS Pack & Collect Service 3-Attempt Box 4 '20' = UPS Pack & Collect Service 3-Attempt Box 5  10 = UPS Exchange Print Return Label and 5 = UPS Three Attempt Return Label are not valid for UPS WorldWide Express Freight and UPS Worldwide Express Freight Midday Services. 3 = UPS One-Attempt Return Label is not valid return service with UPS Premium Care accessorial.
    :type code: str
    :param description: Description for type of Return Service., defaults to None
    :type description: str, optional
    """

    def __init__(self, code: str, description: str = None):
        self.code = code
        if description is not None:
            self.description = description
