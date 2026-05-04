---
title: "TrafficIncidentOnRoute (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficincidentonroute"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficIncidentOnRoute

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.TrafficIncidentOnRoute
All Implemented Interfaces:
[`TrafficIncidentBase`](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")

------------------------------------------------------------------------
public final class TrafficIncidentOnRoute extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here") implements [TrafficIncidentBase](sdk-for-android-explore-api-reference-latesttrafficincidentbase "interface in com.here.sdk.traffic")
Traffic incidents on a route. Use [`Section.getTrafficIncidents()`](sdk-for-android-explore-api-reference-latestsection#getTrafficIncidents()) to get a list of incidents on a route section. Use [`Span.getTrafficIncidentIndexes()`](sdk-for-android-explore-api-reference-latestspan#getTrafficIncidentIndexes()) to associate incidents with spans. Each incident takes at least the whole geometry of matching spans. Also, an incident can take some place out of the built route.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`LocalizedText`](sdk-for-android-explore-api-reference-latestlocalizedtext "class in com.here.sdk.core")

  [getDescription](#getDescription())`()`

Gets the human readable description of the incident, possibly with location information.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getEndTime](#getEndTime())`()`

Get the time until which the incident is valid, after this time the incident should not be considered.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getId](#getId())`()`

Gets the unique current identifier for a traffic incident.

[`TrafficIncidentImpact`](sdk-for-android-explore-api-reference-latesttrafficincidentimpact "enum class in com.here.sdk.traffic")

  [getImpact](#getImpact())`()`

Gets the impact of the incident.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [getStartTime](#getStartTime())`()`

Gets the time from which the incident is valid, before this time the incident should not be considered.

[`TrafficIncidentType`](sdk-for-android-explore-api-reference-latesttrafficincidenttype "enum class in com.here.sdk.traffic")

  [getType](#getType())`()`

Gets the category of the incident.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getId

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getId()

    Gets the unique current identifier for a traffic incident.

    The identifier can be changed by the backend due to some events, e.g. changing of [`TrafficIncidentBase.getEndTime()`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getEndTime()). This field will be empty for `OfflineRouting`.
Returns:
    The unique current identifier for a traffic incident.

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
