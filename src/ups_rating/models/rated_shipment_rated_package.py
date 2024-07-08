# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .rated_package_base_service_charge import RatedPackageBaseServiceCharge
from .rated_package_transportation_charges import RatedPackageTransportationCharges
from .rated_package_service_options_charges import RatedPackageServiceOptionsCharges
from .rated_package_total_charges import RatedPackageTotalCharges
from .rated_package_billing_weight import RatedPackageBillingWeight
from .rated_package_accessorial import RatedPackageAccessorial
from .rated_package_itemized_charges import RatedPackageItemizedCharges
from .rated_package_negotiated_charges import RatedPackageNegotiatedCharges
from .rated_package_simple_rate import RatedPackageSimpleRate
from .rated_package_rate_modifier import RatedPackageRateModifier


@JsonMap(
    {
        "base_service_charge": "BaseServiceCharge",
        "transportation_charges": "TransportationCharges",
        "service_options_charges": "ServiceOptionsCharges",
        "total_charges": "TotalCharges",
        "weight": "Weight",
        "billing_weight": "BillingWeight",
        "accessorial": "Accessorial",
        "itemized_charges": "ItemizedCharges",
        "negotiated_charges": "NegotiatedCharges",
        "simple_rate": "SimpleRate",
        "rate_modifier": "RateModifier",
    }
)
class RatedShipmentRatedPackage(BaseModel):
    """RatedShipmentRatedPackage

    :param base_service_charge: Base Service Charge Container.  These charges would be returned only when subversion is greater than or equal to 1701, defaults to None
    :type base_service_charge: RatedPackageBaseServiceCharge, optional
    :param transportation_charges: Transportation Charges Container., defaults to None
    :type transportation_charges: RatedPackageTransportationCharges, optional
    :param service_options_charges: Service Options Charges Container., defaults to None
    :type service_options_charges: RatedPackageServiceOptionsCharges, optional
    :param total_charges: Total Charges Container., defaults to None
    :type total_charges: RatedPackageTotalCharges, optional
    :param weight: The weight of the package in the rated Package., defaults to None
    :type weight: str, optional
    :param billing_weight: Billing Weight Container., defaults to None
    :type billing_weight: RatedPackageBillingWeight, optional
    :param accessorial: The container for Accessorial indicators. This information would be returned only if ItemizedChargesRequested was present during Rate request. This is valid only for UPS Worldwide Express Freight and UPS Worldwide Express Freight Mid-day service request with Dry Ice or Oversize Pallet and SubVersion greater than or equal to 1707.  This is valid only for UPS Worldwide Express Freight and UPS Worldwide Express Freight Middday Service. **NOTE:** For versions >= v2403, this element will always be returned as an array. For requests using versions < v2403, this element will be returned as an array if there is more than one object and a single object if there is only 1. , defaults to None
    :type accessorial: List[RatedPackageAccessorial], optional
    :param itemized_charges: Itemized Charges are returned only when the subversion element is present and greater than or equal to '1607'.  These charges would be returned only when subversion is greater than or equal to 1607. **NOTE:** For versions >= v2403, this element will always be returned as an array. For requests using versions < v2403, this element will be returned as an array if there is more than one object and a single object if there is only 1. , defaults to None
    :type itemized_charges: List[RatedPackageItemizedCharges], optional
    :param negotiated_charges: Negotiated Rates container.  These charges would be returned only when -1) subversion is greater than or equal to 16072) if negotiated rates were requested for GFP shipments and account number is eligible to receive negotiated rates., defaults to None
    :type negotiated_charges: RatedPackageNegotiatedCharges, optional
    :param simple_rate: SimpleRate will be returned if Simple Rate  present in request, defaults to None
    :type simple_rate: RatedPackageSimpleRate, optional
    :param rate_modifier: Container for returned Rate Modifier information. Applies only if SubVersion is 2205 or greater. **NOTE:** For versions >= v2403, this element will always be returned as an array. For requests using versions < v2403, this element will be returned as an array if there is more than one object and a single object if there is only 1. , defaults to None
    :type rate_modifier: List[RatedPackageRateModifier], optional
    """

    def __init__(
        self,
        base_service_charge: RatedPackageBaseServiceCharge = None,
        transportation_charges: RatedPackageTransportationCharges = None,
        service_options_charges: RatedPackageServiceOptionsCharges = None,
        total_charges: RatedPackageTotalCharges = None,
        weight: str = None,
        billing_weight: RatedPackageBillingWeight = None,
        accessorial: List[RatedPackageAccessorial] = None,
        itemized_charges: List[RatedPackageItemizedCharges] = None,
        negotiated_charges: RatedPackageNegotiatedCharges = None,
        simple_rate: RatedPackageSimpleRate = None,
        rate_modifier: List[RatedPackageRateModifier] = None,
    ):
        if base_service_charge is not None:
            self.base_service_charge = self._define_object(
                base_service_charge, RatedPackageBaseServiceCharge
            )
        if transportation_charges is not None:
            self.transportation_charges = self._define_object(
                transportation_charges, RatedPackageTransportationCharges
            )
        if service_options_charges is not None:
            self.service_options_charges = self._define_object(
                service_options_charges, RatedPackageServiceOptionsCharges
            )
        if total_charges is not None:
            self.total_charges = self._define_object(
                total_charges, RatedPackageTotalCharges
            )
        if weight is not None:
            self.weight = weight
        if billing_weight is not None:
            self.billing_weight = self._define_object(
                billing_weight, RatedPackageBillingWeight
            )
        if accessorial is not None:
            self.accessorial = self._define_list(accessorial, RatedPackageAccessorial)
        if itemized_charges is not None:
            self.itemized_charges = self._define_list(
                itemized_charges, RatedPackageItemizedCharges
            )
        if negotiated_charges is not None:
            self.negotiated_charges = self._define_object(
                negotiated_charges, RatedPackageNegotiatedCharges
            )
        if simple_rate is not None:
            self.simple_rate = self._define_object(simple_rate, RatedPackageSimpleRate)
        if rate_modifier is not None:
            self.rate_modifier = self._define_list(
                rate_modifier, RatedPackageRateModifier
            )
