---
title: "FunctionalRoadClass (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestfunctionalroadclass"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class FunctionalRoadClass

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.FunctionalRoadClass
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`FunctionalRoadClass`](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum FunctionalRoadClass extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing")\>
Types of function road class.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [FUNCTIONAL_ROAD_CLASS_1](#FUNCTIONAL_ROAD_CLASS_1)

A road with high volume and maximum speed traffic.

[FUNCTIONAL_ROAD_CLASS_2](#FUNCTIONAL_ROAD_CLASS_2)

A road with high volume and high speed traffic.

[FUNCTIONAL_ROAD_CLASS_3](#FUNCTIONAL_ROAD_CLASS_3)

A road with high volume traffic.

[FUNCTIONAL_ROAD_CLASS_4](#FUNCTIONAL_ROAD_CLASS_4)

A road with high volume traffic at moderate speeds between neighborhoods.

[FUNCTIONAL_ROAD_CLASS_5](#FUNCTIONAL_ROAD_CLASS_5)

A road whose volume and traffic flow are below the level of any other functional class.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`FunctionalRoadClass`](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`FunctionalRoadClass`](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### FUNCTIONAL_ROAD_CLASS_1

public static final [FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing") FUNCTIONAL_ROAD_CLASS_1

    A road with high volume and maximum speed traffic.

### FUNCTIONAL_ROAD_CLASS_2

public static final [FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing") FUNCTIONAL_ROAD_CLASS_2

    A road with high volume and high speed traffic.

### FUNCTIONAL_ROAD_CLASS_3

public static final [FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing") FUNCTIONAL_ROAD_CLASS_3

    A road with high volume traffic.

### FUNCTIONAL_ROAD_CLASS_4

public static final [FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing") FUNCTIONAL_ROAD_CLASS_4

    A road with high volume traffic at moderate speeds between neighborhoods.

### FUNCTIONAL_ROAD_CLASS_5

public static final [FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing") FUNCTIONAL_ROAD_CLASS_5

    A road whose volume and traffic flow are below the level of any other functional class.

## Method Details

### values

public static [FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
