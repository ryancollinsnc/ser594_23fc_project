#### SER594: Experimentation
#### Title: Predictive Analysis of Housing Prices Using Machine Learning 
#### Author: Ryan Collins
#### Date: 11/20/23


## Explainable Records
### Record 1
**Raw Data:** Sample input for a property in Seneca Falls, neighborhood type, in NV with a date stamp of 2010-12-31.

Prediction Explanation:** The RandomForestRegressor model predicted the property value at $111,311.57. This prediction was based on factors like location, region type, and market conditions at the specified date. The model's ensemble approach, utilizing multiple decision trees, likely recognized patterns and trends within the data specific to the region and time, providing a prediction close to the actual value of $109,905.16.

### Record 2
**Raw Data:** Sample input for a property in South Miami Heights, neighborhood type, in FL with a date stamp of 2017-10-31.

Prediction Explanation:** The prediction was $244,714.61, which is slightly lower than the actual value of $248,121.26. The RandomForestRegressor's prediction may have been influenced by the historical pricing trends in Florida's real estate market and the regional specifics encoded in the model's training data.

## Interesting Features
### Feature A
**Feature:** RegionName

**Justification:** The name of the region, which is likely a proxy for the geographical location, is a significant predictor for housing prices as it encapsulates factors like desirability, local economy, and cost of living.

### Feature B
**Feature:** Date

**Justification:** The date feature captures the temporal trends in the housing market, such as inflation, interest rates, and economic cycles, which are crucial for accurate property valuation.

## Experiments 
### Varying RegionType
**Prediction Trend Seen:** Changing the 'RegionType' from 'neighborhood' to 'city' showed a general increase in the predicted property values, indicating that the model recognizes different types of regions as influential on the housing prices.

### Varying StateName
**Prediction Trend Seen:** Modifying the 'StateName' led to significant changes in predictions, reflecting the model's sensitivity to location as a major determinant of housing price.

### Varying RegionName and Date together
**Prediction Trend Seen:** Altering both 'RegionName' and 'Date' simultaneously resulted in predictions that suggest the model is capable of capturing the combined effects of geographic and temporal factors on property values.


### Varying RegionType and StateName inversely
**Prediction Trend Seen:** As 'RegionType' shifted towards less dense area types and 'StateName' moved towards states with higher property values, the model showed a nuanced understanding of the interplay between region density and state-wide market trends.
