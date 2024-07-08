# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .rated_package_billing_weight_unit_of_measurement import (
    RatedPackageBillingWeightUnitOfMeasurement,
)


@JsonMap({"unit_of_measurement": "UnitOfMeasurement", "weight": "Weight"})
class RatedPackageBillingWeight(BaseModel):
    """Billing Weight Container.

    :param unit_of_measurement: Unit Of Measurement Container.
    :type unit_of_measurement: RatedPackageBillingWeightUnitOfMeasurement
    :param weight: The value for the billable weight associated with the package.  When using a negotiated divisor different from the published UPS divisor (139 for inches and 5,000 for cm), the weight returned is based on the published divisor. Rates, however, are based on the negotiated divisor.
    :type weight: str
    """

    def __init__(
        self,
        unit_of_measurement: RatedPackageBillingWeightUnitOfMeasurement,
        weight: str,
    ):
        self.unit_of_measurement = self._define_object(
            unit_of_measurement, RatedPackageBillingWeightUnitOfMeasurement
        )
        self.weight = weight
