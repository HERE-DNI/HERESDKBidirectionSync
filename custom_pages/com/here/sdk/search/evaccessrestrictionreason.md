---
title: "EVAccessRestrictionReason (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevaccessrestrictionreason"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class EVAccessRestrictionReason

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")\>
com.here.sdk.search.EVAccessRestrictionReason
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`EVAccessRestrictionReason`](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum EVAccessRestrictionReason extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")\>
Represents the restriction reason of an `EVChargingPool`.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BRAND_ONLY](#BRAND_ONLY)

Vehicle brand-restriction, e.g.

[CAR_SHARING_ONLY](#CAR_SHARING_ONLY)

Charging for car sharing.

[CUSTOMERS_ONLY](#CUSTOMERS_ONLY)

Charging for customers of a hotel, restaurant, store etc.

[OTHER](#OTHER)

Charging is restricted due to other reasons

[TAXIS_ONLY](#TAXIS_ONLY)

Charging for taxis

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`EVAccessRestrictionReason`](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`EVAccessRestrictionReason`](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### CUSTOMERS_ONLY

public static final [EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search") CUSTOMERS_ONLY

    Charging for customers of a hotel, restaurant, store etc.

### BRAND_ONLY

public static final [EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search") BRAND_ONLY

    Vehicle brand-restriction, e.g. Tesla, BMW.

### CAR_SHARING_ONLY

public static final [EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search") CAR_SHARING_ONLY

    Charging for car sharing.

### TAXIS_ONLY

public static final [EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search") TAXIS_ONLY

    Charging for taxis

### OTHER

public static final [EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search") OTHER

    Charging is restricted due to other reasons

## Method Details

### values

public static [EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [EVAccessRestrictionReason](sdk-for-android-explore-api-reference-latestevaccessrestrictionreason "enum class in com.here.sdk.search") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
