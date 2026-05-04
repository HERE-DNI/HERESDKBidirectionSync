---
title: "AuthenticationError (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestauthenticationerror"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class AuthenticationError

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core")\>
com.here.sdk.core.AuthenticationError
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`AuthenticationError`](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum AuthenticationError extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core")\>
Authentication error

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [AUTHENTICATION_FAILED](#AUTHENTICATION_FAILED)

Authentication failed.

[INVALID_PARAMETER](#INVALID_PARAMETER)

Invalid parameter is received.

[NO_CONNECTION](#NO_CONNECTION)

Network connection problems.

[OPERATION_AFTER_DISPOSE](#OPERATION_AFTER_DISPOSE)

Method is invoked on object connected to the disposed SDKNativeEngine.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`AuthenticationError`](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`AuthenticationError`](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### INVALID_PARAMETER

public static final [AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core") INVALID_PARAMETER

    Invalid parameter is received. SDK engine and callback must not be null

### AUTHENTICATION_FAILED

public static final [AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core") AUTHENTICATION_FAILED

    Authentication failed. Check your credentials.

### NO_CONNECTION

public static final [AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core") NO_CONNECTION

    Network connection problems.

### OPERATION_AFTER_DISPOSE

public static final [AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core") OPERATION_AFTER_DISPOSE

    Method is invoked on object connected to the disposed SDKNativeEngine.

## Method Details

### values

public static [AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [AuthenticationError](sdk-for-android-explore-api-reference-latestauthenticationerror "enum class in com.here.sdk.core") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
