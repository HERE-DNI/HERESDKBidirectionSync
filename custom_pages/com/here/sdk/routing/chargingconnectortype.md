---
title: "ChargingConnectorType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestchargingconnectortype"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class ChargingConnectorType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.ChargingConnectorType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum ChargingConnectorType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\>
Available charging connector types.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [CHADEMO](#CHADEMO)

CHAdeMO connector.

[GBT_DC](#GBT_DC)

Guobiao GB/T 20234.3 DC connector, commonly called "GB/T DC".

[IEC_62196_TYPE_1_COMBO](#IEC_62196_TYPE_1_COMBO)

Type 1 Combo connector, commonly called "CCS1".

[IEC_62196_TYPE_2_COMBO](#IEC_62196_TYPE_2_COMBO)

Type 2 Combo connector, commonly called "CCS2".

[SAE_J3400](#SAE_J3400)

SAE J3400 - North American Charging Standard (NACS) for Electric Vehicles

[TESLA](#TESLA)

Deprecated.
Will be removed in v4.28.0, use [`SAE_J3400`](#SAE_J3400) instead.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`ChargingConnectorType`](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### IEC_62196_TYPE_1_COMBO

public static final [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") IEC_62196_TYPE_1_COMBO

    Type 1 Combo connector, commonly called "CCS1".

### IEC_62196_TYPE_2_COMBO

public static final [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") IEC_62196_TYPE_2_COMBO

    Type 2 Combo connector, commonly called "CCS2".

### CHADEMO

public static final [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") CHADEMO

    CHAdeMO connector.

### TESLA

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public static final [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") TESLA

    Deprecated.
Will be removed in v4.28.0, use [`SAE_J3400`](#SAE_J3400) instead.

Tesla connector.

### GBT_DC

public static final [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") GBT_DC

    Guobiao GB/T 20234.3 DC connector, commonly called "GB/T DC".

### SAE_J3400

public static final [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") SAE_J3400

    SAE J3400 - North American Charging Standard (NACS) for Electric Vehicles

## Method Details

### values

public static [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [ChargingConnectorType](sdk-for-android-explore-api-reference-latestchargingconnectortype "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
