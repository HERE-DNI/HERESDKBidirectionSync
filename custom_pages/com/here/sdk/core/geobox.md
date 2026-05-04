---
title: "GeoBox (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeobox"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeoBox

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.core.GeoBox
------------------------------------------------------------------------
public final class GeoBox extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a bounding rectangle aligned with latitude and longitude. Geographic area represented by this would be visualised as a rectangle when using a normal cylindrical projection (such as Mercator). The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction. The box with equal values in longitude for the corners is considered as a span of 360 degrees. The box is considered empty if the latitude of the [`southWestCorner`](#southWestCorner) is larger than the the latitude of the [`northEastCorner`](#northEastCorner).

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [northEastCorner](#northEastCorner)

North east corner coordinates.

`final `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [southWestCorner](#southWestCorner)

South west corner coordinates.

## Constructor Summary

Constructors

Constructor

  Description

  [GeoBox](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` southWestCorner, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` northEastCorner)`

Creates a new instance.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [containing](#containing(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`> geoCoordinates)`

Creates a `GeoBox` which encompases all coordinates from the list.

`boolean`

  [contains](#contains(com.here.sdk.core.GeoBox))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` geoBox)`

Determines whether the specified `GeoBox` is covered entirely by this `GeoBox`.

`boolean`

  [contains](#contains(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` geoCoordinates)`

Determines whether the specified GeoCoordinates is contained within this `GeoBox`.

[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [envelope](#envelope(com.here.sdk.core.GeoBox))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` geoBox)`

Envelopes two `GeoBox` areas by returning the smallest `GeoBox` covering both this GeoBox and the specified `GeoBox`.

`static `[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [envelopeGeoBoxes](#envelopeGeoBoxes(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")`> geoBoxes)`

Envelopes the list of `GeoBox` areas by returning the smallest `GeoBox` covering all specified `GeoBox` objects.

`boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [expandedBy](#expandedBy(double,double,double,double))`(double southMeters, double westMeters, double northMeters, double eastMeters)`

Creates a `GeoBox` which is expanded by a fixed distance.

`int`

  [hashCode](#hashCode())`()`

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")`>`

  [intersection](#intersection(com.here.sdk.core.GeoBox))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` geoBox)`

Computes the intersection with the passed [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core").

`static `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")`>`

  [intersection](#intersection(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")`> geoBoxes)`

Computes intersection of list of [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") instances.

`boolean`

  [intersects](#intersects(com.here.sdk.core.GeoBox))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` geoBox)`

Determines whether this `GeoBox` intersects with the passed `GeoBox`.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### southWestCorner

@NonNull public final [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") southWestCorner

    South west corner coordinates.

### northEastCorner

@NonNull public final [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") northEastCorner

    North east corner coordinates.

## Constructor Details

  - (com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates)" class="section detail">

### GeoBox

public GeoBox(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") southWestCorner, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") northEastCorner)

    Creates a new instance.
Parameters:
    `southWestCorner` -

    South west corner coordinates.

    `northEastCorner` -

    North east corner coordinates.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### containing

@Nullable public static [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") containing(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> geoCoordinates)

    Creates a `GeoBox` which encompases all coordinates from the list. The provided list must contain at least two points. The altitude values of the input coordinates are not considered for the result.
Parameters:
    `geoCoordinates` -

    List of coordinates to encompass inside bounding box.

    Returns:
    `GeoBox` containing all supplied coordinates, or `null` if less than two coordinates were provided.

### envelope

@NonNull public [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") envelope(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") geoBox)

    Envelopes two `GeoBox` areas by returning the smallest `GeoBox` covering both this GeoBox and the specified `GeoBox`.
Parameters:
    `geoBox` -

    Another `GeoBox` to envelope with.

    Returns:
    `GeoBox` covering two`GeoBox` areas

### envelopeGeoBoxes

@Nullable public static [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") envelopeGeoBoxes(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")\> geoBoxes)

    Envelopes the list of `GeoBox` areas by returning the smallest `GeoBox` covering all specified `GeoBox` objects.
Parameters:
    `geoBoxes` -

    List of `GeoBox` objects.

    Returns:
    `GeoBox` covering all `GeoBox` areas, or `null` if input is empty.

### intersects

public boolean intersects(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") geoBox)

    Determines whether this `GeoBox` intersects with the passed `GeoBox`. The altitude values are ignored.
Parameters:
    `geoBox` -

    A `GeoBox` to check for intersection.

    Returns:
    `true` if intersects with the `GeoBox`, `false` otherwise.

### intersection

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")\> intersection(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") geoBox)

    Computes the intersection with the passed [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core"). The altitude values are ignored. Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `geoBox` -

    Another geo box to check intersection with.

    Returns:
    It will be empty if there is no overlap. Otherwise, 1 or more geo boxes covering common area by this and passed [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core").

### intersection

@NonNull public static [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")\> intersection(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")\> geoBoxes)

    Computes intersection of list of [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") instances. The altitude values are ignored. Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `geoBoxes` -

    List of [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") instances.

    Returns:
    It will be empty if there is no overlap between all the passed [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") instances. Otherwise, 1 or more geo boxes covering common area by all the passed [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") instances.

### contains

public boolean contains(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") geoBox)

    Determines whether the specified `GeoBox` is covered entirely by this `GeoBox`. The altitude values are ignored.
Parameters:
    `geoBox` -

    A `GeoBox` to check for containment within this `GeoBox`.

    Returns:
    `true` if covered by the `GeoBox`, `false` otherwise.

### contains

public boolean contains(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") geoCoordinates)

    Determines whether the specified GeoCoordinates is contained within this `GeoBox`. The altitude values are ignored.
Parameters:
    `geoCoordinates` -

    A GeoCoordinates to check for containment within this `GeoBox`.

    Returns:
    `true` if contained within the `GeoBox`, `false` otherwise.

### expandedBy

@NonNull public [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") expandedBy(double southMeters, double westMeters, double northMeters, double eastMeters) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a `GeoBox` which is expanded by a fixed distance. Throws an InstantiationError if it is not possible to create a valid `GeoBox` with the given arguments.
Parameters:
    `southMeters` -

    Distance in the south direction in meters to expand the `GeoBox`.

    `westMeters` -

    Distance in the west direction in meters to expand the `GeoBox`.

    `northMeters` -

    Distance in the north direction in meters to expand the `GeoBox`.

    `eastMeters` -

    Distance in the east direction in meters to expand the `GeoBox`.

    Returns:
    The expanded `GeoBox`.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Instantiation error.
