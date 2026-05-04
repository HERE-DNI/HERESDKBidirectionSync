---
title: "TransportMode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransportmode"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class TransportMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")\>
com.here.sdk.transport.TransportMode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`TransportMode`](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum TransportMode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")\>
Specifies the mode of transport used for route calculalation.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [BICYCLE](#BICYCLE)

Route calculation for bicycles.

[BUS](#BUS)

Route calculation for buses.

[CAR](#CAR)

The calculated route is optimized for cars.

[PEDESTRIAN](#PEDESTRIAN)

The calculated route is optimized for pedestrians.

[PRIVATE_BUS](#PRIVATE_BUS)

Route calculation for private buses.

[PUBLIC_TRANSIT](#PUBLIC_TRANSIT)

The calculated route is optimized for public transit.

[SCOOTER](#SCOOTER)

The calculated route is optimized for scooters.

[TAXI](#TAXI)

The taxi transport mode takes into account tax restricted streets as well as streets reserved for exclusive taxi access.

[TRUCK](#TRUCK)

The calculated route is optimized for trucks.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`TransportMode`](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`TransportMode`](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### CAR

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") CAR

    The calculated route is optimized for cars.

### TRUCK

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") TRUCK

    The calculated route is optimized for trucks. This mode considers truck restrictions and uses truck specific speed assumptions when calculating the route.

### PEDESTRIAN

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") PEDESTRIAN

    The calculated route is optimized for pedestrians. As one effect, maneuvers will be optimized for walking, i.e. segments will consider actions relevant for pedestrians and maneuver instructions will contain texts suitable for a walking person. This mode disregards any traffic information.

### SCOOTER

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") SCOOTER

    The calculated route is optimized for scooters.

### BICYCLE

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") BICYCLE

    Route calculation for bicycles.

### PUBLIC_TRANSIT

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") PUBLIC_TRANSIT

    The calculated route is optimized for public transit. Note that this transport mode is available only for some versions of the HERE SDK. Check `SDKBuildInformation` and consult your HERE representative if necessary.

### TAXI

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") TAXI

    The taxi transport mode takes into account tax restricted streets as well as streets reserved for exclusive taxi access. Note that roads that are restricted or reserved for taxis are avoided, unless a waypoint is set on such a road - as this may indicate to pick-up or to drop-off a passenger.

    **Note:** This is a beta release of this transport mode, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

### BUS

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") BUS

    Route calculation for buses. Denotes those vehicles operated by public transport provider. This transport mode has the access to the bus-only lane/road.

### PRIVATE_BUS

public static final [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") PRIVATE_BUS

    Route calculation for private buses. Denotes those vehicles operated by private transport company. This transport mode does not have the access to the bus-only lane/road.

## Method Details

### values

public static [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
