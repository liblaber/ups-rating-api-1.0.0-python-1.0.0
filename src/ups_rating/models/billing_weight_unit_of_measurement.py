# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"code": "Code", "description": "Description"})
class BillingWeightUnitOfMeasurement(BaseModel):
    """Unit Of Measurement Container.

    :param code: The code associated with the unit of measure for the billable weight of a shipment. Possible values are KGS or LBS.
    :type code: str
    :param description: The description for the billable weight associated with the shipment.
    :type description: str
    """

    def __init__(self, code: str, description: str):
        self.code = code
        self.description = description
