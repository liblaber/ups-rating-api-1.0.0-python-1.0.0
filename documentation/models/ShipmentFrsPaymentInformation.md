# ShipmentFrsPaymentInformation

UPS Ground Freight Pricing (GFP) Payment Information container. Required only for GFP and when the FRSIndicator is present.

**Properties**

| Name           | Type                         | Required | Description                                                                                                                                              |
| :------------- | :--------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type\_         | FrsPaymentInformationType    | ✅       | GFP Payment Information Type container. GFP only.                                                                                                        |
| account_number | str                          | ❌       | UPS Account Number.                                                                                                                                      |
| address        | FrsPaymentInformationAddress | ❌       | Payer Address Container. Address container may be present for FRS Payment Information type = 02 and required when the FRS Payment Information type = 03. |

<!-- This file was generated by liblab | https://liblab.com/ -->
