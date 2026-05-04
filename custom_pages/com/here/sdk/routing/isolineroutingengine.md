---
title: "IsolineRoutingEngine (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestisolineroutingengine"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class IsolineRoutingEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.IsolineRoutingEngine
------------------------------------------------------------------------
public final class IsolineRoutingEngine extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Use the IsolineRoutingEngine to calculate a reachable area from a center point. The calculation is done asynchronously and requires an online connection.

## Constructor Summary

Constructors

Constructor

  Description

  [IsolineRoutingEngine](#%3Cinit%3E())`()`

Creates a new instance of this class.

[IsolineRoutingEngine](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkEngine)`

Creates a new instance of IsolineRoutingEngine.

[IsolineRoutingEngine](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkEngine, `[`RoutingConnectionSettings`](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing")` connectionSettings)`

Creates a new instance of RoutingEngine.

[IsolineRoutingEngine](#%3Cinit%3E(com.here.sdk.routing.RoutingConnectionSettings))`(`[`RoutingConnectionSettings`](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing")` connectionSettings)`

Creates a new instance of RoutingEngine.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateIsoline](#calculateIsoline(com.here.sdk.routing.Waypoint,com.here.sdk.routing.IsolineOptions,com.here.sdk.routing.CalculateIsolineCallback))`(`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")` center, `[`IsolineOptions`](sdk-for-android-explore-api-reference-latestisolineoptions "class in com.here.sdk.routing")` isolineOptions, `[`CalculateIsolineCallback`](sdk-for-android-explore-api-reference-latestcalculateisolinecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously calculates isolines to indicate the reachable area from a center point.

[`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")

  [setCustomOption](#setCustomOption(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` value)`

Sets a custom option for routing backend queries.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### IsolineRoutingEngine

public IsolineRoutingEngine() throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of this class.
Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.routing.RoutingConnectionSettings)" class="section detail">

### IsolineRoutingEngine

public IsolineRoutingEngine(@NonNull [RoutingConnectionSettings](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing") connectionSettings) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of RoutingEngine.
Parameters:
    `connectionSettings` -

    Settings for the route calculation.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings)" class="section detail">

### IsolineRoutingEngine

public IsolineRoutingEngine(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkEngine, @NonNull [RoutingConnectionSettings](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing") connectionSettings) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of RoutingEngine.
Parameters:
    `sdkEngine` -

    An SDKEngine instance.

    `connectionSettings` -

    Settings for the route calculation.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.core.engine.SDKNativeEngine)" class="section detail">

### IsolineRoutingEngine

public IsolineRoutingEngine(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkEngine) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of IsolineRoutingEngine.
Parameters:
    `sdkEngine` -

    An SDKEngine instance.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

## Method Details

### calculateIsoline

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateIsoline(@NonNull [Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") center, @NonNull [IsolineOptions](sdk-for-android-explore-api-reference-latestisolineoptions "class in com.here.sdk.routing") isolineOptions, @NonNull [CalculateIsolineCallback](sdk-for-android-explore-api-reference-latestcalculateisolinecallback "interface in com.here.sdk.routing") callback)

    Asynchronously calculates isolines to indicate the reachable area from a center point. This finds all destinations that can be reached in a specific amount of time, a maximum travel distance, or even the charge level available in an electric vehicle. The result is a polygon area where each point is reachable within the provided limit.
Parameters:
    `center` -

    Center point from which isolines are calculated. At minimum, the waypoint must contain the coordinates as point of origin.

    `isolineOptions` -

    Options for isoline calculation.

    `callback` -

    Callback object that will be invoked after isoline calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### setCustomOption

@Nullable public [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") setCustomOption(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)

    Sets a custom option for routing backend queries. The custom option is applied to all the queries that `IsolineRoutingEngine` performs. For a complete list of available parameter names and their valid values, refer to [HERE Routing API v8](https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html). **Note:** It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.
Parameters:
    `name` -

    An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string. The option name should't duplicate option names that SDK creates by itself for usage in the query, otherwise the query will callback with the error `RoutingError.INTERNAL_ERROR`.

    `value` -

    An option value. If the value is `null`, the option will be removed. The option value must be a non-empty string.

    Returns:
    An optional error of setting the option. It's `null` if the option has been set successfully. It's `RoutingError.INVALID_PARAMETER` if the input name and/or value haven't passed internal validation.
