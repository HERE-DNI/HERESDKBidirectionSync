---
title: "TrafficIncidentLookupCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficincidentlookupcallback"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface TrafficIncidentLookupCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface TrafficIncidentLookupCallback
Callback passed to [`TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)). The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `null` for an operation that succeeds. The second argument is the incident in the case of the success. It is `null` in case of an error.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTrafficIncidentFetched](#onTrafficIncidentFetched(com.here.sdk.traffic.TrafficQueryError,com.here.sdk.traffic.TrafficIncident))`(`[`TrafficQueryError`](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic")` queryError, `[`TrafficIncident`](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic")` result)`

Callback passed to [`TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)).

## Method Details

### onTrafficIncidentFetched

void onTrafficIncidentFetched(@Nullable [TrafficQueryError](sdk-for-android-explore-api-reference-latesttrafficqueryerror "enum class in com.here.sdk.traffic") queryError, @Nullable [TrafficIncident](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic") result)

    Callback passed to [`TrafficEngine.lookupIncident(java.lang.String, com.here.sdk.traffic.TrafficIncidentLookupOptions, com.here.sdk.traffic.TrafficIncidentLookupCallback)`](sdk-for-android-explore-api-reference-latesttrafficengine#lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)). The method will be called on the main thread when a search call has been completed. The first argument is the error in the case of the failure. It is `null` for an operation that succeeds. The second argument is the incident in the case of the success. It is `null` in case of an error.
Parameters:
    `queryError` -

    The error in the case of the failure. It is `null` for an operation that succeeds.

    `result` -

    The incident in the case of the success. It is `null` in case of an error.
