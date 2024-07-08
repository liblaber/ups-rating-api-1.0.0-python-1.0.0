# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .time_in_transit_service_summary import TimeInTransitServiceSummary


@JsonMap(
    {
        "pickup_date": "PickupDate",
        "documents_only_indicator": "DocumentsOnlyIndicator",
        "package_bill_type": "PackageBillType",
        "service_summary": "ServiceSummary",
        "auto_duty_code": "AutoDutyCode",
        "disclaimer": "Disclaimer",
    }
)
class RatedShipmentTimeInTransit(BaseModel):
    """Container for returned Time in Transit information.  Will only be returned if request option was either "ratetimeintransit" or "shoptimeintransit" and DeliveryTimeInformation container was present in request.

    :param pickup_date: The date the user requests UPS to pickup the package from the origin. Format: YYYYMMDD. In the event this Pickup date differs from the Pickup date in the Estimated Arrival Container, a warning will be returned.  In the event this Pickup date differs from the Pickup date in the Estimated Arrival Container, a warning will be returned.
    :type pickup_date: str
    :param documents_only_indicator: If the indicator is present then the shipment was processed as Document Only., defaults to None
    :type documents_only_indicator: str, optional
    :param package_bill_type: Package bill type for the shipment. Valid values:02 - Document only 03 - Non-Document04 - Pallet, defaults to None
    :type package_bill_type: str, optional
    :param service_summary: Container for all available service information.
    :type service_summary: TimeInTransitServiceSummary
    :param auto_duty_code: Required output for International requests. If Documents indicator is set for Non-document a duty is automatically calculated. The possible values to be returned are: 01 - Dutiable02 - Non-Dutiable03 - Low-value04 - Courier Remission05 - Gift06 - Military07 - Exception08 - Line Release09 - Section 321 low value., defaults to None
    :type auto_duty_code: str, optional
    :param disclaimer: The Disclaimer is provided based upon the origin and destination country or territory codes provided in the request document. The possible disclaimers that can be returned are available in the Service Guaranteed Disclaimers table., defaults to None
    :type disclaimer: str, optional
    """

    def __init__(
        self,
        pickup_date: str,
        service_summary: TimeInTransitServiceSummary,
        documents_only_indicator: str = None,
        package_bill_type: str = None,
        auto_duty_code: str = None,
        disclaimer: str = None,
    ):
        self.pickup_date = pickup_date
        if documents_only_indicator is not None:
            self.documents_only_indicator = documents_only_indicator
        if package_bill_type is not None:
            self.package_bill_type = package_bill_type
        self.service_summary = self._define_object(
            service_summary, TimeInTransitServiceSummary
        )
        if auto_duty_code is not None:
            self.auto_duty_code = auto_duty_code
        if disclaimer is not None:
            self.disclaimer = disclaimer
