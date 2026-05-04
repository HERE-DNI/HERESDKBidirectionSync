---
title: "TransitRoutingEngine (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransitroutingengine"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransitRoutingEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.TransitRoutingEngine
------------------------------------------------------------------------
public final class TransitRoutingEngine extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Use the TransitRoutingEngine to calculate a public transit route from A to B with a number of waypoints in between. Route calculation is done asynchronously and requires an online connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data.

**Note**: Clients need to explicitly call [`dispose()`](#dispose()) in order to prevent a possible, though unlikely, deadlock on destruction.

## Constructor Summary

Constructors

Constructor

  Description

  [TransitRoutingEngine](#%3Cinit%3E())`()`

Creates a new instance of this class.

[TransitRoutingEngine](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkEngine)`

Creates a new instance of TransitRoutingEngine.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(com.here.sdk.routing.TransitWaypoint,com.here.sdk.routing.TransitWaypoint,com.here.sdk.routing.TransitRouteOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[`TransitWaypoint`](sdk-for-android-explore-api-reference-latesttransitwaypoint "class in com.here.sdk.routing")` startingPoint, `[`TransitWaypoint`](sdk-for-android-explore-api-reference-latesttransitwaypoint "class in com.here.sdk.routing")` destination, `[`TransitRouteOptions`](sdk-for-android-explore-api-reference-latesttransitrouteoptions "class in com.here.sdk.routing")` routeOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously calculates a public transit route from the origin to the destination.

`void`

  [dispose](#dispose())`()`

Cancels pending requests and closes the background worker thread.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### TransitRoutingEngine

public TransitRoutingEngine() throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of this class.
Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.core.engine.SDKNativeEngine)" class="section detail">

### TransitRoutingEngine

public TransitRoutingEngine(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkEngine) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of TransitRoutingEngine.
Parameters:
    `sdkEngine` -

    An SDKEngine instance.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

## Method Details

### calculateRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [TransitWaypoint](sdk-for-android-explore-api-reference-latesttransitwaypoint "class in com.here.sdk.routing") startingPoint, @NonNull [TransitWaypoint](sdk-for-android-explore-api-reference-latesttransitwaypoint "class in com.here.sdk.routing") destination, @NonNull [TransitRouteOptions](sdk-for-android-explore-api-reference-latesttransitrouteoptions "class in com.here.sdk.routing") routeOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously calculates a public transit route from the origin to the destination.
Parameters:
    `startingPoint` -

    Position of starting point.

    `destination` -

    Position of destination.

    `routeOptions` -

    Options for public transit route calculation.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### dispose

public void dispose()

    Cancels pending requests and closes the background worker thread. **Note:** This method should be called from main thread.
