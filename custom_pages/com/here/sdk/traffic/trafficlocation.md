---
title: "TrafficLocation (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficlocation"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficLocation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.traffic.TrafficLocation
------------------------------------------------------------------------
public final class TrafficLocation extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The location reference to the traffic incident.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")`>`

  [additionalPolylines](#additionalPolylines)

List of polylines that were not included in continuous polyline.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [description](#description)

The description of the location.

`int`

  [lengthInMeters](#lengthInMeters)

The affected road length in meters.

[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")

  [polyline](#polyline)

The polyline representing the traffic entity shape.

## Constructor Summary

Constructors

Constructor

  Description

  [TrafficLocation](#%3Cinit%3E(com.here.sdk.core.GeoPolyline,java.util.List,int))`(`[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")` polyline, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")`> additionalPolylines, int lengthInMeters)`

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

### description

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) description

    The description of the location. In general, the language can't be bound to the description. Usually, the language is one of the local languages of the incident region. Note: A localizable description of the incident is part of [`TrafficIncidentBase.getDescription()`](sdk-for-android-explore-api-reference-latesttrafficincidentbase#getDescription()). This description describes only the location where the incident occurred. Defaults to an empty string.

### polyline

@NonNull public [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") polyline

    The polyline representing the traffic entity shape. The current field contains a continuous polyline with no gaps between geo-coordinates. All others following the gap are present in the `additional_polylines` field.

### additionalPolylines

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")\> additionalPolylines

    List of polylines that were not included in continuous polyline. Use this to fill any gaps in the continuous polyline.

### lengthInMeters

public int lengthInMeters

    The affected road length in meters. The length can be 0 only if the incident supplier has provided incomplete data.

## Constructor Details

  - (com.here.sdk.core.GeoPolyline,java.util.List,int)" class="section detail">

### TrafficLocation

public TrafficLocation(@NonNull [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") polyline, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")\> additionalPolylines, int lengthInMeters)

    Creates a new instance.
Parameters:
    `polyline` -

    The polyline representing the traffic entity shape. The current field contains a continuous polyline with no gaps between geo-coordinates. All others following the gap are present in the `additional_polylines` field.

    `additionalPolylines` -

    List of polylines that were not included in continuous polyline. Use this to fill any gaps in the continuous polyline.

    `lengthInMeters` -

    The affected road length in meters. The length can be 0 only if the incident supplier has provided incomplete data.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
