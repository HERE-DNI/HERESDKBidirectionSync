---
title: "GeoPolygon (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeopolygon"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoPolygon

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.GeoPolygon
------------------------------------------------------------------------
public final class GeoPolygon extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a `GeoPolygon` area as a series of geographic coordinates, and optionally, a list of inner boundaries (also known as holes). An instance of this class, initialized with appropriate vertices.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`>>`

  [innerBoundaries](#innerBoundaries)

The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.

`final `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`>`

  [vertices](#vertices)

The list of geographic coordinates representing the outer boundary vertices of polygon.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoPolygon](#%3Cinit%3E(com.here.sdk.core.GeoBox))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` geoBox)`

Constructs an instance of this class from [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core").

[GeoPolygon](#%3Cinit%3E(com.here.sdk.core.GeoCircle))`(`[`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")` geoCircle)`

Constructs an instance of this class from [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core").

[GeoPolygon](#%3Cinit%3E(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`> vertices)`

Constructs an instance of this class from the provided vertices.

[GeoPolygon](#%3Cinit%3E(java.util.List,java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`> vertices, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`>> innerBoundaries)`

Constructs an instance of this class from the provided vertices and inner boundaries (holes).

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

### vertices

@NonNull public final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> vertices

    The list of geographic coordinates representing the outer boundary vertices of polygon.

### innerBoundaries

@NonNull public final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\>\> innerBoundaries

    The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.

## Constructor Details

  - (java.util.List)" class="section detail">

### GeoPolygon

public GeoPolygon(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> vertices) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Constructs an instance of this class from the provided vertices. Throws InstantiationError if the number of vertices is less than three.
Parameters:
    `vertices` -

    List of vertices representing the polygon outer boundary in clockwise order.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Instantiation error.
- (java.util.List,java.util.List)" class="section detail">

### GeoPolygon

public GeoPolygon(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> vertices, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\>\> innerBoundaries) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Constructs an instance of this class from the provided vertices and inner boundaries (holes). Throws InstantiationError if the number of vertices is less than three.
Parameters:
    `vertices` -

    List of vertices representing the polygon outer boundary in clockwise order.

    `innerBoundaries` -

    List of polygon inner boundaries (holes), each in counterclockwise order.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Instantiation error.
- (com.here.sdk.core.GeoCircle)" class="section detail">

### GeoPolygon

public GeoPolygon(@NonNull [GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") geoCircle)

    Constructs an instance of this class from [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core").
Parameters:
    `geoCircle` -

    A [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") to be converted into [`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core").
- (com.here.sdk.core.GeoBox)" class="section detail">

### GeoPolygon

public GeoPolygon(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") geoBox)

    Constructs an instance of this class from [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core").
Parameters:
    `geoBox` -

    A rectangle defined by the [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") to be converted into [`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core"). The corner coordinates defined by the [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") will define the outer boundary verticies of the [`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core").

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
