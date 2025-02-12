# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .estimated_arrival_arrival import EstimatedArrivalArrival
from .estimated_arrival_pickup import EstimatedArrivalPickup


@JsonMap(
    {
        "arrival": "Arrival",
        "business_days_in_transit": "BusinessDaysInTransit",
        "pickup": "Pickup",
        "day_of_week": "DayOfWeek",
        "customer_center_cutoff": "CustomerCenterCutoff",
        "delay_count": "DelayCount",
        "holiday_count": "HolidayCount",
        "rest_days": "RestDays",
        "total_transit_days": "TotalTransitDays",
    }
)
class ServiceSummaryEstimatedArrival(BaseModel):
    """Container for the Time-In-Transit arrival information by service

    :param arrival: Container for the Time-In-Transit arrival information by service. This is the most accurate delivery information available via the Rating API and will reflect changes in delivery schedules due to peak business seasons or holidays.
    :type arrival: EstimatedArrivalArrival
    :param business_days_in_transit: Number of business days from Origin to Destination Locations.
    :type business_days_in_transit: str
    :param pickup: The date and pick up time container.
    :type pickup: EstimatedArrivalPickup
    :param day_of_week: Day of week for arrival. Valid values are: MONTUEWEDTHUFRISAT
    :type day_of_week: str
    :param customer_center_cutoff: Customer Service call time. Returned for domestic as well as international requests., defaults to None
    :type customer_center_cutoff: str, optional
    :param delay_count: Number of days delayed at customs. Returned for International requests., defaults to None
    :type delay_count: str, optional
    :param holiday_count: Number of National holidays during transit. Returned for International requests., defaults to None
    :type holiday_count: str, optional
    :param rest_days: Number of rest days, i.e. non movement. Returned for International requests., defaults to None
    :type rest_days: str, optional
    :param total_transit_days: The total number of days in transit from one location to the next. Returned for International requests., defaults to None
    :type total_transit_days: str, optional
    """

    def __init__(
        self,
        arrival: EstimatedArrivalArrival,
        business_days_in_transit: str,
        pickup: EstimatedArrivalPickup,
        day_of_week: str,
        customer_center_cutoff: str = None,
        delay_count: str = None,
        holiday_count: str = None,
        rest_days: str = None,
        total_transit_days: str = None,
    ):
        self.arrival = self._define_object(arrival, EstimatedArrivalArrival)
        self.business_days_in_transit = business_days_in_transit
        self.pickup = self._define_object(pickup, EstimatedArrivalPickup)
        self.day_of_week = day_of_week
        if customer_center_cutoff is not None:
            self.customer_center_cutoff = customer_center_cutoff
        if delay_count is not None:
            self.delay_count = delay_count
        if holiday_count is not None:
            self.holiday_count = holiday_count
        if rest_days is not None:
            self.rest_days = rest_days
        if total_transit_days is not None:
            self.total_transit_days = total_transit_days
