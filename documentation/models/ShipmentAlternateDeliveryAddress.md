# ShipmentAlternateDeliveryAddress

Alternate Delivery Address container. Applies for deliveries to UPS Access Point™ locations.

Required for the following ShipmentIndicationType values:

- 01 - Hold for Pickup at UPS Access Point™
- 02 - UPS Access Point™ Delivery

**Properties**

| Name    | Type                            | Required | Description                                       |
| :------ | :------------------------------ | :------- | :------------------------------------------------ |
| address | AlternateDeliveryAddressAddress | ✅       | Address container for Alternate Delivery Address. |
| name    | str                             | ❌       | UPS Access Point location name.                   |

<!-- This file was generated by liblab | https://liblab.com/ -->
