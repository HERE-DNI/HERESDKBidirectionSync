---
title: "RoadFeatures (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroadfeatures"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class RoadFeatures

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.RoadFeatures
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`RoadFeatures`](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum RoadFeatures extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")\>
Road features or states.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [CAR_SHUTTLE_TRAIN](#CAR_SHUTTLE_TRAIN)

This part of the route is for transit with a car shuttle train.

[CONTROLLED_ACCESS_HIGHWAY](#CONTROLLED_ACCESS_HIGHWAY)

This part of the route is a controlled-access highway, i.e.

[DIRT_ROAD](#DIRT_ROAD)

This part of the route has an un-paved surface.

[FERRY](#FERRY)

This part of the route is for transit with a ferry.

[SEASONAL_CLOSURE](#SEASONAL_CLOSURE)

This part of the route is subject to seasonal closure.

[TOLL_ROAD](#TOLL_ROAD)

Access to this part of the route is restricted with a fee or toll.

[TUNNEL](#TUNNEL)

This part of the route is a tunnel.

[U_TURNS](#U_TURNS)

This part of the route has a u-turns.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`RoadFeatures`](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`RoadFeatures`](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### SEASONAL_CLOSURE

public static final [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") SEASONAL_CLOSURE

    This part of the route is subject to seasonal closure.

### TOLL_ROAD

public static final [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") TOLL_ROAD

    Access to this part of the route is restricted with a fee or toll.

### CONTROLLED_ACCESS_HIGHWAY

public static final [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") CONTROLLED_ACCESS_HIGHWAY

    This part of the route is a controlled-access highway, i.e. high-speed and highly controlled.

### FERRY

public static final [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") FERRY

    This part of the route is for transit with a ferry.

### CAR_SHUTTLE_TRAIN

public static final [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") CAR_SHUTTLE_TRAIN

    This part of the route is for transit with a car shuttle train.

### TUNNEL

public static final [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") TUNNEL

    This part of the route is a tunnel.

### DIRT_ROAD

public static final [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") DIRT_ROAD

    This part of the route has an un-paved surface.

### U_TURNS

public static final [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") U_TURNS

    This part of the route has a u-turns. Note that this feature is valid only for cars, trucks, taxis and buses.

## Method Details

### values

public static [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
