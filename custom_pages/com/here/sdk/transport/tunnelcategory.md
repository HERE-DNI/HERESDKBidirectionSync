---
title: "TunnelCategory (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttunnelcategory"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class TunnelCategory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")\>
com.here.sdk.transport.TunnelCategory
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum TunnelCategory extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")\>
Specifies the tunnel categories.

Tunnels are categorized from B (low risk, few restrictions) to E (high risk) based on their safety features and the potential danger posed by the goods transported through them.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [B](#B)

Category B.

[C](#C)

Category C.

[D](#D)

Category D.

[E](#E)

Category E.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### B

public static final [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") B

    Category B. Prohibited for the transport of hazardous substances which could cause a very large explosion.

### C

public static final [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") C

    Category C. The same restriction as for B, plus hazardous goods which could cause a large explosion or the extensive release of toxic substances.

### D

public static final [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") D

    Category D. The same restrictions as for C plus hazardous goods which could cause a large fire.

### E

public static final [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") E

    Category E. Prohibited for the transport of all hazardous substances. There are some exceptions for certain radioactive substances, clinical waste and samples.

## Method Details

### values

public static [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
