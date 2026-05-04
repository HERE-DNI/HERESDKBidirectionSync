---
title: "LocationIndicator.MarkerType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlocationindicator-markertype"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class LocationIndicator.MarkerType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.LocationIndicator.MarkerType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`LocationIndicator.MarkerType`](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[LocationIndicator](sdk-for-android-explore-api-reference-latestlocationindicator "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum LocationIndicator.MarkerType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")\>
Enum to identify different types of markers of the location indicator.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [NAVIGATION](#NAVIGATION)

Vehicle navigation represented by a green triangular arrow by default.

[NAVIGATION_INACTIVE](#NAVIGATION_INACTIVE)

Vehicle navigation in inactive state, represented by a gray triangular arrow by default.

[PEDESTRIAN](#PEDESTRIAN)

Pedestrian navigation represented by a green dot by default.

[PEDESTRIAN_INACTIVE](#PEDESTRIAN_INACTIVE)

Pedestrian navigation in inactive state, represented by a gray dot by default.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`LocationIndicator.MarkerType`](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`LocationIndicator.MarkerType`](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### PEDESTRIAN

public static final [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview") PEDESTRIAN

    Pedestrian navigation represented by a green dot by default.

### PEDESTRIAN_INACTIVE

public static final [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview") PEDESTRIAN_INACTIVE

    Pedestrian navigation in inactive state, represented by a gray dot by default. It is used when the indicator was set to inactive using [`LocationIndicator.setActive(boolean)`](sdk-for-android-explore-api-reference-latestlocationindicator#setActive(boolean)) in pedestrian mode.

### NAVIGATION

public static final [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview") NAVIGATION

    Vehicle navigation represented by a green triangular arrow by default.

### NAVIGATION_INACTIVE

public static final [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview") NAVIGATION_INACTIVE

    Vehicle navigation in inactive state, represented by a gray triangular arrow by default. It is used when the indicator was set to inactive using [`LocationIndicator.setActive(boolean)`](sdk-for-android-explore-api-reference-latestlocationindicator#setActive(boolean)) in navigation mode.

## Method Details

### values

public static [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [LocationIndicator.MarkerType](sdk-for-android-explore-api-reference-latestlocationindicator-markertype "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
