---
title: "MapMarker3DModel.InstantiationErrorCode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class MapMarker3DModel.InstantiationErrorCode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapMarker3DModel.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.MapMarker3DModel.InstantiationErrorCode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`MapMarker3DModel.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[MapMarker3DModel](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum MapMarker3DModel.InstantiationErrorCode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapMarker3DModel.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview")\>
Indicates the reason for a failure to create [`MapMarker3DModel`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel "class in com.here.sdk.mapview").

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [MISSING_TEXTURE_COORDINATES](#MISSING_TEXTURE_COORDINATES)

The provided [`Mesh`](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview") does not contain texture coordinates.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapMarker3DModel.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`MapMarker3DModel.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### MISSING_TEXTURE_COORDINATES

public static final [MapMarker3DModel.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview") MISSING_TEXTURE_COORDINATES

    The provided [`Mesh`](sdk-for-android-explore-api-reference-latestmesh "class in com.here.sdk.mapview") does not contain texture coordinates.

## Method Details

### values

public static [MapMarker3DModel.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [MapMarker3DModel.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmapmarker3dmodel-instantiationerrorcode "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
