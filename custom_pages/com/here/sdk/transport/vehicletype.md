---
title: "VehicleType (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestvehicletype"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class VehicleType

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")\>
com.here.sdk.transport.VehicleType
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`VehicleType`](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum VehicleType extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")\>
Defines the type of the vehicle.

**Note:** This is a beta release of this vehicle type, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BICYCLE](#BICYCLE)

Vehicle type is a bicycle.

[BUS](#BUS)

Vehicle type is a bus.

[CAR](#CAR)

Vehicle type is a car.

[MOTORCYCLE](#MOTORCYCLE)

Vehicle type is a motorcycle.

[PRIVATE_BUS](#PRIVATE_BUS)

Vehicle type is a private bus.

[SCOOTER](#SCOOTER)

Vehicle type is a scooter.

[TRUCK](#TRUCK)

Vehicle type is a truck.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`VehicleType`](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`VehicleType`](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### CAR

public static final [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") CAR

    Vehicle type is a car.

### TRUCK

public static final [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") TRUCK

    Vehicle type is a truck.

### BICYCLE

public static final [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") BICYCLE

    Vehicle type is a bicycle.

### BUS

public static final [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") BUS

    Vehicle type is a bus.

### MOTORCYCLE

public static final [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") MOTORCYCLE

    Vehicle type is a motorcycle.

### SCOOTER

public static final [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") SCOOTER

    Vehicle type is a scooter.

### PRIVATE_BUS

public static final [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") PRIVATE_BUS

    Vehicle type is a private bus.

## Method Details

### values

public static [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
