---
title: "GeoPolyline (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeopolyline"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoPolyline

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.GeoPolyline
------------------------------------------------------------------------
public final class GeoPolyline extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A list of geographic coordinates representing the vertices of a polyline. An instance of this class, initialized with appropriate vertices. Represents a `GeoPolyline` as a series of geographic coordinates.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`>`

  [vertices](#vertices)

The list of vertices representing the polyline.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoPolyline](#%3Cinit%3E(com.here.sdk.core.GeoBox))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` geoBox)`

Constructs an instance of this class from [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core").

[GeoPolyline](#%3Cinit%3E(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`> vertices)`

Constructs a GeoPolyline from the provided vertices.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [coordinatesAtOffsetInMeters](#coordinatesAtOffsetInMeters(double,com.here.sdk.core.GeoPolylineDirection))`(double offsetInMeters, `[`GeoPolylineDirection`](sdk-for-android-explore-api-reference-latestgeopolylinedirection "enum class in com.here.sdk.core")` direction)`

Returns the coordinates at the given distance along the polyline.

`boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `long`

  [getNearestIndexTo](#getNearestIndexTo(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` point)`

Returns the index of the nearest vertex to the given point.

`int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### vertices

@NonNull public final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> vertices

    The list of vertices representing the polyline.

## Constructor Details

  - (java.util.List)" class="section detail">

### GeoPolyline

public GeoPolyline(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> vertices) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Constructs a GeoPolyline from the provided vertices. Throws an InstantiationError if the number of vertices is less than two.
Parameters:
    `vertices` -

    List of vertices representing the polyline.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Instantiation error.
- (com.here.sdk.core.GeoBox)" class="section detail">

### GeoPolyline

public GeoPolyline(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") geoBox)

    Constructs an instance of this class from [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core").
Parameters:
    `geoBox` -

    A rectangle defined by the [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") to be converted into [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core"). The corner coordinates of the [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") will define the points of the resulting [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core").

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### getNearestIndexTo

public long getNearestIndexTo(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") point)

    Returns the index of the nearest vertex to the given point.
Parameters:
    `point` -

    Coordinates of the point.

    Returns:
    Index of the closest vertex of the polyline.

### coordinatesAtOffsetInMeters

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinatesAtOffsetInMeters(double offsetInMeters, @NonNull [GeoPolylineDirection](sdk-for-android-explore-api-reference-latestgeopolylinedirection "enum class in com.here.sdk.core") direction)

    Returns the coordinates at the given distance along the polyline. When the polyline is traversed from the beginning, the distance is calculated from the start of the polyline; while a direction from the end indicates a distance from the last vertex.

    The offset is expected to be non-negative and smaller than the length of the polyline. When the offset is negative, the function returns the starting end point of the polyline, i.e. the first vertex in positive direction and the last vertex in the negative direction. Similarly, when the offset is larger than the length of the polyline, then the function returns the opposite end point of the polyline.

    The distance between two consecutive vertices is calculated using the [`GeoCoordinates.distanceTo(com.here.sdk.core.GeoCoordinates)`](sdk-for-android-explore-api-reference-latestgeocoordinates#distanceTo(com.here.sdk.core.GeoCoordinates)) function. Therefore, it computes the distance (in meters) along the great circle between the two vertices. Similarly, the full length of the polyline is the sum of the distances between its vertices. The interpolation coordinates between two vertices is calculated using the [`GeoCoordinates.interpolate(com.here.sdk.core.GeoCoordinates, double)`](sdk-for-android-explore-api-reference-latestgeocoordinates#interpolate(com.here.sdk.core.GeoCoordinates,double)) function.

    Note: the result may different from the analogue result from other matching components since they may adapt the result to the length of the underlying object described by the polyline.
Parameters:
    `offsetInMeters` -

    The distance along the polyline in meters

    `direction` -

    The direction in which the polyline is traversed.

    Returns:
    The coordinates of the point at the given distance
