---
title: "MapSceneLights.Category (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapscenelights-category"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class MapSceneLights.Category

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.MapSceneLights.Category
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[MapSceneLights](sdk-for-android-explore-api-reference-latestmapscenelights "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum MapSceneLights.Category extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")\>
The scene uses three categories of lighting which are: Main light, Back light and Rim light. These lights are directional lights.

The properties of all lights have an impact on the shading of 3D objects, for instance, extruded buildings within the scene. However, shadow casting is only affected by the direction of the main light.

Category primarily serves as an identifier type for managing the lights.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BACK](#BACK)

Back light

[MAIN](#MAIN)

Main light

[RIM](#RIM)

Rim light

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`MapSceneLights.Category`](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### MAIN

public static final [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") MAIN

    Main light

### BACK

public static final [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") BACK

    Back light

### RIM

public static final [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") RIM

    Rim light

## Method Details

### values

public static [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [MapSceneLights.Category](sdk-for-android-explore-api-reference-latestmapscenelights-category "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
