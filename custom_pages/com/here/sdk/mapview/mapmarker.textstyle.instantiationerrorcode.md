---
title: "MapMarker.TextStyle.InstantiationErrorCode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class MapMarker.TextStyle.InstantiationErrorCode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.MapMarker.TextStyle.InstantiationErrorCode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`MapMarker.TextStyle.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[MapMarker.TextStyle](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum MapMarker.TextStyle.InstantiationErrorCode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview")\>
Describes a reason for failing to create a [`MapMarker.TextStyle`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle "class in com.here.sdk.mapview").

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [DUPLICATE_TEXT_PLACEMENT_VALUES](#DUPLICATE_TEXT_PLACEMENT_VALUES)

Instantiation parameters contain unsupported list with duplicate [`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") entries.

[EMPTY_TEXT_PLACEMENT_LIST](#EMPTY_TEXT_PLACEMENT_LIST)

Instantiation parameters contain unsupported empty list without any [`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") entries.

[NEGATIVE_TEXT_OUTLINE_SIZE](#NEGATIVE_TEXT_OUTLINE_SIZE)

Instantiation parameters contain unsupported negative text outline size.

[NON_POSITIVE_TEXT_SIZE](#NON_POSITIVE_TEXT_SIZE)

Instantiation parameters contain unsupported non positive text size.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapMarker.TextStyle.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`MapMarker.TextStyle.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### NON_POSITIVE_TEXT_SIZE

public static final [MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview") NON_POSITIVE_TEXT_SIZE

    Instantiation parameters contain unsupported non positive text size.

### NEGATIVE_TEXT_OUTLINE_SIZE

public static final [MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview") NEGATIVE_TEXT_OUTLINE_SIZE

    Instantiation parameters contain unsupported negative text outline size.

### EMPTY_TEXT_PLACEMENT_LIST

public static final [MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview") EMPTY_TEXT_PLACEMENT_LIST

    Instantiation parameters contain unsupported empty list without any [`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") entries.

### DUPLICATE_TEXT_PLACEMENT_VALUES

public static final [MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview") DUPLICATE_TEXT_PLACEMENT_VALUES

    Instantiation parameters contain unsupported list with duplicate [`MapMarker.TextStyle.Placement`](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-placement "enum class in com.here.sdk.mapview") entries.

## Method Details

### values

public static [MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [MapMarker.TextStyle.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker-textstyle-instantiationerrorcode "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
