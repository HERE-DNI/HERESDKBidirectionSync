---
title: "TrafficOnSection (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficonsection"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficOnSection

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.TrafficOnSection
------------------------------------------------------------------------
public final class TrafficOnSection extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Traffic information on a section.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")

  [arrivalPlace](#arrivalPlace)

Describes the arrival place.

[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")

  [departurePlace](#departurePlace)

Describes the departure place.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`>`

  [geometry](#geometry)

List of coordinates representing the polyline of this section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficIncidentOnRoute`](sdk-for-android-explore-api-reference-latesttrafficincidentonroute "class in com.here.sdk.routing")`>`

  [trafficIncidents](#trafficIncidents)

List of traffic incidents.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficOnSpan`](sdk-for-android-explore-api-reference-latesttrafficonspan "class in com.here.sdk.routing")`>`

  [trafficSpans](#trafficSpans)

List of traffic spans.

## Constructor Summary

Constructors

Constructor

  Description

  [TrafficOnSection](#%3Cinit%3E(com.here.sdk.routing.RoutePlace,com.here.sdk.routing.RoutePlace))`(`[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")` departurePlace, `[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")` arrivalPlace)`

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

### geometry

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> geometry

    List of coordinates representing the polyline of this section.

### trafficSpans

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficOnSpan](sdk-for-android-explore-api-reference-latesttrafficonspan "class in com.here.sdk.routing")\> trafficSpans

    List of traffic spans.

### trafficIncidents

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficIncidentOnRoute](sdk-for-android-explore-api-reference-latesttrafficincidentonroute "class in com.here.sdk.routing")\> trafficIncidents

    List of traffic incidents.

### departurePlace

@NonNull public [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") departurePlace

    Describes the departure place.

### arrivalPlace

@NonNull public [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") arrivalPlace

    Describes the arrival place.

## Constructor Details

  - (com.here.sdk.routing.RoutePlace,com.here.sdk.routing.RoutePlace)" class="section detail">

### TrafficOnSection

public TrafficOnSection(@NonNull [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") departurePlace, @NonNull [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") arrivalPlace)

    Creates a new instance.
Parameters:
    `departurePlace` -

    Describes the departure place.

    `arrivalPlace` -

    Describes the arrival place.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
