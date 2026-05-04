---
title: "TrafficFlowQueryCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficflowquerycallback"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TrafficFlowQueryCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface TrafficFlowQueryCallback
Callback passed to following functions: [`TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `null` for an operation that succeeds. The second argument is the list of flow items in the case of the success. It is `null` in case of an error.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTrafficFlowFetched](#onTrafficFlowFetched(com.here.sdk.traffic.TrafficQueryError,java.util.List))`(`[`TrafficQueryError`](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")` queryError, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficFlow`](sdk-for-android-explore-api-reference-latesttrafficflow "class in com.here.sdk.traffic")`> result)`

Callback passed to following functions: [`TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) The method will be called on the main thread when a search call has been completed.

## Method Details

### onTrafficFlowFetched

void onTrafficFlowFetched(@Nullable [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") queryError, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficFlow](sdk-for-android-explore-api-reference-latesttrafficflow "class in com.here.sdk.traffic")\> result)

    Callback passed to following functions: [`TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) [`TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)) The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `null` for an operation that succeeds. The second argument is the list of flow items in the case of the success. It is `null` in case of an error.
Parameters:
    `queryError` -

    The error in the case of the failure. It is `null` for an operation that succeeds.

    `result` -

    The list of incidents in the case of the success. It is `null` in case of an error.

    Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
