---
title: "TrafficFlow (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficflow"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficFlow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.traffic.TrafficFlow
All Implemented Interfaces:
[`TrafficFlowBase`](sdk-for-android-explore-api-reference-latesttrafficflowbase "interface in com.here.sdk.traffic")

------------------------------------------------------------------------
public final class TrafficFlow extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here") implements [TrafficFlowBase](sdk-for-android-explore-api-reference-latesttrafficflowbase "interface in com.here.sdk.traffic")
This class provides details about traffic flow along a [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core"), inside a [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") or a [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core"), that represents particular path of the road network.
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.
For additional information about fields, refer to [Traffic API v7 API Reference: Traffic API v7](https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getConfidence](#getConfidence())`()`

Gets the confidence field value which is normalized value between 0.0 and 1.0.

`double`

  [getFreeFlowSpeedInMetersPerSecond](#getFreeFlowSpeedInMetersPerSecond())`()`

Gets the reference speed in meters per second along the roadway when no traffic is present.

`double`

  [getJamFactor](#getJamFactor())`()`

Gets a value for the amount of traffic on the roadway.

[Short](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html)

  [getJamTendency](#getJamTendency())`()`

Gets the jam tendency field value which denotes whether the congestion is increasing, decreasing, or constant.

[`JunctionsTraversability`](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")

  [getJunctionsTraversability](#getJunctionsTraversability())`()`

Gets the traversability of junctions along the affected road.

[`TrafficLocation`](sdk-for-android-explore-api-reference-latesttrafficlocation "class in com.here.sdk.traffic")

  [getLocation](#getLocation())`()`

Gets the location of the incident.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getSpeedInMetersPerSecond](#getSpeedInMetersPerSecond())`()`

Gets the expected speed in meters per second along the roadway; will not exceed the legal speed limit.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getSpeedUncappedInMetersPerSecond](#getSpeedUncappedInMetersPerSecond())`()`

Gets the expected speed in meters per second along the roadway.

[`Traversability`](sdk-for-android-explore-api-reference-latesttraversability "enum class in com.here.sdk.traffic")

  [getTraversability](#getTraversability())`()`

Gets the traversability of roadway.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getLocation

@NonNull public [TrafficLocation](sdk-for-android-explore-api-reference-latesttrafficlocation "class in com.here.sdk.traffic") getLocation()

    Gets the location of the incident.
Returns:
    Defines the location affected by traffic flow.

### getSpeedInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getSpeedInMetersPerSecond()

    Gets the expected speed in meters per second along the roadway; will not exceed the legal speed limit.
Returns:
    The expected speed in meters per second along the roadway; will not exceed the legal speed limit.

### getSpeedUncappedInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getSpeedUncappedInMetersPerSecond()

    Gets the expected speed in meters per second along the roadway.

    It is based on probe data (GPS coordinates sent by vehicles or mobile devices driving along that roadway). The calculated 'expected speed' may be over the legal speed limit for that roadway because people are driving over the speed limit.
Returns:
    The expected speed in meters per second that a car can drive along a roadway right now; may exceed the legal speed limit.

### getJamTendency

@Nullable public [Short](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Short.html) getJamTendency()

    Gets the jam tendency field value which denotes whether the congestion is increasing, decreasing, or constant.

    The congestion tendency may take the following values:

    - +2 - rapidly increasing congestion
    - +1 - increasing congestion
    - 0 - constant congestion
    - -1 - decreasing congestion
    - -2 - rapidly decreasing congestion Default value of 0 can be assumed when this attribute is not present.
Returns:
    The jamTendency field denotes whether the congestion is increasing, decreasing, or constant.

### getConfidence

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getConfidence()

    Gets the confidence field value which is normalized value between 0.0 and 1.0.

    It is a normalized value between 0.0 and 1.0 with the following meaning:

    - 0.7 \< confidence \<= 1.0 indicates real time speeds
    - 0.5 \< confidence \<= 0.7 indicates historical speeds
    - 0.0 \< confidence \<= 0.5 indicates speed limit

    This field can be used to identify whether the data for a location is derived from real-time probe sources or historical information only. All confidence data 0.71 and above is based on real-time information, where a confidence value of 0.75 or greater indicates high confidence real-time information. A confidence value equal to 0.70 or lower means that the data is derived from historical data only.
Returns:
    The confidence field indicates the proportion of real-time data included in the speed calculation.

### getTraversability

@Nullable public [Traversability](sdk-for-android-explore-api-reference-latesttraversability "enum class in com.here.sdk.traffic") getTraversability()

    Gets the traversability of roadway.
Returns:
    The traversability of roadway.

### getJunctionsTraversability

@Nullable public [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic") getJunctionsTraversability()

    Gets the traversability of junctions along the affected road.
Returns:
    The traversability of junctions along the affected road.

### getFreeFlowSpeedInMetersPerSecond

public double getFreeFlowSpeedInMetersPerSecond()

    Gets the reference speed in meters per second along the roadway when no traffic is present.
Specified by:
    [`getFreeFlowSpeedInMetersPerSecond`](sdk-for-android-explore-api-reference-latesttrafficflowbase#getFreeFlowSpeedInMetersPerSecond()) in interface [`TrafficFlowBase`](sdk-for-android-explore-api-reference-latesttrafficflowbase "interface in com.here.sdk.traffic")

    Returns:
    The reference speed in meters per second along the roadway when no traffic is present.

### getJamFactor

public double getJamFactor()

    Gets a value for the amount of traffic on the roadway.

    The value, between 0.0 and 10.0, indicate the expected quality of travel. A value of 0.0 indicates that there is no congestion on the roadway. As the value approaches 10.0, it indicates increasing congestion. A value of 10.0 is reserved to represent a blocked roadway (closure).
Specified by:
    [`getJamFactor`](sdk-for-android-explore-api-reference-latesttrafficflowbase#getJamFactor()) in interface [`TrafficFlowBase`](sdk-for-android-explore-api-reference-latesttrafficflowbase "interface in com.here.sdk.traffic")

    Returns:
    A value for the amount of traffic on the roadway.
