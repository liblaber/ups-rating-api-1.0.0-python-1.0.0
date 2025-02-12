# ServiceSummaryEstimatedArrival

Container for the Time-In-Transit arrival information by service

**Properties**

| Name                     | Type                    | Required | Description                                                                                                                                                                                                                            |
| :----------------------- | :---------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| arrival                  | EstimatedArrivalArrival | ✅       | Container for the Time-In-Transit arrival information by service. This is the most accurate delivery information available via the Rating API and will reflect changes in delivery schedules due to peak business seasons or holidays. |
| business_days_in_transit | str                     | ✅       | Number of business days from Origin to Destination Locations.                                                                                                                                                                          |
| pickup                   | EstimatedArrivalPickup  | ✅       | The date and pick up time container.                                                                                                                                                                                                   |
| day_of_week              | str                     | ✅       | Day of week for arrival. Valid values are: MONTUEWEDTHUFRISAT                                                                                                                                                                          |
| customer_center_cutoff   | str                     | ❌       | Customer Service call time. Returned for domestic as well as international requests.                                                                                                                                                   |
| delay_count              | str                     | ❌       | Number of days delayed at customs. Returned for International requests.                                                                                                                                                                |
| holiday_count            | str                     | ❌       | Number of National holidays during transit. Returned for International requests.                                                                                                                                                       |
| rest_days                | str                     | ❌       | Number of rest days, i.e. non movement. Returned for International requests.                                                                                                                                                           |
| total_transit_days       | str                     | ❌       | The total number of days in transit from one location to the next. Returned for International requests.                                                                                                                                |

<!-- This file was generated by liblab | https://liblab.com/ -->
