---
title: "JunctionsTraversability (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestjunctionstraversability"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class JunctionsTraversability

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")\>
com.here.sdk.traffic.JunctionsTraversability
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`JunctionsTraversability`](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum JunctionsTraversability extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")\>
Junctions traversability of some traffic incident or flow section.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [ALL_CLOSED](#ALL_CLOSED)

All junctions are closed.

[ALL_OPEN](#ALL_OPEN)

All junctions are open.

[END_OPEN_OTHERS_CLOSED](#END_OPEN_OTHERS_CLOSED)

First edge junction is open, all others are closed.

[INTERMEDIATE_CLOSED_EDGE_OPEN](#INTERMEDIATE_CLOSED_EDGE_OPEN)

Junctions at the beginning and end of the roadway are open, intermediate junctions are closed.

[START_OPEN_OTHERS_CLOSED](#START_OPEN_OTHERS_CLOSED)

First edge junction is open, all others are closed.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`JunctionsTraversability`](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`JunctionsTraversability`](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### ALL_OPEN

public static final [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic") ALL_OPEN

    All junctions are open.

### ALL_CLOSED

public static final [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic") ALL_CLOSED

    All junctions are closed.

### INTERMEDIATE_CLOSED_EDGE_OPEN

public static final [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic") INTERMEDIATE_CLOSED_EDGE_OPEN

    Junctions at the beginning and end of the roadway are open, intermediate junctions are closed.

### START_OPEN_OTHERS_CLOSED

public static final [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic") START_OPEN_OTHERS_CLOSED

    First edge junction is open, all others are closed.

### END_OPEN_OTHERS_CLOSED

public static final [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic") END_OPEN_OTHERS_CLOSED

    First edge junction is open, all others are closed.

## Method Details

### values

public static [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [JunctionsTraversability](sdk-for-android-explore-api-reference-latestjunctionstraversability "enum class in com.here.sdk.traffic") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
