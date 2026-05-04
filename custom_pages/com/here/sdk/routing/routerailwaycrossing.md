---
title: "RouteRailwayCrossing (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrouterailwaycrossing"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RouteRailwayCrossing

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RouteRailwayCrossing
------------------------------------------------------------------------
public final class RouteRailwayCrossing extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains information about railway crossing.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [coordinates](#coordinates)

Location on the route

[`RouteOffset`](sdk-for-android-explore-api-reference-latestrouteoffset "class in com.here.sdk.routing")

  [routeOffset](#routeOffset)

Route position

[`RouteRailwayCrossingType`](sdk-for-android-explore-api-reference-latestrouterailwaycrossingtype "enum class in com.here.sdk.routing")

  [type](#type)

The type of the route place.

## Constructor Summary

Constructors

Constructor

  Description

  [RouteRailwayCrossing](#%3Cinit%3E(com.here.sdk.routing.RouteRailwayCrossingType,com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.RouteOffset))`(`[`RouteRailwayCrossingType`](sdk-for-android-explore-api-reference-latestrouterailwaycrossingtype "enum class in com.here.sdk.routing")` type, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates, `[`RouteOffset`](sdk-for-android-explore-api-reference-latestrouteoffset "class in com.here.sdk.routing")` routeOffset)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### type

@NonNull public [RouteRailwayCrossingType](sdk-for-android-explore-api-reference-latestrouterailwaycrossingtype "enum class in com.here.sdk.routing") type

    The type of the route place.

### coordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates

    Location on the route

### routeOffset

@NonNull public [RouteOffset](sdk-for-android-explore-api-reference-latestrouteoffset "class in com.here.sdk.routing") routeOffset

    Route position

## Constructor Details

  - (com.here.sdk.routing.RouteRailwayCrossingType,com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.RouteOffset)" class="section detail">

### RouteRailwayCrossing

public RouteRailwayCrossing(@NonNull [RouteRailwayCrossingType](sdk-for-android-explore-api-reference-latestrouterailwaycrossingtype "enum class in com.here.sdk.routing") type, @NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [RouteOffset](sdk-for-android-explore-api-reference-latestrouteoffset "class in com.here.sdk.routing") routeOffset)

    Creates a new instance.
Parameters:
    `type` -

    The type of the route place.

    `coordinates` -

    Location on the route

    `routeOffset` -

    Route position
