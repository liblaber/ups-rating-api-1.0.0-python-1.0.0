# RatedPackageBillingWeight

Billing Weight Container.

**Properties**

| Name                | Type                                       | Required | Description                                                                                                                                                                                                                                                                            |
| :------------------ | :----------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unit_of_measurement | RatedPackageBillingWeightUnitOfMeasurement | ✅       | Unit Of Measurement Container.                                                                                                                                                                                                                                                         |
| weight              | str                                        | ✅       | The value for the billable weight associated with the package. When using a negotiated divisor different from the published UPS divisor (139 for inches and 5,000 for cm), the weight returned is based on the published divisor. Rates, however, are based on the negotiated divisor. |

<!-- This file was generated by liblab | https://liblab.com/ -->
