# RateRequestPickupType

Pickup Type container tag.

**Properties**

| Name        | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                      |
| :---------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code        | str  | ✅       | Pickup Type Code. Valid values: 01 - Daily Pickup (Default - used when an invalid pickup type code is provided)03 - Customer Counter06 - One Time Pickup19 - Letter Center20 - Air Service CenterLength is not validated. When negotiated rates are requested, 07 (onCallAir) will be ignored.Refer to the Rate Types Table in the Appendix for rate type based on Pickup Type and Customer Classification Code. |
| description | str  | ❌       | Pickup Type Description. Ignored if provided in the Request.                                                                                                                                                                                                                                                                                                                                                     |

<!-- This file was generated by liblab | https://liblab.com/ -->
