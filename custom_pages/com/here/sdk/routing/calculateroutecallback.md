---
title: "CalculateRouteCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcalculateroutecallback"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface CalculateRouteCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface CalculateRouteCallback
A function which is called by the RoutingEngine after route calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument is the calculated routes. It is `null` in case of an error.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onRouteCalculated](#onRouteCalculated(com.here.sdk.routing.RoutingError,java.util.List))`(`[`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")` routingError, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")`> routeList)`

A function which is called by the RoutingEngine after route calculation has completed.

## Method Details

### onRouteCalculated

void onRouteCalculated(@Nullable [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") routingError, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Route](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")\> routeList)

    A function which is called by the RoutingEngine after route calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument is the calculated routes. It is `null` in case of an error.
Parameters:
    `routingError` -

    The error in case of a failure. It is `null` for an operation that succeeds.

    `routeList` -

    The calculated routes. It is `null` in case of an error.
