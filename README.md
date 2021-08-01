# Traffic Congestion 
This project delves into finding different ways of improving safety, optimizing operations and identifying diverse opportunities for infrastructural challenges. 
This dataset is obtained from [GeoTab](https://data.geotab.com/ "GEOTAB") contains information regarding traffic congestions in most of United States cities.  This aims at accurately predicting possible future congestions. Breaking this project further includes:
- Exporatory Data Analysis
- Data Preprocessing
- Algorithm Selection 
- Model Evaluation 


# Data columns:

## 1. Independent Variables (Features)
- IntersectionId: Represents a unique intersectionID for some intersection of roads within a city.
- Latitude: The latitude of the intersection.
- Longitude: The longitude of the intersection.
- EntryStreetName: The street name from which the vehicle entered towards the intersection.
- ExitStreetName: The street name to which the vehicle goes from the intersection.
- EntryHeading: Direction to which the car was heading while entering the intersection.
- ExitHeading: Direction to which the car went after it went through the intersection.
- Hour: The hour of the day.
- Weekend: It's weekend or not.
- Month: Which Month it is.
- Path: It is a concatination in the format: EntryStreetName_EntryHeading ExitStreetName_ExitHeading.
- City: Name of the city

## 2. Dependent Variables (Targets)
- TotalTimeStopped_p20: Total time for which 20% of the vehicles had to stop at an intersection.
- TotalTimeStopped_p40: Total time for which 40% of the vehicles had to stop at an intersection.
- TotalTimeStopped_p50: Total time for which 50% of the vehicles had to stop at an intersection.
- TotalTimeStopped_p60: Total time for which 60% of the vehicles had to stop at an intersection.
- TotalTimeStopped_p80: Total time for which 80% of the vehicles had to stop at an intersection.
- TimeFromFirstStop_p20: Time taken for 20% of the vehicles to stop again after crossing an intersection.
- TimeFromFirstStop_p40: Time taken for 40% of the vehicles to stop again after crossing an intersection.
- TimeFromFirstStop_p50: Time taken for 50% of the vehicles to stop again after crossing a intersection.
- TimeFromFirstStop_p60: Time taken for 60% of the vehicles to stop again after crossing a intersection.
- TimeFromFirstStop_p80: Time taken for 80% of the vehicles to stop again after crossing a intersection.
- DistanceToFirstStop_p20: How far before the intersection the 20% of the vehicles stopped for the first time.
- DistanceToFirstStop_p40: How far before the intersection the 40% of the vehicles stopped for the first time.
- DistanceToFirstStop_p50: How far before the intersection the 50% of the vehicles stopped for the first time.
- DistanceToFirstStop_p60: How far before the intersection the 60% of the vehicles stopped for the first time.
- DistanceToFirstStop_p80: How far before the intersection the 80% of the vehicles stopped for the first time.

## 3. Target Output (based on Competition's Rules)
Total time stopped at an intersection, 20th, 50th, 80th percentiles and Distance between the intersection and the first place the vehicle stopped and started waiting, 20th, 50th, 80th percentiles

- TotalTimeStopped_p20
- TotalTimeStopped_p50
- TotalTimeStopped_p80
- DistanceToFirstStop_p20
- DistanceToFirstStop_p50
- DistanceToFirstStop_p80



