---
title: "JsonStyleFactory.InstantiationErrorCode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class JsonStyleFactory.InstantiationErrorCode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview")\>
com.here.sdk.mapview.JsonStyleFactory.InstantiationErrorCode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`JsonStyleFactory.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[JsonStyleFactory](sdk-for-android-explore-api-reference-latestjsonstylefactory "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static enum JsonStyleFactory.InstantiationErrorCode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview")\>
Describes reasons for failing to create a [`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") from a JSON source.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [INVALID_JSON_STYLE_SYNTAX](#INVALID_JSON_STYLE_SYNTAX)

JSON style syntax validation failed.

[MALFORMED_JSON_CONTENT](#MALFORMED_JSON_CONTENT)

JSON parsing failed.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`JsonStyleFactory.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`JsonStyleFactory.InstantiationErrorCode`](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### MALFORMED_JSON_CONTENT

public static final [JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview") MALFORMED_JSON_CONTENT

    JSON parsing failed.

### INVALID_JSON_STYLE_SYNTAX

public static final [JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview") INVALID_JSON_STYLE_SYNTAX

    JSON style syntax validation failed.

## Method Details

### values

public static [JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [JsonStyleFactory.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestjsonstylefactory-instantiationerrorcode "enum class in com.here.sdk.mapview") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
