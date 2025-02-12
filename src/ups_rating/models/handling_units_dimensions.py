# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .handling_units_unit_of_measurement import HandlingUnitsUnitOfMeasurement


@JsonMap(
    {
        "unit_of_measurement": "UnitOfMeasurement",
        "length": "Length",
        "width": "Width",
        "height": "Height",
    }
)
class HandlingUnitsDimensions(BaseModel):
    """Dimension of the HandlingUnit container for density based pricing.

    :param unit_of_measurement: UnitOfMeasurement container.
    :type unit_of_measurement: HandlingUnitsUnitOfMeasurement
    :param length: The length of the line item used to determine dimensional weight.
    :type length: str
    :param width: The width of the line item used to determine dimensional weight.
    :type width: str
    :param height: The height of the line item used to determine dimensional weight.
    :type height: str
    """

    def __init__(
        self,
        unit_of_measurement: HandlingUnitsUnitOfMeasurement,
        length: str,
        width: str,
        height: str,
    ):
        self.unit_of_measurement = self._define_object(
            unit_of_measurement, HandlingUnitsUnitOfMeasurement
        )
        self.length = length
        self.width = width
        self.height = height
