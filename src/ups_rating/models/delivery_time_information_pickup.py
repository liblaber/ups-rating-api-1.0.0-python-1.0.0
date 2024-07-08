# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"date_": "Date", "time": "Time"})
class DeliveryTimeInformationPickup(BaseModel):
    """Pickup container.

    :param date_: Shipment Date; The Pickup date is a Shipment Date and it is a required input field.  The user is allowed to query up to 35 days into the past and 60 days into the future. Format: YYYYMMDD  If a date is not provided, it will be defaulted to the current system date.
    :type date_: str
    :param time: Reflects the time the package is tendered to UPS for shipping (can be dropped off at UPS or picked up by UPS).  Military Time Format HHMMSS or HHMM.   Invalid pickup time will not be validated., defaults to None
    :type time: str, optional
    """

    def __init__(self, date_: str, time: str = None):
        self.date_ = date_
        if time is not None:
            self.time = time
