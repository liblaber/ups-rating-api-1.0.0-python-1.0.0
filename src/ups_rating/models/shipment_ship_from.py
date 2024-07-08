# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ship_from_address import ShipFromAddress


@JsonMap({"name": "Name", "attention_name": "AttentionName", "address": "Address"})
class ShipmentShipFrom(BaseModel):
    """Ship From Container.

    :param name: Origin attention name or company name.  Length is not validated., defaults to None
    :type name: str, optional
    :param attention_name: Origin attention name.  Length is not validated., defaults to None
    :type attention_name: str, optional
    :param address: Address container for Ship From.  Address Container
    :type address: ShipFromAddress
    """

    def __init__(
        self, address: ShipFromAddress, name: str = None, attention_name: str = None
    ):
        if name is not None:
            self.name = name
        if attention_name is not None:
            self.attention_name = attention_name
        self.address = self._define_object(address, ShipFromAddress)
