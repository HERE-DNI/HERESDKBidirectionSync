---
title: "TrafficIncidentsQueryCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficincidentsquerycallback"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TrafficIncidentsQueryCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface TrafficIncidentsQueryCallback
Callback passed to [`TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)). The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `null` for an operation that succeeds. The second argument is the list of incidents in the case of the success. It is `null` in case of an error.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTrafficIncidentsFetched](#onTrafficIncidentsFetched(com.here.sdk.traffic.TrafficQueryError,java.util.List))`(`[`TrafficQueryError`](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")` queryError, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficIncident`](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic")`> result)`

Callback passed to [`TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)).

## Method Details

### onTrafficIncidentsFetched

void onTrafficIncidentsFetched(@Nullable [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") queryError, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficIncident](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic")\> result)

    Callback passed to [`TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)). The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `null` for an operation that succeeds. The second argument is the list of incidents in the case of the success. It is `null` in case of an error.
Parameters:
    `queryError` -

    The error in the case of the failure. It is `null` for an operation that succeeds.

    `result` -

    The list of incidents in the case of the success. It is `null` in case of an error.
