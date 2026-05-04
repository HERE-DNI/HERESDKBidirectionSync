---
title: "PickMapContentResult.TrafficIncidentResult (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpickmapcontentresult-trafficincidentresult"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PickMapContentResult.TrafficIncidentResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.PickMapContentResult.TrafficIncidentResult
All Implemented Interfaces:
[`TrafficIncidentBase`](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

<!-- -->

Enclosing class:
[PickMapContentResult](sdk-for-android-explore-api-reference-latestpickmapcontentresult "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class PickMapContentResult.TrafficIncidentResult extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here") implements [TrafficIncidentBase](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")
Carries the result of picking a Carto traffic incident object. Description of incident is currently not present in our map data, so [`TrafficIncidentBase.getDescription()`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getDescription()) always returns an empty string.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [getCoordinates](#getCoordinates())`()`

Gets the geographic coordinates of the traffic incident.

[`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")

  [getDescription](#getDescription())`()`

Gets the human readable description of the incident, possibly with location information.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getEndTime](#getEndTime())`()`

Get the time until which the incident is valid, after this time the incident should not be considered.

[`TrafficIncidentImpact`](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic")

  [getImpact](#getImpact())`()`

Gets the impact of the incident.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getOriginalId](#getOriginalId())`()`

Gets the unique traffic event ID.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getStartTime](#getStartTime())`()`

Gets the time from which the incident is valid, before this time the incident should not be considered.

[`TrafficIncidentType`](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")

  [getType](#getType())`()`

Gets the category of the incident.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getOriginalId

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getOriginalId()

    Gets the unique traffic event ID.

    Can be referenced when checking for updated traffic information for the specified event.
Returns:
    Unique traffic event ID.

### getCoordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") getCoordinates()

    Gets the geographic coordinates of the traffic incident.
Returns:
    The geographic coordinates of the traffic incident.

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
