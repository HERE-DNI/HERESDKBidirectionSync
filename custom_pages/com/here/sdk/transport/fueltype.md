---
title: "FuelType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestfueltype"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class FuelType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")\>
com.here.sdk.transport.FuelType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`FuelType`](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum FuelType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")\>
Defines possible fuel types provided by a fuel station.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BIO_DIESEL](#BIO_DIESEL)

Bio-Diesel fuel type.

[CNG](#CNG)

Compressed natural gas fuel type.

[DIESEL](#DIESEL)

Diesel fuel type.

[DIESEL_WITH_ADDITIVES](#DIESEL_WITH_ADDITIVES)

Diesel with additives fuel type.

[E10](#E10)

10% Ethanol and 90% Gasoline fuel type.

[E20](#E20)

20% Ethanol and 80% Gasoline fuel type.

[E85](#E85)

85% Ethanol and 15% Gasoline fuel type.

[ETHANOL](#ETHANOL)

Ethanol fuel type.

[ETHANOL_WITH_ADDITIVES](#ETHANOL_WITH_ADDITIVES)

Ethanol with additives fuel type.

[GASOHOL_91](#GASOHOL_91)

Gasohol 91 fuel type.

[GASOHOL_95](#GASOHOL_95)

Gasohol 95 fuel type.

[GASOLINE](#GASOLINE)

Gasoline fuel type.

[HVO](#HVO)

Hydrotreated vegetable oil fuel type.

[HYDROGEN](#HYDROGEN)

Hydrogen fuel type.

[LNG](#LNG)

Liquefied natural gas fuel type.

[LPG](#LPG)

Liquified petroleum gas fuel type.

[MIDGRADE](#MIDGRADE)

Midgrade fuel type.

[OCTANE_100](#OCTANE_100)

Octane 100 fuel type.

[OCTANE_87](#OCTANE_87)

Octane 87 fuel type.

[OCTANE_89](#OCTANE_89)

Octane 89 fuel type.

[OCTANE_90](#OCTANE_90)

Octane 90 fuel type.

[OCTANE_91](#OCTANE_91)

Octane 91 fuel type.

[OCTANE_92](#OCTANE_92)

Octane 92 fuel type.

[OCTANE_93](#OCTANE_93)

Octane 93 fuel type.

[OCTANE_95](#OCTANE_95)

Octane 95 fuel type.

[OCTANE_98](#OCTANE_98)

Octane 98 fuel type.

[PREMIUM](#PREMIUM)

Premium fuel type.

[PREMIUM_WITH_ADDITIVES](#PREMIUM_WITH_ADDITIVES)

Premium with additives fuel type.

[REGULAR](#REGULAR)

Regular fuel type.

[REGULAR_WITH_ADDITIVES](#REGULAR_WITH_ADDITIVES)

Regular with additives fuel type.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`FuelType`](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`FuelType`](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### DIESEL

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") DIESEL

    Diesel fuel type.

### LPG

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") LPG

    Liquified petroleum gas fuel type.

### BIO_DIESEL

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") BIO_DIESEL

    Bio-Diesel fuel type.

### CNG

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") CNG

    Compressed natural gas fuel type.

### DIESEL_WITH_ADDITIVES

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") DIESEL_WITH_ADDITIVES

    Diesel with additives fuel type.

### E10

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") E10

    10% Ethanol and 90% Gasoline fuel type.

### E20

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") E20

    20% Ethanol and 80% Gasoline fuel type.

### E85

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") E85

    85% Ethanol and 15% Gasoline fuel type.

### ETHANOL

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") ETHANOL

    Ethanol fuel type.

### ETHANOL_WITH_ADDITIVES

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") ETHANOL_WITH_ADDITIVES

    Ethanol with additives fuel type.

### GASOLINE

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") GASOLINE

    Gasoline fuel type.

### GASOHOL_91

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") GASOHOL_91

    Gasohol 91 fuel type.

### GASOHOL_95

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") GASOHOL_95

    Gasohol 95 fuel type.

### HVO

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") HVO

    Hydrotreated vegetable oil fuel type.

### HYDROGEN

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") HYDROGEN

    Hydrogen fuel type.

### LNG

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") LNG

    Liquefied natural gas fuel type.

### MIDGRADE

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") MIDGRADE

    Midgrade fuel type.

### PREMIUM

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") PREMIUM

    Premium fuel type.

### PREMIUM_WITH_ADDITIVES

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") PREMIUM_WITH_ADDITIVES

    Premium with additives fuel type.

### REGULAR

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") REGULAR

    Regular fuel type.

### REGULAR_WITH_ADDITIVES

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") REGULAR_WITH_ADDITIVES

    Regular with additives fuel type.

### OCTANE_87

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_87

    Octane 87 fuel type.

### OCTANE_89

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_89

    Octane 89 fuel type.

### OCTANE_90

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_90

    Octane 90 fuel type.

### OCTANE_91

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_91

    Octane 91 fuel type.

### OCTANE_92

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_92

    Octane 92 fuel type.

### OCTANE_93

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_93

    Octane 93 fuel type.

### OCTANE_95

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_95

    Octane 95 fuel type.

### OCTANE_98

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_98

    Octane 98 fuel type.

### OCTANE_100

public static final [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") OCTANE_100

    Octane 100 fuel type.

## Method Details

### values

public static [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [FuelType](sdk-for-android-explore-api-reference-latestfueltype "enum class in com.here.sdk.transport") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
