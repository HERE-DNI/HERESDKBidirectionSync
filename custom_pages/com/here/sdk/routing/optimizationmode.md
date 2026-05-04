---
title: "OptimizationMode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestoptimizationmode"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class OptimizationMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.OptimizationMode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum OptimizationMode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")\>
Identifiers for different optimizations that can be used during the route calculation while trying to keep the quality of the route being calculated high. The route is considered to be of low quality if it gives the traveler an unpleasant experience, such as having difficult turns or having a lot of turns in general. For example, if there are two possible routes from A to B, one with a length of 1000m and 10 turns, and another with a length of 1050m and only one turn, the second one will be returned as the shortest, although it is 50m longer. Yet, it contains only one turn and it is therefore considered to provide a better traveler experience.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [FASTEST](#FASTEST)

The routing algorithm will attempt to find the fastest route possible, i.e.

[SHORTEST](#SHORTEST)

The routing algorithm will attempt to find the shortest route possible, i.e.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### FASTEST

public static final [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") FASTEST

    The routing algorithm will attempt to find the fastest route possible, i.e. to optimize travel time while at the same time keeping the quality of the route high. For example, the algorithm may favor a route that remains on a highway, even if a shorter route can be achieved by taking a shortcut through side roads.

### SHORTEST

public static final [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") SHORTEST

    The routing algorithm will attempt to find the shortest route possible, i.e. to optimize the length of the route while at the same time keeping the quality of the route high. For example, the algorithm may favor taking a shortcut that ignores speed information, even if a faster route can be achieved by staying on the highway.

## Method Details

### values

public static [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
