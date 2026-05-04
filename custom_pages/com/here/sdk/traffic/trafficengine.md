---
title: "TrafficEngine (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficengine"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.traffic.TrafficEngine
------------------------------------------------------------------------
public final class TrafficEngine extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Use the TrafficEngine to get information about current traffic flow and incidents in an area specified by [`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core"), [`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core"), or [`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core"). Provides optional parameters given in [`TrafficIncidentsQueryOptions`](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic") and [`TrafficFlowQueryOptions`](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic") to filter the result.

By default, incidents are localized based on their geographical location. You can override that behavior by specifying the desired language that should be used for the incidents description and summary.

The resulting traffic data contains information on incident types such as congestion, construction for road works, road hazard, road closure, weather updates for road condition, lane restriction and others.

Traffic data is fetched online to get the most precise and freshest data available. In offline mode, live traffic data can be fetched using the traffic pass-through features. See [`SDKNativeEngine.getPassThroughFeatures()`](sdk-for-android-explore-api-reference-latestsdknativeengine#getPassThroughFeatures())

## Constructor Summary

Constructors

Constructor

  Description

  [TrafficEngine](#%3Cinit%3E())`()`

Creates a new instance of this class.

[TrafficEngine](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkEngine)`

Creates a new instance of this class.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [lookupIncident](#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` originalId, `[`TrafficIncidentLookupOptions`](sdk-for-android-explore-api-reference-latesttrafficincidentlookupoptions "class in com.here.sdk.traffic")` lookupOptions, `[`TrafficIncidentLookupCallback`](sdk-for-android-explore-api-reference-latesttrafficincidentlookupcallback "interface in com.here.sdk.traffic")` callback)`

Asynchronously queries for traffic incident by the original id.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [queryForFlow](#queryForFlow(com.here.sdk.core.GeoBox,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` boxArea, `[`TrafficFlowQueryOptions`](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic")` queryOptions, `[`TrafficFlowQueryCallback`](sdk-for-android-explore-api-reference-latesttrafficflowquerycallback "interface in com.here.sdk.traffic")` callback)`

Asynchronously queries for traffic flow using a bounding box as a filter.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [queryForFlow](#queryForFlow(com.here.sdk.core.GeoCircle,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback))`(`[`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")` circleArea, `[`TrafficFlowQueryOptions`](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic")` queryOptions, `[`TrafficFlowQueryCallback`](sdk-for-android-explore-api-reference-latesttrafficflowquerycallback "interface in com.here.sdk.traffic")` callback)`

Asynchronously queries for traffic flow using a circle as a filter.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [queryForFlow](#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback))`(`[`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")` corridorArea, `[`TrafficFlowQueryOptions`](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic")` queryOptions, `[`TrafficFlowQueryCallback`](sdk-for-android-explore-api-reference-latesttrafficflowquerycallback "interface in com.here.sdk.traffic")` callback)`

Asynchronously queries for traffic flow by a corridor as a filter.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [queryForIncidents](#queryForIncidents(com.here.sdk.core.GeoBox,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` boxArea, `[`TrafficIncidentsQueryOptions`](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic")` queryOptions, `[`TrafficIncidentsQueryCallback`](sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback "interface in com.here.sdk.traffic")` callback)`

Asynchronously queries for traffic incidents using a bounding box as a filter.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [queryForIncidents](#queryForIncidents(com.here.sdk.core.GeoCircle,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback))`(`[`GeoCircle`](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core")` circleArea, `[`TrafficIncidentsQueryOptions`](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic")` queryOptions, `[`TrafficIncidentsQueryCallback`](sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback "interface in com.here.sdk.traffic")` callback)`

Asynchronously queries for traffic incidents using a circle as a filter.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [queryForIncidents](#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback))`(`[`GeoCorridor`](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core")` corridorArea, `[`TrafficIncidentsQueryOptions`](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic")` queryOptions, `[`TrafficIncidentsQueryCallback`](sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback "interface in com.here.sdk.traffic")` callback)`

Asynchronously queries for traffic incidents by a corridor as a filter.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### TrafficEngine

public TrafficEngine() throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of this class.
Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.core.engine.SDKNativeEngine)" class="section detail">

### TrafficEngine

public TrafficEngine(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkEngine) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of this class.
Parameters:
    `sdkEngine` -

    An SDKEngine instance.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

## Method Details

### queryForIncidents

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") queryForIncidents(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") boxArea, @NonNull [TrafficIncidentsQueryOptions](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic") queryOptions, @NonNull [TrafficIncidentsQueryCallback](sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback "interface in com.here.sdk.traffic") callback)

    Asynchronously queries for traffic incidents using a bounding box as a filter.
Parameters:
    `boxArea` -

    The bounding box area to search for traffic incidents. The maximum width and height for a bounding box filter is 1 degree.

    `queryOptions` -

    The options which are specific for incidents query.

    `callback` -

    It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### queryForIncidents

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") queryForIncidents(@NonNull [GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") circleArea, @NonNull [TrafficIncidentsQueryOptions](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic") queryOptions, @NonNull [TrafficIncidentsQueryCallback](sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback "interface in com.here.sdk.traffic") callback)

    Asynchronously queries for traffic incidents using a circle as a filter.
Parameters:
    `circleArea` -

    The circle area to search for traffic incidents. The maximum radius of the circle filter is 50000 meters.

    `queryOptions` -

    The options which are specific for incidents query.

    `callback` -

    It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### queryForIncidents

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") queryForIncidents(@NonNull [GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core") corridorArea, @NonNull [TrafficIncidentsQueryOptions](sdk-for-android-explore-api-reference-latesttrafficincidentsqueryoptions "class in com.here.sdk.traffic") queryOptions, @NonNull [TrafficIncidentsQueryCallback](sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback "interface in com.here.sdk.traffic") callback)

    Asynchronously queries for traffic incidents by a corridor as a filter.
Parameters:
    `corridorArea` -

    The corridor box to search for traffic incidents. The maximum length for the corridor is 500000 meters and the maximum `GeoCorridor.half_width_in_meters` is 5000 meters. If the number of points in corridor is greater than 300 then request is split into smaller ones and results are aggregated into single response, this will result in multiple requests to the backend. This process does not change a shape of the corridor.

    To reduce number of points in the corridor use [`PolylineSimplifier`](sdk-for-android-explore-api-reference-latestpolylinesimplifier "class in com.here.sdk.core").

    If no `GeoCorridor.half_width_in_meters` is specified, the default value is used. The default value is 30 meters.

    `queryOptions` -

    The options which are specific for incidents query.

    `callback` -

    It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### lookupIncident

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") lookupIncident(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) originalId, @NonNull [TrafficIncidentLookupOptions](sdk-for-android-explore-api-reference-latesttrafficincidentlookupoptions "class in com.here.sdk.traffic") lookupOptions, @NonNull [TrafficIncidentLookupCallback](sdk-for-android-explore-api-reference-latesttrafficincidentlookupcallback "interface in com.here.sdk.traffic") callback)

    Asynchronously queries for traffic incident by the original id. See [`TrafficIncident.getOriginalId()`](sdk-for-android-explore-api-reference-latesttrafficincident#getOriginalId()) for more information.
Parameters:
    `originalId` -

    The requested incident original id.

    `lookupOptions` -

    The options which are specific for the incident lookup query.

    `callback` -

    The callback object that will be invoked after the incident lookup query. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### queryForFlow

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") queryForFlow(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") boxArea, @NonNull [TrafficFlowQueryOptions](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic") queryOptions, @NonNull [TrafficFlowQueryCallback](sdk-for-android-explore-api-reference-latesttrafficflowquerycallback "interface in com.here.sdk.traffic") callback)

    Asynchronously queries for traffic flow using a bounding box as a filter.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `boxArea` -

    The bounding box area to search for traffic flow.

    `queryOptions` -

    The options which are specific for flow query.

    `callback` -

    It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### queryForFlow

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") queryForFlow(@NonNull [GeoCircle](sdk-for-android-explore-api-reference-latestgeocircle "class in com.here.sdk.core") circleArea, @NonNull [TrafficFlowQueryOptions](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic") queryOptions, @NonNull [TrafficFlowQueryCallback](sdk-for-android-explore-api-reference-latesttrafficflowquerycallback "interface in com.here.sdk.traffic") callback)

    Asynchronously queries for traffic flow using a circle as a filter.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `circleArea` -

    The circle area to search for traffic flow. The maximum radius of the circle filter is 50000 meters.

    `queryOptions` -

    The options which are specific for flow query.

    `callback` -

    It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### queryForFlow

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") queryForFlow(@NonNull [GeoCorridor](sdk-for-android-explore-api-reference-latestgeocorridor "class in com.here.sdk.core") corridorArea, @NonNull [TrafficFlowQueryOptions](sdk-for-android-explore-api-reference-latesttrafficflowqueryoptions "class in com.here.sdk.traffic") queryOptions, @NonNull [TrafficFlowQueryCallback](sdk-for-android-explore-api-reference-latesttrafficflowquerycallback "interface in com.here.sdk.traffic") callback)

    Asynchronously queries for traffic flow by a corridor as a filter.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `corridorArea` -

    The corridor box to search for traffic flow. The maximum length for the corridor is 500000 meters and the maximum `GeoCorridor.half_width_in_meters` is 5000 meters.

    Maximum number of points in the corridor is 300.

    To reduce number of points in the corridor use [`PolylineSimplifier`](sdk-for-android-explore-api-reference-latestpolylinesimplifier "class in com.here.sdk.core").

    If no `GeoCorridor.half_width_in_meters` is specified, the default value is used. The default value is 30 meters.

    `queryOptions` -

    The options which are specific for flow query.

    `callback` -

    It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.
