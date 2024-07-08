# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .package_packaging_type import PackagePackagingType
from .package_dimensions import PackageDimensions
from .package_dim_weight import PackageDimWeight
from .package_package_weight import PackagePackageWeight
from .package_commodity import PackageCommodity
from .package_package_service_options import PackagePackageServiceOptions
from .package_simple_rate import PackageSimpleRate
from .package_ups_premier import PackageUpsPremier


@JsonMap(
    {
        "packaging_type": "PackagingType",
        "dimensions": "Dimensions",
        "dim_weight": "DimWeight",
        "package_weight": "PackageWeight",
        "commodity": "Commodity",
        "large_package_indicator": "LargePackageIndicator",
        "package_service_options": "PackageServiceOptions",
        "additional_handling_indicator": "AdditionalHandlingIndicator",
        "simple_rate": "SimpleRate",
        "ups_premier": "UPSPremier",
        "oversize_indicator": "OversizeIndicator",
        "minimum_billable_weight_indicator": "MinimumBillableWeightIndicator",
    }
)
class ShipmentPackage(BaseModel):
    """Package Container.  Only one Package allowed for Simple Rate

    :param packaging_type: Packaging Type Container., defaults to None
    :type packaging_type: PackagePackagingType, optional
    :param dimensions: Dimensions Container. This container is not applicable for GFP Rating request.  Required for Heavy Goods service. Package Dimension will be ignored for Simple Rate, defaults to None
    :type dimensions: PackageDimensions, optional
    :param dim_weight: Package Dimensional Weight container. Values in this container are ignored when package dimensions are provided. Please visit ups.com for instructions on calculating this value.  Only used for non-US/CA/PR shipments., defaults to None
    :type dim_weight: PackageDimWeight, optional
    :param package_weight: Package Weight Container.  Required for an GFP Rating request. Otherwise optional. Required for Heavy Goods service.  Package Weight will be ignored for Simple Rate, defaults to None
    :type package_weight: PackagePackageWeight, optional
    :param commodity: Commodity Container.  Required only for GFP rating when FRSShipmentIndicator is requested., defaults to None
    :type commodity: PackageCommodity, optional
    :param large_package_indicator: This element does not require a value and if one is entered it will be ignored.  If present, it indicates the shipment will be categorized as a Large Package., defaults to None
    :type large_package_indicator: str, optional
    :param package_service_options: PackageServiceOptions container., defaults to None
    :type package_service_options: PackagePackageServiceOptions, optional
    :param additional_handling_indicator: A flag indicating if the packages require additional handling. True if AdditionalHandlingIndicator tag exists; false otherwise. Additional Handling indicator indicates it's a non-corrugated package.  Empty Tag., defaults to None
    :type additional_handling_indicator: str, optional
    :param simple_rate: SimpleRate Container, defaults to None
    :type simple_rate: PackageSimpleRate, optional
    :param ups_premier: UPS Premier, defaults to None
    :type ups_premier: PackageUpsPremier, optional
    :param oversize_indicator: Presence/Absence Indicator. Any value inside is ignored. It indicates if packge is oversized.  Applicable for UPS Worldwide Economy DDU service, defaults to None
    :type oversize_indicator: str, optional
    :param minimum_billable_weight_indicator: Presence/Absence Indicator. Any value inside is ignored. It indicates if packge is qualified for minimum billable weight.  Applicable for UPS Worldwide Economy DDU service, defaults to None
    :type minimum_billable_weight_indicator: str, optional
    """

    def __init__(
        self,
        packaging_type: PackagePackagingType = None,
        dimensions: PackageDimensions = None,
        dim_weight: PackageDimWeight = None,
        package_weight: PackagePackageWeight = None,
        commodity: PackageCommodity = None,
        large_package_indicator: str = None,
        package_service_options: PackagePackageServiceOptions = None,
        additional_handling_indicator: str = None,
        simple_rate: PackageSimpleRate = None,
        ups_premier: PackageUpsPremier = None,
        oversize_indicator: str = None,
        minimum_billable_weight_indicator: str = None,
    ):
        if packaging_type is not None:
            self.packaging_type = self._define_object(
                packaging_type, PackagePackagingType
            )
        if dimensions is not None:
            self.dimensions = self._define_object(dimensions, PackageDimensions)
        if dim_weight is not None:
            self.dim_weight = self._define_object(dim_weight, PackageDimWeight)
        if package_weight is not None:
            self.package_weight = self._define_object(
                package_weight, PackagePackageWeight
            )
        if commodity is not None:
            self.commodity = self._define_object(commodity, PackageCommodity)
        if large_package_indicator is not None:
            self.large_package_indicator = large_package_indicator
        if package_service_options is not None:
            self.package_service_options = self._define_object(
                package_service_options, PackagePackageServiceOptions
            )
        if additional_handling_indicator is not None:
            self.additional_handling_indicator = additional_handling_indicator
        if simple_rate is not None:
            self.simple_rate = self._define_object(simple_rate, PackageSimpleRate)
        if ups_premier is not None:
            self.ups_premier = self._define_object(ups_premier, PackageUpsPremier)
        if oversize_indicator is not None:
            self.oversize_indicator = oversize_indicator
        if minimum_billable_weight_indicator is not None:
            self.minimum_billable_weight_indicator = minimum_billable_weight_indicator
