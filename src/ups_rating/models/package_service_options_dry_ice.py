# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dry_ice_dry_ice_weight import DryIceDryIceWeight


@JsonMap(
    {
        "regulation_set": "RegulationSet",
        "dry_ice_weight": "DryIceWeight",
        "medical_use_indicator": "MedicalUseIndicator",
        "audit_required": "AuditRequired",
    }
)
class PackageServiceOptionsDryIce(BaseModel):
    """Container to hold Dry Ice information.  Lane check will happen based on postal code/ city.

    :param regulation_set: Regulation set for DryIce Shipment. Valid values: CFR = For HazMat regulated by US Dept of Transportation within the U.S. or ground shipments to Canada,IATA = For Worldwide Air movement.   The following values are valid: CFR and IATA.
    :type regulation_set: str
    :param dry_ice_weight: Container for Weight information for Dry Ice.
    :type dry_ice_weight: DryIceDryIceWeight
    :param medical_use_indicator: Presence/Absence Indicator. Any value inside is ignored. Relevant only in CFR regulation set. If present it is used to designate the Dry Ice is for any medical use and rates are adjusted for DryIce weight more than 2.5 KGS or 5.5 LBS., defaults to None
    :type medical_use_indicator: str, optional
    :param audit_required: Presence/Absence Indicator. Any value inside is ignored. Indicates a Dry Ice audit will be performed per the Regulation Set requirements. Empty tag means indicator is present., defaults to None
    :type audit_required: str, optional
    """

    def __init__(
        self,
        regulation_set: str,
        dry_ice_weight: DryIceDryIceWeight,
        medical_use_indicator: str = None,
        audit_required: str = None,
    ):
        self.regulation_set = regulation_set
        self.dry_ice_weight = self._define_object(dry_ice_weight, DryIceDryIceWeight)
        if medical_use_indicator is not None:
            self.medical_use_indicator = medical_use_indicator
        if audit_required is not None:
            self.audit_required = audit_required
