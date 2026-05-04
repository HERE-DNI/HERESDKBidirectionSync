---
title: "GeoCoordinates (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeocoordinates"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoCoordinates

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.GeoCoordinates
------------------------------------------------------------------------
public final class GeoCoordinates extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents geographical coordinates in 3D space.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [altitude](#altitude)

Optional altitude in meters.

`final double`

  [latitude](#latitude)

Latitude in degrees.

`final double`

  [longitude](#longitude)

Longitude in degrees.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoCoordinates](#%3Cinit%3E(double,double))`(double latitude, double longitude)`

Constructs a GeoCoordinates from the provided latitude and longitude values.

[GeoCoordinates](#%3Cinit%3E(double,double,double))`(double latitude, double longitude, double altitude)`

Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `double`

  [distanceTo](#distanceTo(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` point)`

Computes distance (in meters) along the great circle between two coordinates.

`boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `static `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [fromString](#fromString(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` input)`

Constructs GeoCoordinates from the provided string in specified format.

`int`

  [hashCode](#hashCode())`()`

  [`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [interpolate](#interpolate(com.here.sdk.core.GeoCoordinates,double))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` towardCoords, double factor)`

Computes the coordinates of the interpolated location along the great circle between the two coordinates.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### latitude

public final double latitude

    Latitude in degrees.

### longitude

public final double longitude

    Longitude in degrees.

### altitude

@Nullable public final [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) altitude

    Optional altitude in meters. By convention, on iOS devices, altitude is set as meters relative to the mean sea level. On Android devices, altitude is set as meters relative to the WGS 84 reference ellipsoid.

## Constructor Details

  - (double,double,double)" class="section detail">

### GeoCoordinates

public GeoCoordinates(double latitude, double longitude, double altitude)

    Constructs a GeoCoordinates from the provided latitude, longitude and altitude values. Corrects values of lat and long if they exceed the ranges.
Parameters:
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of \[-90.0, 90.0\] it's clamped to that range. NaN value is converted to 0.0.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. NaN value is converted to 0.0.

    `altitude` -

    Altitude in meters. NaN value is converted to `null`.
- (double,double)" class="section detail">

### GeoCoordinates

public GeoCoordinates(double latitude, double longitude)

    Constructs a GeoCoordinates from the provided latitude and longitude values. Corrects values of latitude and longitude if they exceed the ranges. Altitude set to `null`.
Parameters:
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of \[-90.0, 90.0\] it's clamped to that range. NaN value is converted to 0.0.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. NaN value is converted to 0.0.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### distanceTo

public double distanceTo(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") point)

    Computes distance (in meters) along the great circle between two coordinates. This method ignores altitude of both points.
Parameters:
    `point` -

    Coordinates of the point to which the distance is computed.

    Returns:
    distance in meters.

### interpolate

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") interpolate(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") towardCoords, double factor)

    Computes the coordinates of the interpolated location along the great circle between the two coordinates.

    The interpolation factor is clamped to the range `[0.0, 1.0]` where `0.0` identifies this `GeoCoordinates` and `1.0` indicates the other coordinates.

    The ratio between the distance to the interpolated coordinates and the distance to the other coordinates is approximately equal to the interpolation factor. When both coordinates have the altitude, then the altitude is interpolated as well; `null` otherwise.
Parameters:
    `towardCoords` -

    Coordinates of the point to which the interpolation is directed.

    `factor` -

    The interpolation factor

    Returns:
    interpolated coordinates

### fromString

@Nullable public static [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") fromString(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) input)

    Constructs GeoCoordinates from the provided string in specified format. Corrects values of lat and long if they exceed the ranges. If the latitude value is out of range of \[-90.0, 90.0\] it's clamped to that range. If the longitude value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. Examples: `53.43762,-13.65468`. `49°59'56.948"N, 15°48'22.989"E` `50d4m17.698N 14d24m2.826E` `49.9991522N, 150.8063858E` `40°26′47″N 79°58′36″W`
Parameters:
    `input` -

    String representing GeoCoordinates in one of supported formats.

    Returns:
    Created GeoCoordinates, or 'null' if string was not in appropriate format.
