---
title: "PlaceType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestplacetype"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class PlaceType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")\>
com.here.sdk.search.PlaceType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`PlaceType`](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum PlaceType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")\>
Specifies place type of Place result from a search query.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [ADDRESS](#ADDRESS)

Address of a place.

[AREA](#AREA)

Geographical area, for example a country, a city or a district.

[INTERSECTION](#INTERSECTION)

An intersection of two, or more, streets.

[POI](#POI)

Point of interest, for example a shop, restaurant, museum.

[STREET](#STREET)

A street.

[UNKNOWN](#UNKNOWN)

Unknown or missing place type.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`PlaceType`](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`PlaceType`](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### POI

public static final [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") POI

    Point of interest, for example a shop, restaurant, museum.

### ADDRESS

public static final [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") ADDRESS

    Address of a place. It can have different formats based on the addressing system.

### AREA

public static final [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") AREA

    Geographical area, for example a country, a city or a district.

### STREET

public static final [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") STREET

    A street.

### INTERSECTION

public static final [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") INTERSECTION

    An intersection of two, or more, streets. Note: This type is not supported in offline search.

### UNKNOWN

public static final [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") UNKNOWN

    Unknown or missing place type.

## Method Details

### values

public static [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [PlaceType](sdk-for-android-explore-api-reference-latestplacetype "enum class in com.here.sdk.search") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
