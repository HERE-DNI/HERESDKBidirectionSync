---
title: "TrafficIncidentBase (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficincidentbase"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TrafficIncidentBase

All Known Implementing Classes:
[`PickMapContentResult.TrafficIncidentResult`](sdk-for-android-explore-api-reference-latestpickmapcontentresult-trafficincidentresult "class in com.here.sdk.mapview"), [`TrafficIncident`](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic"), [`TrafficIncidentOnRoute`](sdk-for-android-explore-api-reference-latesttrafficincidentonroute "class in com.here.sdk.routing")

------------------------------------------------------------------------
public interface TrafficIncidentBase
TrafficIncident provides details about a traffic incident.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  [`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")

  [getDescription](#getDescription())`()`

Gets the human readable description of the incident, possibly with location information.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getEndTime](#getEndTime())`()`

Get the time until which the incident is valid, after this time the incident should not be considered.

[`TrafficIncidentImpact`](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic")

  [getImpact](#getImpact())`()`

Gets the impact of the incident.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getStartTime](#getStartTime())`()`

Gets the time from which the incident is valid, before this time the incident should not be considered.

[`TrafficIncidentType`](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")

  [getType](#getType())`()`

Gets the category of the incident.

## Method Details

### getImpact

@NonNull [TrafficIncidentImpact](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic") getImpact()

    Gets the impact of the incident.

    The value is [`TrafficIncidentImpact.UNKNOWN`](sdk-for-android-explore-api-reference-latesttrafficincidentimpact#UNKNOWN) if it hasn't been provided by the traffic incidents supplier.
Returns:
    The impact of the incident.

### getType

@NonNull [TrafficIncidentType](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic") getType()

    Gets the category of the incident.

    The value is [`TrafficIncidentType.UNKNOWN`](sdk-for-android-explore-api-reference-latesttrafficincidenttype#UNKNOWN) if it hasn't been provided by the traffic incidents supplier.
Returns:
    The category of the incident.

### getDescription

@NonNull [LocalizedText](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core") getDescription()

    Gets the human readable description of the incident, possibly with location information.

    The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via `TrafficIncidentResult`, then always an empty string is returned. This does not apply when using the `TrafficEngine`.
Returns:
    The human readable description of the incident, possibly with location information.

### getStartTime

@Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) getStartTime()

    Gets the time from which the incident is valid, before this time the incident should not be considered.

    The value is `null` if it hasn't been provided by the traffic incidents supplier.
Returns:
    The time from which the incident is valid, before this time the incident should not be considered.

### getEndTime

@Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) getEndTime()

    Get the time until which the incident is valid, after this time the incident should not be considered.

    The value is `null` if it hasn't been provided by the traffic incidents supplier.
Returns:
    The time until which the incident is valid, after this time the incident should not be considered.
