---
title: "TrafficOnSpan (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficonspan"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficOnSpan

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TrafficOnSpan
------------------------------------------------------------------------
public final class TrafficOnSpan extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Traffic information of a span along a route.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [baseSpeedInMetersPerSecond](#baseSpeedInMetersPerSecond)

The speed, in meters per second, without taking traffic into consideration.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [consumptionInKilowattHours](#consumptionInKilowattHours)

The power consumption in kilowatt-hours (kWh) necessary to traverse the span.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [duration](#duration)

The time duration necessary to traverse the traffic span.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`>`

  [incidentIndices](#incidentIndices)

The indices of traffic incidents from the field [`TrafficOnSection.trafficIncidents`](sdk-for-android-explore-api-reference-latesttrafficonsection#trafficIncidents).

`double`

  [jamFactor](#jamFactor)

The traffic jam factor shows the traffic condition in a numeric way.

`double`

  [lengthInMeters](#lengthInMeters)

Length of the traffic span, in meters.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [trafficDelay](#trafficDelay)

The estimated extra time in seconds spent due to traffic delays along this traffic span.

`int`

  [trafficSectionPolylineOffset](#trafficSectionPolylineOffset)

Index over [`TrafficOnSection.geometry`](sdk-for-android-explore-api-reference-latesttrafficonsection#geometry) where this span starts.

`double`

  [trafficSpeedInMetersPerSecond](#trafficSpeedInMetersPerSecond)

The speed, in meters per second, considering traffic.

## Constructor Summary

Constructors

Constructor

  Description

  [TrafficOnSpan](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### trafficSectionPolylineOffset

public int trafficSectionPolylineOffset

    Index over [`TrafficOnSection.geometry`](sdk-for-android-explore-api-reference-latesttrafficonsection#geometry) where this span starts.

### lengthInMeters

public double lengthInMeters

    Length of the traffic span, in meters.

### duration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration

    The time duration necessary to traverse the traffic span. This duration takes also into consideration the delays caused by the traffic.

### trafficDelay

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") trafficDelay

    The estimated extra time in seconds spent due to traffic delays along this traffic span. Negative values indicate that the traffic span can be traversed faster than usual.

### baseSpeedInMetersPerSecond

public double baseSpeedInMetersPerSecond

    The speed, in meters per second, without taking traffic into consideration.

### trafficSpeedInMetersPerSecond

public double trafficSpeedInMetersPerSecond

    The speed, in meters per second, considering traffic.

### jamFactor

public double jamFactor

    The traffic jam factor shows the traffic condition in a numeric way. It is a value in the range \[0.0, 10.0\]. A large jamFactor value means more traffic jam in general. Specifically, 0.0 means free traffic and 10.0 means stationary traffic.

### incidentIndices

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> incidentIndices

    The indices of traffic incidents from the field [`TrafficOnSection.trafficIncidents`](sdk-for-android-explore-api-reference-latesttrafficonsection#trafficIncidents).

### consumptionInKilowattHours

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) consumptionInKilowattHours

    The power consumption in kilowatt-hours (kWh) necessary to traverse the span.

## Constructor Details

  - ()" class="section detail">

### TrafficOnSpan

public TrafficOnSpan()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
