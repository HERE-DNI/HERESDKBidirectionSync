---
title: "GeoCoordinatesUpdate (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeocoordinatesupdate"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoCoordinatesUpdate

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.GeoCoordinatesUpdate
------------------------------------------------------------------------
public final class GeoCoordinatesUpdate extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents geographical coordinates in 3D space. Unlike [`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core"), its members can be undefined, allowing for APIs that update only the specified parts of geo coordinates.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [altitude](#altitude)

Optional altitude in meters.

`final `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [latitude](#latitude)

Optional latitude in degrees.

`final `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [longitude](#longitude)

Optional longitude in degrees.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoCoordinatesUpdate](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates)`

Constructs a GeoCoordinatesUpdate from GeoCoordinates

[GeoCoordinatesUpdate](#%3Cinit%3E(java.lang.Double,java.lang.Double))`(`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` latitude, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` longitude)`

Constructs a GeoCoordinatesUpdate from the provided latitude and longitude values.

[GeoCoordinatesUpdate](#%3Cinit%3E(java.lang.Double,java.lang.Double,java.lang.Double))`(`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` latitude, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` longitude, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` altitude)`

Constructs a GeoCoordinatesUpdate from the provided latitude, longitude and alt values.

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

### latitude

@Nullable public final [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) latitude

    Optional latitude in degrees.

### longitude

@Nullable public final [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) longitude

    Optional longitude in degrees.

### altitude

@Nullable public final [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) altitude

    Optional altitude in meters.

## Constructor Details

  - (java.lang.Double,java.lang.Double)" class="section detail">

### GeoCoordinatesUpdate

public GeoCoordinatesUpdate(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) latitude, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) longitude)

    Constructs a GeoCoordinatesUpdate from the provided latitude and longitude values. Corrects values of latitude and longitude if they exceed the ranges.
Parameters:
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of \[-90.0, 90.0\] it's clamped to that range. NaN value is converted to `null`.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. NaN value is converted to `null`.
- (java.lang.Double,java.lang.Double,java.lang.Double)" class="section detail">

### GeoCoordinatesUpdate

public GeoCoordinatesUpdate(@Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) latitude, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) longitude, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) altitude)

    Constructs a GeoCoordinatesUpdate from the provided latitude, longitude and alt values. Corrects values of latitude and longitude if they exceed the ranges.
Parameters:
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of \[-90.0, 90.0\] it's clamped to that range. NaN value is converted to `null`.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. NaN value is converted to `null`.

    `altitude` -

    Altitude in meters. NaN value is converted to `null`.
- (com.here.sdk.core.GeoCoordinates)" class="section detail">

### GeoCoordinatesUpdate

public GeoCoordinatesUpdate(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates)

    Constructs a GeoCoordinatesUpdate from GeoCoordinates
Parameters:
    `coordinates` -

    GeoCoordinates to construct GeoCoordinatesUpdate.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
