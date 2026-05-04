---
title: "RoutePlace (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrouteplace"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RoutePlace

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RoutePlace
------------------------------------------------------------------------
public final class RoutePlace extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The location information.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [chargeInKilowattHours](#chargeInKilowattHours)

Estimated battery charge in kWh for electric vehicles when leaving this place.

[`ChargingStation`](sdk-for-android-explore-api-reference-latestchargingstation "class in com.here.sdk.routing")

  [chargingStation](#chargingStation)

Charging station data for electric vehicles.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [displayCoordinates](#displayCoordinates)

Location of the Points of Interest (PoI) to be displayed in the visualization.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [id](#id)

Identifier of a public transit place if available.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [mapMatchedCoordinates](#mapMatchedCoordinates)

Map-matched geographic coordinates.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [name](#name)

Name of a public transit place if available.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [originalCoordinates](#originalCoordinates)

User-defined geographic coordinates.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [platform](#platform)

Platform name or number of a public transit place if available.

[`SideOfDestination`](sdk-for-android-explore-api-reference-latestsideofdestination "enum class in com.here.sdk.routing")

  [sideOfDestination](#sideOfDestination)

Side of destination: left, right or undefined.

[`RoutePlaceType`](sdk-for-android-explore-api-reference-latestrouteplacetype "enum class in com.here.sdk.routing")

  [type](#type)

The type of the route place.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [waypointIndex](#waypointIndex)

If available, this index corresponds to the waypoint in the original user-defined waypoint list.

## Constructor Summary

Constructors

Constructor

  Description

  [RoutePlace](#%3Cinit%3E(com.here.sdk.routing.RoutePlaceType,com.here.sdk.core.GeoCoordinates))`(`[`RoutePlaceType`](sdk-for-android-explore-api-reference-latestrouteplacetype "enum class in com.here.sdk.routing")` type, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` mapMatchedCoordinates)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

  `boolean`

  [isOffRoad](#isOffRoad())`()`

Checks whether the [`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") is off-road or not.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### type

@NonNull public [RoutePlaceType](sdk-for-android-explore-api-reference-latestrouteplacetype "enum class in com.here.sdk.routing") type

    The type of the route place.

### waypointIndex

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) waypointIndex

    If available, this index corresponds to the waypoint in the original user-defined waypoint list. Otherwise, this waypoint was added during route calculation by the system.

### originalCoordinates

@Nullable public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") originalCoordinates

    User-defined geographic coordinates. If not available, it means this place was added during route calculation.

### mapMatchedCoordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") mapMatchedCoordinates

    Map-matched geographic coordinates.

### displayCoordinates

@Nullable public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") displayCoordinates

    Location of the Points of Interest (PoI) to be displayed in the visualization. In the map data, PoI have a set of display coordinates as well as a set of access/routing coordinates. While the access/routing coordinates specify the nearest accessible road network location that can be apart from actual location of the PoI, the display coordinates specify the location of the PoI to be displayed accurately in the visualization.

### chargeInKilowattHours

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) chargeInKilowattHours

    Estimated battery charge in kWh for electric vehicles when leaving this place. Available only if the route was calculated with [`ElectricVehicleOptions.ensureReachability`](sdk-for-android-explore-api-reference-latestelectricvehicleoptions#ensureReachability) = `true`.

### chargingStation

@Nullable public [ChargingStation](sdk-for-android-explore-api-reference-latestchargingstation "class in com.here.sdk.routing") chargingStation

    Charging station data for electric vehicles.

### name

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name

    Name of a public transit place if available.

### id

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) id

    Identifier of a public transit place if available.

### platform

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) platform

    Platform name or number of a public transit place if available.

### sideOfDestination

@Nullable public [SideOfDestination](sdk-for-android-explore-api-reference-latestsideofdestination "enum class in com.here.sdk.routing") sideOfDestination

    Side of destination: left, right or undefined. `null` for transit sections and for origin points. `UNDEFINED` if `originalCoordinates` are not identified or too close to the road.

## Constructor Details

  - (com.here.sdk.routing.RoutePlaceType,com.here.sdk.core.GeoCoordinates)" class="section detail">

### RoutePlace

public RoutePlace(@NonNull [RoutePlaceType](sdk-for-android-explore-api-reference-latestrouteplacetype "enum class in com.here.sdk.routing") type, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") mapMatchedCoordinates)

    Creates a new instance.
Parameters:
    `type` -

    The type of the route place.

    `mapMatchedCoordinates` -

    Map-matched geographic coordinates.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### isOffRoad

public boolean isOffRoad()

    Checks whether the [`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") is off-road or not.
Returns:
    `true` if the [`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") is off-road, `false` otherwise.
