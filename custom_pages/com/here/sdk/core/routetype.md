---
title: "RouteType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutetype"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class RouteType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")\>
com.here.sdk.core.RouteType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`RouteType`](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum RouteType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")\>
Indicates the level of significance of a route in a range from 1 to 6. A value of 1 stands for the most major route and 6 the most minor. The route type indicates that the road's name is actually a route number and in many countries is displayed in a shield symbol (e.g., Interstate and State routes in the U.S.). See https://developer.here.com/documentation/here-map-content-schema/dev_guide/topics_schema/streetname.routetype.html

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [LEVEL_1_ROAD](#LEVEL_1_ROAD)

International / European road

[LEVEL_2_ROAD](#LEVEL_2_ROAD)

National road

[LEVEL_3_ROAD](#LEVEL_3_ROAD)

Primary road

[LEVEL_4_ROAD](#LEVEL_4_ROAD)

Secondary road

[LEVEL_5_ROAD](#LEVEL_5_ROAD)

Minor road

[LEVEL_6_ROAD](#LEVEL_6_ROAD)

Avenue

[TYPE_UNKNOWN](#TYPE_UNKNOWN)

Unknown

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`RouteType`](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`RouteType`](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### TYPE_UNKNOWN

public static final [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") TYPE_UNKNOWN

    Unknown

### LEVEL_1_ROAD

public static final [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") LEVEL_1_ROAD

    International / European road

### LEVEL_2_ROAD

public static final [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") LEVEL_2_ROAD

    National road

### LEVEL_3_ROAD

public static final [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") LEVEL_3_ROAD

    Primary road

### LEVEL_4_ROAD

public static final [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") LEVEL_4_ROAD

    Secondary road

### LEVEL_5_ROAD

public static final [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") LEVEL_5_ROAD

    Minor road

### LEVEL_6_ROAD

public static final [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") LEVEL_6_ROAD

    Avenue

## Method Details

### values

public static [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [RouteType](sdk-for-android-explore-api-reference-latestroutetype "enum class in com.here.sdk.core") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
