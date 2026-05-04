---
title: "CategoryQuery.Area (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcategoryquery-area"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class CategoryQuery.Area

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.CategoryQuery.Area
Enclosing class:
[CategoryQuery](sdk-for-android-explore-api-reference-latestcategoryquery "class in com.here.sdk.search")

------------------------------------------------------------------------
public static final class CategoryQuery.Area extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Area to perform search on.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [areaCenter](#areaCenter)

Geographic coordinates of the center around which to provide the most relevant places.

`final `[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [boxArea](#boxArea)

Geographic rectangle area in which to provide the most relevant places.

`final `[`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")

  [circleArea](#circleArea)

Geographic circle area in which to provide the most relevant places.

`final `[`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")

  [corridorArea](#corridorArea)

Geographic corridor area in which to provide the most relevant places.

## Constructor Summary

Constructors

Constructor

  Description

  [Area](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` areaCenter)`

Constructs a new instance of this class from provided parameters.

[Area](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoBox))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` areaCenter, `[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` boxArea)`

Constructs a new instance of this class from provided parameters.

[Area](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCircle))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` areaCenter, `[`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")` circleArea)`

Constructs a new instance of this class from provided parameters.

[Area](#%3Cinit%3E(com.here.sdk.core.GeoCorridor,com.here.sdk.core.GeoCoordinates))`(`[`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")` corridorArea, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` areaCenter)`

Constructs a new instance of this class from provided parameters.

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

### areaCenter

@NonNull public final [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter

    Geographic coordinates of the center around which to provide the most relevant places.

### boxArea

@Nullable public final [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") boxArea

    Geographic rectangle area in which to provide the most relevant places.

### circleArea

@Nullable public final [GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") circleArea

    Geographic circle area in which to provide the most relevant places.

### corridorArea

@Nullable public final [GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core") corridorArea

    Geographic corridor area in which to provide the most relevant places. The contained polyline and half-width define the area that will be used in a search query.

    When used with `SearchEngine`, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.

    When [`corridorArea`](#corridorArea) is provided, [`areaCenter`](#areaCenter) has to be within it, otherwise [`areaCenter`](#areaCenter) is ignored when searching.

## Constructor Details

  - (com.here.sdk.core.GeoCoordinates)" class="section detail">

### Area

public Area(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter)

    Constructs a new instance of this class from provided parameters.
Parameters:
    `areaCenter` -

    Geographic coordinates of the center around which to provide the most relevant places.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoBox)" class="section detail">

### Area

public Area(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter, @NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") boxArea)

    Constructs a new instance of this class from provided parameters.
Parameters:
    `areaCenter` -

    Geographic coordinates of the center around which to provide the most relevant places.

    `boxArea` -

    Geographic rectangle area in which to provide the most relevant places.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCircle)" class="section detail">

### Area

public Area(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter, @NonNull [GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") circleArea)

    Constructs a new instance of this class from provided parameters.
Parameters:
    `areaCenter` -

    Geographic coordinates of the center around which to provide the most relevant places.

    `circleArea` -

    Geographic circle area in which to provide the most relevant places.
- (com.here.sdk.core.GeoCorridor,com.here.sdk.core.GeoCoordinates)" class="section detail">

### Area

public Area(@NonNull [GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core") corridorArea, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") areaCenter)

    Constructs a new instance of this class from provided parameters. The given corridor and center define the area that will be used in the search query.

    When used with `SearchEngine`, the polyline is compressed and sent. More complex polylines with large amounts of coordinates and with smaller half-width may have the less relevant part removed, such as the one far away from the search center. This usually makes no difference, because there will be enough POIs near the search center. For use cases where it is important to search the entire polyline, half-width can be increased or not set. For example: Route between New York and Chicago with half-width 800 will be added to request without removing the far away part, but route of the same length (around 360km) between Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.

    The area center has to be within the corridor, otherwise it is ignored.
Parameters:
    `corridorArea` -

    Geographic corridor area in which to provide the most relevant places.

    `areaCenter` -

    Geographic coordinates of the prioritized area center.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
