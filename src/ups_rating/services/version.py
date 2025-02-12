# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.rate_response_wrapper import RateResponseWrapper
from ..models.rate_request_wrapper import RateRequestWrapper


class VersionService(BaseService):

    @cast_models
    def rate(
        self,
        request_body: RateRequestWrapper,
        version: str,
        requestoption: str,
        additionalinfo: str = None,
        trans_id: str = None,
        transaction_src: str = None,
    ) -> RateResponseWrapper:
        """The Rating API is used when rating or shopping a shipment.

        :param request_body: The request body.
        :type request_body: RateRequestWrapper
        :param version: Indicates Rate API to display the new release features in Rate API response based on Rate release. See the New section for the latest Rate release.

        Valid values:
        - v2403
        :type version: str
        :param requestoption: Valid Values:
        - Rate = The server rates (The default Request option is Rate if a Request Option is not provided).
        - Shop = The server validates the shipment, and returns rates for all UPS products from the ShipFrom to the ShipTo addresses.
        - Ratetimeintransit = The server rates with transit time information
        - Shoptimeintransit = The server validates the shipment, and returns rates and transit times for all UPS products from the ShipFrom to the ShipTo addresses.

        Rate is the only valid request option for UPS Ground Freight Pricing requests.
        :type requestoption: str
        :param additionalinfo: Valid Values: timeintransit = The server rates with transit time information combined with requestoption in URL.Rate is the only valid request option for Ground Freight Pricing requests. Length 15, defaults to None
        :type additionalinfo: str, optional
        :param trans_id: An identifier unique to the request. Length 32, defaults to None
        :type trans_id: str, optional
        :param transaction_src: An identifier of the client/source application that is making the request.Length 512, defaults to None
        :type transaction_src: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: successful operation
        :rtype: RateResponseWrapper
        """

        Validator(RateRequestWrapper).validate(request_body)
        Validator(str).validate(version)
        Validator(str).max_length(10).validate(requestoption)
        Validator(str).is_optional().validate(additionalinfo)
        Validator(str).is_optional().validate(trans_id)
        Validator(str).is_optional().validate(transaction_src)

        serialized_request = (
            Serializer(
                f"{self.base_url}/rating/{{version}}/{{requestoption}}",
                self.get_default_headers(),
            )
            .add_header("transId", trans_id)
            .add_header("transactionSrc", transaction_src)
            .add_path("version", version)
            .add_path("requestoption", requestoption)
            .add_query("additionalinfo", additionalinfo)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return RateResponseWrapper._unmap(response)
