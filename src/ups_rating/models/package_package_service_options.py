# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .package_service_options_delivery_confirmation import (
    PackageServiceOptionsDeliveryConfirmation,
)
from .package_service_options_access_point_cod import (
    PackageServiceOptionsAccessPointCod,
)
from .package_service_options_cod import PackageServiceOptionsCod
from .package_service_options_declared_value import PackageServiceOptionsDeclaredValue
from .package_service_options_shipper_declared_value import (
    PackageServiceOptionsShipperDeclaredValue,
)
from .package_service_options_insurance import PackageServiceOptionsInsurance
from .package_service_options_haz_mat import PackageServiceOptionsHazMat
from .package_service_options_dry_ice import PackageServiceOptionsDryIce


@JsonMap(
    {
        "delivery_confirmation": "DeliveryConfirmation",
        "access_point_cod": "AccessPointCOD",
        "cod": "COD",
        "declared_value": "DeclaredValue",
        "shipper_declared_value": "ShipperDeclaredValue",
        "shipper_release_indicator": "ShipperReleaseIndicator",
        "proactive_indicator": "ProactiveIndicator",
        "refrigeration_indicator": "RefrigerationIndicator",
        "insurance": "Insurance",
        "ups_premium_care_indicator": "UPSPremiumCareIndicator",
        "haz_mat": "HazMat",
        "dry_ice": "DryIce",
    }
)
class PackagePackageServiceOptions(BaseModel):
    """PackageServiceOptions container.

    :param delivery_confirmation: Delivery Confirmation Container. For a list of valid origin/destination countries or territories please refer to appendix.  DeliveryConfirmation and COD are mutually exclusive., defaults to None
    :type delivery_confirmation: PackageServiceOptionsDeliveryConfirmation, optional
    :param access_point_cod: Access Point COD indicates Package COD is requested for a shipment.  Valid only for : 01 - Hold For Pickup At UPS Access Point, Shipment Indication type. Package Access Point COD is valid only for shipment without return service from US/PR to US/PR and CA to CA. Not valid with (Package) COD., defaults to None
    :type access_point_cod: PackageServiceOptionsAccessPointCod, optional
    :param cod: COD Container. Indicates COD is requested.   Valid for the following country or territory combinations: US/PR to US/PRCA to CACA to USNot allowed for CA to US for packages that are designated as Letters or Envelopes., defaults to None
    :type cod: PackageServiceOptionsCod, optional
    :param declared_value: Declared Value Container., defaults to None
    :type declared_value: PackageServiceOptionsDeclaredValue, optional
    :param shipper_declared_value: Shipper Paid Declared Value Charge at Package level.   Valid for UPS World Wide Express Freight shipments., defaults to None
    :type shipper_declared_value: PackageServiceOptionsShipperDeclaredValue, optional
    :param shipper_release_indicator: The presence indicates that the package may be released by driver without a signature from the consignee.  Empty Tag. Only available for US50/PR to US50/PR packages without return service., defaults to None
    :type shipper_release_indicator: str, optional
    :param proactive_indicator: Any value associated with this element will be ignored. If present, the package is rated for UPS Proactive Response and proactive package tracking.Contractual accessorial for health care companies to allow package monitoring throughout the UPS system.  Shippers account needs to have valid contract for UPS Proactive Response., defaults to None
    :type proactive_indicator: str, optional
    :param refrigeration_indicator: Presence/Absence Indicator. Any value is ignored. If present, indicates that the package contains an item that needs refrigeration.  Shippers account needs to have a valid contract for Refrigeration., defaults to None
    :type refrigeration_indicator: str, optional
    :param insurance: Insurance Accesorial. Only one type of insurance can exist at a time on the shipment. Valid for UPS World Wide Express Freight shipments., defaults to None
    :type insurance: PackageServiceOptionsInsurance, optional
    :param ups_premium_care_indicator: The UPSPremiumCareIndicator indicates special handling is required for shipment having controlled substances.  Empty Tag means indicator is present. Valid only for Canada to Canada movements. Available for the following Return Services: - Returns Exchange (available with a contract) - Print Return Label - Print and Mail - Electronic Return Label - Return Service Three Attempt May be requested with following UPS services: - UPS Express® Early - UPS Express - UPS Express Saver - UPS Standard. Not available for packages with the following: - Delivery Confirmation - Signature Required - Delivery Confirmation - Adult Signature Required. , defaults to None
    :type ups_premium_care_indicator: str, optional
    :param haz_mat: Container to hold HazMat information.  Applies only if SubVersion is greater than or equal to 1701., defaults to None
    :type haz_mat: PackageServiceOptionsHazMat, optional
    :param dry_ice: Container to hold Dry Ice information.  Lane check will happen based on postal code/ city., defaults to None
    :type dry_ice: PackageServiceOptionsDryIce, optional
    """

    def __init__(
        self,
        delivery_confirmation: PackageServiceOptionsDeliveryConfirmation = None,
        access_point_cod: PackageServiceOptionsAccessPointCod = None,
        cod: PackageServiceOptionsCod = None,
        declared_value: PackageServiceOptionsDeclaredValue = None,
        shipper_declared_value: PackageServiceOptionsShipperDeclaredValue = None,
        shipper_release_indicator: str = None,
        proactive_indicator: str = None,
        refrigeration_indicator: str = None,
        insurance: PackageServiceOptionsInsurance = None,
        ups_premium_care_indicator: str = None,
        haz_mat: PackageServiceOptionsHazMat = None,
        dry_ice: PackageServiceOptionsDryIce = None,
    ):
        if delivery_confirmation is not None:
            self.delivery_confirmation = self._define_object(
                delivery_confirmation, PackageServiceOptionsDeliveryConfirmation
            )
        if access_point_cod is not None:
            self.access_point_cod = self._define_object(
                access_point_cod, PackageServiceOptionsAccessPointCod
            )
        if cod is not None:
            self.cod = self._define_object(cod, PackageServiceOptionsCod)
        if declared_value is not None:
            self.declared_value = self._define_object(
                declared_value, PackageServiceOptionsDeclaredValue
            )
        if shipper_declared_value is not None:
            self.shipper_declared_value = self._define_object(
                shipper_declared_value, PackageServiceOptionsShipperDeclaredValue
            )
        if shipper_release_indicator is not None:
            self.shipper_release_indicator = shipper_release_indicator
        if proactive_indicator is not None:
            self.proactive_indicator = proactive_indicator
        if refrigeration_indicator is not None:
            self.refrigeration_indicator = refrigeration_indicator
        if insurance is not None:
            self.insurance = self._define_object(
                insurance, PackageServiceOptionsInsurance
            )
        if ups_premium_care_indicator is not None:
            self.ups_premium_care_indicator = ups_premium_care_indicator
        if haz_mat is not None:
            self.haz_mat = self._define_object(haz_mat, PackageServiceOptionsHazMat)
        if dry_ice is not None:
            self.dry_ice = self._define_object(dry_ice, PackageServiceOptionsDryIce)
