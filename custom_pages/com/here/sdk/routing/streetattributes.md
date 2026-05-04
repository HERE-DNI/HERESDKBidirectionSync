---
title: "StreetAttributes (API Reference)"
slug: "sdk-for-android-explore-api-reference-lateststreetattributes"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class StreetAttributes

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.StreetAttributes
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`StreetAttributes`](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum StreetAttributes extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")\>
Types of street attributes.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BRIDGE](#BRIDGE)

The street goes over a bridge.

[BUILT_UP_AREA](#BUILT_UP_AREA)

The street is most likely in a built-up area.

[CONTROLLED_ACCESS_HIGHWAY](#CONTROLLED_ACCESS_HIGHWAY)

The street is either a controlled access or a limited access road or both.

[DIRT_ROAD](#DIRT_ROAD)

The street is a dirt road.

[DIVIDED_ROAD](#DIVIDED_ROAD)

The street is a divided road.

[MOTORWAY](#MOTORWAY)

The street is a motorway.

[PRIVATE_ROAD](#PRIVATE_ROAD)

The street is a private road.

[RAMP](#RAMP)

The street contains a ramp.

[RIGHT_DRIVING_SIDE](#RIGHT_DRIVING_SIDE)

The driving on the street is done on the right side.

[ROUNDABOUT](#ROUNDABOUT)

The street contains a roundabout.

[TUNNEL](#TUNNEL)

The street goes through a tunnel.

[UNDER_CONSTRUCTION](#UNDER_CONSTRUCTION)

The street is under construction.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`StreetAttributes`](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`StreetAttributes`](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### RIGHT_DRIVING_SIDE

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") RIGHT_DRIVING_SIDE

    The driving on the street is done on the right side.

### DIRT_ROAD

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") DIRT_ROAD

    The street is a dirt road.

### TUNNEL

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") TUNNEL

    The street goes through a tunnel.

### BRIDGE

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") BRIDGE

    The street goes over a bridge.

### RAMP

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") RAMP

    The street contains a ramp.

### ROUNDABOUT

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") ROUNDABOUT

    The street contains a roundabout.

### UNDER_CONSTRUCTION

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") UNDER_CONSTRUCTION

    The street is under construction.

### DIVIDED_ROAD

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") DIVIDED_ROAD

    The street is a divided road.

### MOTORWAY

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") MOTORWAY

    The street is a motorway.

### PRIVATE_ROAD

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") PRIVATE_ROAD

    The street is a private road.

### BUILT_UP_AREA

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") BUILT_UP_AREA

    The street is most likely in a built-up area.

### CONTROLLED_ACCESS_HIGHWAY

public static final [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") CONTROLLED_ACCESS_HIGHWAY

    The street is either a controlled access or a limited access road or both.

## Method Details

### values

public static [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
