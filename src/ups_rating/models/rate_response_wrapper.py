# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .rate_response import RateResponse


@JsonMap({"rate_response": "RateResponse"})
class RateResponseWrapper(BaseModel):
    """N/A

    :param rate_response: Rate Response Container.
    :type rate_response: RateResponse
    """

    def __init__(self, rate_response: RateResponse):
        self.rate_response = self._define_object(rate_response, RateResponse)
