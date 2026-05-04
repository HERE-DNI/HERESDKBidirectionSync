---
title: "VehicleRestrictionMaxWeightType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class VehicleRestrictionMaxWeightType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.VehicleRestrictionMaxWeightType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`VehicleRestrictionMaxWeightType`](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum VehicleRestrictionMaxWeightType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")\>
This enum represents the specific type of the maximum permitted weight restriction. **NOTES:** A restriction of type [`UNKNOWN`](#UNKNOWN) may change to [`GROSS`](#GROSS), [`CURRENT`](#CURRENT) or [`EMPTY`](#EMPTY) when data becomes available in future. A restriction of type [`GROSS`](#GROSS), [`CURRENT`](#CURRENT) or [`EMPTY`](#EMPTY) may also change to a different type if actual regulation changes.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [CURRENT](#CURRENT)

Restriction is for current weight.

[EMPTY](#EMPTY)

Restriction is for empty weight.

[GROSS](#GROSS)

Restriction is for gross weight.

[UNKNOWN](#UNKNOWN)

Restriction may apply to gross or current weight.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`VehicleRestrictionMaxWeightType`](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`VehicleRestrictionMaxWeightType`](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### UNKNOWN

public static final [VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing") UNKNOWN

    Restriction may apply to gross or current weight.

### GROSS

public static final [VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing") GROSS

    Restriction is for gross weight.

### CURRENT

public static final [VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing") CURRENT

    Restriction is for current weight.

### EMPTY

public static final [VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing") EMPTY

    Restriction is for empty weight.

## Method Details

### values

public static [VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [VehicleRestrictionMaxWeightType](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweighttype "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
