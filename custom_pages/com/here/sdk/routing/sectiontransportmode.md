---
title: "SectionTransportMode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsectiontransportmode"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class SectionTransportMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.SectionTransportMode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`SectionTransportMode`](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum SectionTransportMode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing")\>
Specifies the [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") mode of transport. A [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") may have a different transport mode than the one specified for route calculation. For example, a car route may have a section having ferry transport mode.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BICYCLE](#BICYCLE)

Bicycle mode of transport.

[BUS](#BUS)

Bus mode of transport.

[CAR](#CAR)

Car mode of transport.

[CAR_SHUTTLE_TRAIN](#CAR_SHUTTLE_TRAIN)

Mode of transport representing a shuttle train for cars.

[FERRY](#FERRY)

Ferry mode of transport.

[PEDESTRIAN](#PEDESTRIAN)

Pedestrian mode of transport.

[PRIVATE_BUS](#PRIVATE_BUS)

Private bus mode of transport.

[PUBLIC_TRANSIT](#PUBLIC_TRANSIT)

A section with this mode is part of a public transit route.

[SCOOTER](#SCOOTER)

Scooter mode of transport.

[TAXI](#TAXI)

Taxi mode of transport.

[TRUCK](#TRUCK)

Truck mode of transport.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`SectionTransportMode`](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`SectionTransportMode`](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### CAR

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") CAR

    Car mode of transport.

### TRUCK

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") TRUCK

    Truck mode of transport.

### PEDESTRIAN

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") PEDESTRIAN

    Pedestrian mode of transport.

### FERRY

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") FERRY

    Ferry mode of transport.

### CAR_SHUTTLE_TRAIN

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") CAR_SHUTTLE_TRAIN

    Mode of transport representing a shuttle train for cars.

### SCOOTER

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") SCOOTER

    Scooter mode of transport.

### BICYCLE

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") BICYCLE

    Bicycle mode of transport.

### PUBLIC_TRANSIT

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") PUBLIC_TRANSIT

    A section with this mode is part of a public transit route. The actual transport mode can be obtained from [`Section.getTransitDetails()`](sdk-for-android-explore-api-reference-latestsection#getTransitDetails()).

### TAXI

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") TAXI

    Taxi mode of transport.

### BUS

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") BUS

    Bus mode of transport. Denotes those vehicles operated by public transport provider. This transport mode has the access to the bus-only lane/road.

### PRIVATE_BUS

public static final [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") PRIVATE_BUS

    Private bus mode of transport. Denotes those vehicles operated by private transport company. This transport mode does not have the access to the bus-only lane/road.

## Method Details

### values

public static [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
