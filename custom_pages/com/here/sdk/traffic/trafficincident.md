---
title: "TrafficIncident (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficincident"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficIncident

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.traffic.TrafficIncident
All Implemented Interfaces:
[`TrafficIncidentBase`](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

------------------------------------------------------------------------
public final class TrafficIncident extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here") implements [TrafficIncidentBase](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")
TrafficIncident provides details about a traffic incident.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory)

The vehicle categories that can be restricted.

`static final class `

  [TrafficIncident.VehicleRestriction](sdk-for-android-explore-api-reference-latesttrafficincident-vehiclerestriction)

The vehicle restriction representing a vehicle category and relevant restriction rules.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`>`

  [getCodes](#getCodes())`()`

Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.

[`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")

  [getDescription](#getDescription())`()`

Gets the human readable description of the incident, possibly with location information.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getEndTime](#getEndTime())`()`

Get the time until which the incident is valid, after this time the incident should not be considered.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getEntryTime](#getEntryTime())`()`

Gets the time the incident was entered into the system.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getId](#getId())`()`

Gets the unique current identifier for a traffic incident.

[`TrafficIncidentImpact`](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic")

  [getImpact](#getImpact())`()`

Gets the impact of the incident.

[`JunctionsTraversability`](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")

  [getJunctionsTraversability](#getJunctionsTraversability())`()`

Gets the traversability of junctions along the affected road.

[`TrafficLocation`](sdk-for-android-explore-api-reference-latesttrafficlocation "class in com.here.sdk.traffic")

  [getLocation](#getLocation())`()`

Gets the location of the incident.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getOriginalId](#getOriginalId())`()`

Gets the unique identifier of the first traffic incident.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getParentId](#getParentId())`()`

Gets the identifier of another incident to which this incident is linked.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getStartTime](#getStartTime())`()`

Gets the time from which the incident is valid, before this time the incident should not be considered.

[`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")

  [getSummary](#getSummary())`()`

Gets the human readable summary of the incident.

[`TrafficIncidentType`](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")

  [getType](#getType())`()`

Gets the category of the incident.

[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[`TrafficIncident.RestrictedVehicleCategory`](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic"), [`TrafficIncident.VehicleRestriction`](sdk-for-android-explore-api-reference-latesttrafficincident-vehiclerestriction "class in com.here.sdk.traffic")`>`

  [getVehicleRestrictions](#getVehicleRestrictions())`()`

Gets the map of restricted vehicle categories to restrictions.

`boolean`

  [isRoadClosed](#isRoadClosed())`()`

Gets the flag indicating whether road is closed or not.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getId

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getId()

    Gets the unique current identifier for a traffic incident.
Returns:
    The unique current identifier for a traffic incident.

### getOriginalId

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOriginalId()

    Gets the unique identifier of the first traffic incident.

    The original id remains the same whenever the traffic incident is updated and [`getId()`](#getId()) is changed. Once an incident chain has been created, this value will never change. The traffic incident an be looked up by original id using [`TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)).
Returns:
    The unique identifier of the first traffic incident.

### getParentId

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getParentId()

    Gets the identifier of another incident to which this incident is linked.

    The value is `null` if the incident doesn't have a parent.
Returns:
    The identifier of another incident to which this incident is linked.

### getJunctionsTraversability

@NonNull public [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic") getJunctionsTraversability()

    Gets the traversability of junctions along the affected road.
Returns:
    The traversability of junctions along the affected road.

### isRoadClosed

public boolean isRoadClosed()

    Gets the flag indicating whether road is closed or not.
Returns:
    The flag indicates whether road is closed or not.

### getCodes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> getCodes()

    Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.

    Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.
Returns:
    The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.

### getSummary

@NonNull public [LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core") getSummary()

    Gets the human readable summary of the incident.

    The summary field provides a short version of the description containing no location information. The expected summary language can be managed via [`TrafficIncidentsQueryOptions.languageCode`](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions#languageCode) and [`TrafficIncidentLookupOptions.languageCode`](sdk-for-android-explore-api-reference-latesttrafficincidentlookupoptions#languageCode).
Returns:
    The human readable summary of the incident.

### getEntryTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) getEntryTime()

    Gets the time the incident was entered into the system.

    The value is `null` if it hasn't been provided by the traffic incidents supplier.
Returns:
    The time the incident was entered into the system.

### getLocation

@NonNull public [TrafficLocation](sdk-for-android-explore-api-reference-latesttrafficlocation "class in com.here.sdk.traffic") getLocation()

    Gets the location of the incident.
Returns:
    The location of the incident.

### getVehicleRestrictions

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic"),[TrafficIncident.VehicleRestriction](sdk-for-android-explore-api-reference-latesttrafficincident-vehiclerestriction "class in com.here.sdk.traffic")\> getVehicleRestrictions()

    Gets the map of restricted vehicle categories to restrictions.

    A vehicle is restricted if at least one restriction field is applicable for it. If the map is empty, there're no restricted vehicles for the incident.
Returns:
    The map of restricted vehicle categories to restrictions.

### getImpact

@NonNull public [TrafficIncidentImpact](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic") getImpact()

    Gets the impact of the incident.

    The value is [`TrafficIncidentImpact.UNKNOWN`](sdk-for-android-explore-api-reference-latesttrafficincidentimpact#UNKNOWN) if it hasn't been provided by the traffic incidents supplier.
Specified by:
    [`getImpact`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getImpact()) in interface [`TrafficIncidentBase`](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

    Returns:
    The impact of the incident.

### getType

@NonNull public [TrafficIncidentType](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic") getType()

    Gets the category of the incident.

    The value is [`TrafficIncidentType.UNKNOWN`](sdk-for-android-explore-api-reference-latesttrafficincidenttype#UNKNOWN) if it hasn't been provided by the traffic incidents supplier.
Specified by:
    [`getType`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getType()) in interface [`TrafficIncidentBase`](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

    Returns:
    The category of the incident.

### getDescription

@NonNull public [LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core") getDescription()

    Gets the human readable description of the incident, possibly with location information.

    The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via `TrafficIncidentResult`, then always an empty string is returned. This does not apply when using the `TrafficEngine`.
Specified by:
    [`getDescription`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getDescription()) in interface [`TrafficIncidentBase`](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

    Returns:
    The human readable description of the incident, possibly with location information.

### getStartTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) getStartTime()

    Gets the time from which the incident is valid, before this time the incident should not be considered.

    The value is `null` if it hasn't been provided by the traffic incidents supplier.
Specified by:
    [`getStartTime`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getStartTime()) in interface [`TrafficIncidentBase`](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

    Returns:
    The time from which the incident is valid, before this time the incident should not be considered.

### getEndTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) getEndTime()

    Get the time until which the incident is valid, after this time the incident should not be considered.

    The value is `null` if it hasn't been provided by the traffic incidents supplier.
Specified by:
    [`getEndTime`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getEndTime()) in interface [`TrafficIncidentBase`](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

    Returns:
    The time until which the incident is valid, after this time the incident should not be considered.
