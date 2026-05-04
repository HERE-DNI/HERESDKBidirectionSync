---
title: "EVSEStatus (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevsestatus"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class EVSEStatus

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search")\>
com.here.sdk.search.EVSEStatus
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`EVSEStatus`](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum EVSEStatus extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search")\>
EVSE status

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [AVAILABLE](#AVAILABLE)

The EVSE is able to start a new charging session.

[OCCUPIED](#OCCUPIED)

The EVSE is in use.

[OFFLINE](#OFFLINE)

No status information available.

[OTHER](#OTHER)

No status information available.

[OUT_OF_SERVICE](#OUT_OF_SERVICE)

The EVSE is currently out of order.

[RESERVED](#RESERVED)

The EVSE has been reserved for a particular EV driver and is unavailable for other drivers.

[UNAVAILABLE](#UNAVAILABLE)

The EVSE is not available because of a physical barrier, for example a car.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`EVSEStatus`](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`EVSEStatus`](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### AVAILABLE

public static final [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") AVAILABLE

    The EVSE is able to start a new charging session.

### OCCUPIED

public static final [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") OCCUPIED

    The EVSE is in use.

### OFFLINE

public static final [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") OFFLINE

    No status information available. Also used when offline.

### OTHER

public static final [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") OTHER

    No status information available. Also used when offline.

### OUT_OF_SERVICE

public static final [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") OUT_OF_SERVICE

    The EVSE is currently out of order.

### RESERVED

public static final [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") RESERVED

    The EVSE has been reserved for a particular EV driver and is unavailable for other drivers.

### UNAVAILABLE

public static final [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") UNAVAILABLE

    The EVSE is not available because of a physical barrier, for example a car.

## Method Details

### values

public static [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [EVSEStatus](sdk-for-android-explore-api-reference-latestevsestatus "enum class in com.here.sdk.search") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
