# VersionService

A list of all methods in the `VersionService` service. Click on the method name to view detailed information about that method.

| Methods       | Description                                                |
| :------------ | :--------------------------------------------------------- |
| [rate](#rate) | The Rating API is used when rating or shopping a shipment. |

## rate

The Rating API is used when rating or shopping a shipment.

- HTTP Method: `POST`
- Endpoint: `/rating/{version}/{requestoption}`

**Parameters**

| Name            | Type                                                  | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :-------------- | :---------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body    | [RateRequestWrapper](../models/RateRequestWrapper.md) | ✅       | The request body.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| version         | str                                                   | ✅       | Indicates Rate API to display the new release features in Rate API response based on Rate release. See the New section for the latest Rate release. Valid values: - v2403                                                                                                                                                                                                                                                                                                                                                                                        |
| requestoption   | str                                                   | ✅       | Valid Values: - Rate = The server rates (The default Request option is Rate if a Request Option is not provided). - Shop = The server validates the shipment, and returns rates for all UPS products from the ShipFrom to the ShipTo addresses. - Ratetimeintransit = The server rates with transit time information - Shoptimeintransit = The server validates the shipment, and returns rates and transit times for all UPS products from the ShipFrom to the ShipTo addresses. Rate is the only valid request option for UPS Ground Freight Pricing requests. |
| additionalinfo  | str                                                   | ❌       | Valid Values: timeintransit = The server rates with transit time information combined with requestoption in URL.Rate is the only valid request option for Ground Freight Pricing requests. Length 15                                                                                                                                                                                                                                                                                                                                                             |
| trans_id        | str                                                   | ❌       | An identifier unique to the request. Length 32                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| transaction_src | str                                                   | ❌       | An identifier of the client/source application that is making the request.Length 512                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**Return Type**

`RateResponseWrapper`

**Example Usage Code Snippet**

```python
from ups_rating import UpsRating, Environment
from ups_rating.models import RateRequestWrapper

sdk = UpsRating(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RateRequestWrapper(
    rate_request={
        "request": {
            "request_option": "ex labo",
            "sub_version": "eu E",
            "transaction_reference": {
                "customer_context": "amet aliquip deserunt"
            }
        },
        "pickup_type": {
            "code": "co",
            "description": "ipsum aliquip minim quis"
        },
        "customer_classification": {
            "code": "ir",
            "description": "sunt consectetur"
        },
        "shipment": {
            "origin_record_transaction_timestamp": "OriginRecordTransactionTimestamp",
            "shipper": {
                "name": "in",
                "attention_name": "laborum Excepteur",
                "shipper_number": "veniam",
                "address": {
                    "address_line": [
                        "AddressLine"
                    ],
                    "city": "consec",
                    "state_province_code": "no",
                    "postal_code": "anim",
                    "country_code": "ex"
                }
            },
            "ship_to": {
                "name": "voluptate ",
                "attention_name": "do",
                "address": {
                    "address_line": [
                        "AddressLine"
                    ],
                    "city": "dolore ut",
                    "state_province_code": "la",
                    "postal_code": "ani",
                    "country_code": "ei",
                    "residential_address_indicator": "ResidentialAddressIndicator"
                }
            },
            "ship_from": {
                "name": "id ul",
                "attention_name": "dol",
                "address": {
                    "address_line": [
                        "AddressLine"
                    ],
                    "city": "eu co",
                    "state_province_code": "Ut",
                    "postal_code": "Excepteur",
                    "country_code": "no"
                }
            },
            "alternate_delivery_address": {
                "name": "Name",
                "address": {
                    "address_line": [
                        "AddressLine"
                    ],
                    "city": "anim sit esse",
                    "state_province_code": "ut",
                    "postal_code": "et eli",
                    "country_code": "ei",
                    "residential_address_indicator": "ResidentialAddressIndicator",
                    "po_box_indicator": "POBoxIndicator"
                }
            },
            "shipment_indication_type": [
                {
                    "code": "la",
                    "description": "sit sint occaecat"
                }
            ],
            "payment_details": {
                "shipment_charge": [
                    {
                        "type_": "nu",
                        "bill_shipper": {
                            "account_number": "ea qui"
                        },
                        "bill_receiver": {
                            "account_number": "Except",
                            "address": {
                                "postal_code": "tempor"
                            }
                        },
                        "bill_third_party": {
                            "account_number": "quisla",
                            "address": {
                                "address_line": [
                                    "AddressLine"
                                ],
                                "city": "fugiat",
                                "state_province_code": "ip",
                                "postal_code": "sit off",
                                "country_code": "fu"
                            }
                        },
                        "consignee_billed_indicator": "ConsigneeBilledIndicator"
                    }
                ],
                "split_duty_vat_indicator": "SplitDutyVATIndicator"
            },
            "frs_payment_information": {
                "type_": {
                    "code": "lab",
                    "description": "dolor reprehenderit i"
                },
                "account_number": "sint t",
                "address": {
                    "postal_code": "irure ",
                    "country_code": "ir"
                }
            },
            "freight_shipment_information": {
                "freight_density_info": {
                    "adjusted_height_indicator": "AdjustedHeightIndicator",
                    "adjusted_height": {
                        "value": "in amet Ut",
                        "unit_of_measurement": {
                            "code": "te",
                            "description": "dolore"
                        }
                    },
                    "handling_units": [
                        {
                            "quantity": "anim in ",
                            "type_": {
                                "code": "ull",
                                "description": "aliqua fugiat id ea"
                            },
                            "dimensions": {
                                "unit_of_measurement": {
                                    "code": "ad",
                                    "description": "eu "
                                },
                                "length": "oc",
                                "width": "mini",
                                "height": "ad cupidat"
                            }
                        }
                    ]
                },
                "density_eligible_indicator": "DensityEligibleIndicator"
            },
            "goods_not_in_free_circulation_indicator": "GoodsNotInFreeCirculationIndicator",
            "service": {
                "code": "ull",
                "description": "occae"
            },
            "num_of_pieces": "NumOfPieces",
            "shipment_total_weight": {
                "unit_of_measurement": {
                    "code": "ad",
                    "description": "esse laboris ad"
                },
                "weight": "Weight"
            },
            "documents_only_indicator": "DocumentsOnlyIndicator",
            "package": [
                {
                    "packaging_type": {
                        "code": "co",
                        "description": "quis nisi"
                    },
                    "dimensions": {
                        "unit_of_measurement": {
                            "code": "l",
                            "description": "reprehenderit"
                        },
                        "length": "do",
                        "width": "et Ut",
                        "height": "veniam d"
                    },
                    "dim_weight": {
                        "unit_of_measurement": {
                            "code": "ali",
                            "description": "est cupidatat"
                        },
                        "weight": "veniam"
                    },
                    "package_weight": {
                        "unit_of_measurement": {
                            "code": "in",
                            "description": "est sint qu"
                        },
                        "weight": "esse n"
                    },
                    "commodity": {
                        "freight_class": "et qui exe",
                        "nmfc": {
                            "prime_code": "sit ",
                            "sub_code": "la"
                        }
                    },
                    "large_package_indicator": "LargePackageIndicator",
                    "package_service_options": {
                        "delivery_confirmation": {
                            "dcis_type": "v"
                        },
                        "access_point_cod": {
                            "currency_code": "Ut ",
                            "monetary_value": "amet "
                        },
                        "cod": {
                            "cod_funds_code": "i",
                            "cod_amount": {
                                "currency_code": "inc",
                                "monetary_value": "adipisic"
                            }
                        },
                        "declared_value": {
                            "currency_code": "sin",
                            "monetary_value": "exercita"
                        },
                        "shipper_declared_value": {
                            "currency_code": "eiu",
                            "monetary_value": "ad"
                        },
                        "shipper_release_indicator": "ShipperReleaseIndicator",
                        "proactive_indicator": "ProactiveIndicator",
                        "refrigeration_indicator": "RefrigerationIndicator",
                        "insurance": {
                            "basic_flexible_parcel_indicator": {
                                "currency_code": "cup",
                                "monetary_value": "mollit e"
                            },
                            "extended_flexible_parcel_indicator": {
                                "currency_code": "Exc",
                                "monetary_value": "dolordol"
                            },
                            "time_in_transit_flexible_parcel_indicator": {
                                "currency_code": "dol",
                                "monetary_value": "indolore"
                            }
                        },
                        "ups_premium_care_indicator": "UPSPremiumCareIndicator",
                        "haz_mat": {
                            "package_identifier": "cup",
                            "q_value": "par",
                            "over_packed_indicator": "OverPackedIndicator",
                            "all_packed_in_one_indicator": "AllPackedInOneIndicator",
                            "haz_mat_chemical_record": [
                                {
                                    "chemical_record_identifier": "of",
                                    "class_division_number": "incidi",
                                    "id_number": "no",
                                    "transportation_mode": "al",
                                    "regulation_set": "in ",
                                    "emergency_phone": "proident",
                                    "emergency_contact": "consectetur sed Lorem fugiat",
                                    "reportable_quantity": "o",
                                    "sub_risk_class": "enim velit",
                                    "packaging_group_type": "irur",
                                    "quantity": "Duis sintdeseru",
                                    "uom": "Lorem ",
                                    "packaging_instruction_code": "dolor",
                                    "proper_shipping_name": "veniam Lorem",
                                    "technical_name": "dolore voluptate cillum fugiat",
                                    "additional_description": "sunt deserunt",
                                    "packaging_type": "ut ni",
                                    "hazard_label_required": "ull",
                                    "packaging_type_quantity": "con",
                                    "commodity_regulated_level_code": "of",
                                    "transport_category": "d",
                                    "tunnel_restriction_code": "exercitati"
                                }
                            ]
                        },
                        "dry_ice": {
                            "regulation_set": "et ",
                            "dry_ice_weight": {
                                "unit_of_measurement": {
                                    "code": "E",
                                    "description": "quis"
                                },
                                "weight": "inci"
                            },
                            "medical_use_indicator": "MedicalUseIndicator",
                            "audit_required": "AuditRequired"
                        }
                    },
                    "additional_handling_indicator": "AdditionalHandlingIndicator",
                    "simple_rate": {
                        "code": "nu",
                        "description": "an"
                    },
                    "ups_premier": {
                        "category": "si"
                    },
                    "oversize_indicator": "OversizeIndicator",
                    "minimum_billable_weight_indicator": "MinimumBillableWeightIndicator"
                }
            ],
            "shipment_service_options": {
                "saturday_pickup_indicator": "SaturdayPickupIndicator",
                "saturday_delivery_indicator": "SaturdayDeliveryIndicator",
                "sunday_delivery_indicator": "SundayDeliveryIndicator",
                "available_services_option": "q",
                "access_point_cod": {
                    "currency_code": "eiu",
                    "monetary_value": "sed occaeca"
                },
                "deliver_to_addressee_only_indicator": "DeliverToAddresseeOnlyIndicator",
                "direct_delivery_only_indicator": "DirectDeliveryOnlyIndicator",
                "cod": {
                    "cod_funds_code": "l",
                    "cod_amount": {
                        "currency_code": "euc",
                        "monetary_value": "cillum f"
                    }
                },
                "delivery_confirmation": {
                    "dcis_type": "DCISType"
                },
                "return_of_document_indicator": "ReturnOfDocumentIndicator",
                "up_scarbonneutral_indicator": "UPScarbonneutralIndicator",
                "certificate_of_origin_indicator": "CertificateOfOriginIndicator",
                "pickup_options": {
                    "lift_gate_at_pickup_indicator": "LiftGateAtPickupIndicator",
                    "hold_for_pickup_indicator": "HoldForPickupIndicator"
                },
                "delivery_options": {
                    "lift_gate_at_delivery_indicator": "LiftGateAtDeliveryIndicator",
                    "drop_off_at_ups_facility_indicator": "DropOffAtUPSFacilityIndicator"
                },
                "restricted_articles": {
                    "alcoholic_beverages_indicator": "AlcoholicBeveragesIndicator",
                    "diagnostic_specimens_indicator": "DiagnosticSpecimensIndicator",
                    "perishables_indicator": "PerishablesIndicator",
                    "plants_indicator": "PlantsIndicator",
                    "seeds_indicator": "SeedsIndicator",
                    "special_exceptions_indicator": "SpecialExceptionsIndicator",
                    "tobacco_indicator": "TobaccoIndicator",
                    "e_cigarettes_indicator": "ECigarettesIndicator",
                    "hemp_cbd_indicator": "HempCBDIndicator"
                },
                "shipper_export_declaration_indicator": "ShipperExportDeclarationIndicator",
                "commercial_invoice_removal_indicator": "CommercialInvoiceRemovalIndicator",
                "import_control": {
                    "code": "in",
                    "description": "dolore eu"
                },
                "return_service": {
                    "code": "t",
                    "description": "irure exercitation dolor v"
                },
                "sdl_shipment_indicator": "SDLShipmentIndicator",
                "epra_indicator": "EPRAIndicator",
                "inside_delivery": "si",
                "item_disposal_indicator": "ItemDisposalIndicator"
            },
            "shipment_rating_options": {
                "negotiated_rates_indicator": "NegotiatedRatesIndicator",
                "frs_shipment_indicator": "FRSShipmentIndicator",
                "rate_chart_indicator": "RateChartIndicator",
                "user_level_discount_indicator": "UserLevelDiscountIndicator",
                "tpfc_negotiated_rates_indicator": "TPFCNegotiatedRatesIndicator"
            },
            "invoice_line_total": {
                "currency_code": "dol",
                "monetary_value": "exerc"
            },
            "rating_method_requested_indicator": "RatingMethodRequestedIndicator",
            "tax_information_indicator": "TaxInformationIndicator",
            "promotional_discount_information": {
                "promo_code": "consectet",
                "promo_alias_code": "et commodo officiani"
            },
            "delivery_time_information": {
                "package_bill_type": "fu",
                "pickup": {
                    "date_": "doelit E",
                    "time": "sed "
                },
                "return_contract_services": [
                    {
                        "code": "ve",
                        "description": "Excepteur"
                    }
                ]
            },
            "master_carton_indicator": "MasterCartonIndicator",
            "wwe_shipment_indicator": "WWEShipmentIndicator"
        }
    }
)

result = sdk.version.rate(
    request_body=request_body,
    version="v2403",
    requestoption="voluptate",
    additionalinfo="additionalinfo",
    trans_id="transId",
    transaction_src="testing"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
