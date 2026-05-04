---
title: "CalculateTrafficOnRouteCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcalculatetrafficonroutecallback"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface CalculateTrafficOnRouteCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface CalculateTrafficOnRouteCallback
A function which is called by the RoutingEngine after route traffic calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument is the calculated route traffic. It is `null` in case of an error.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onTrafficOnRouteCalculated](#onTrafficOnRouteCalculated(com.here.sdk.routing.RoutingError,com.here.sdk.routing.TrafficOnRoute))`(`[`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")` routingError, `[`TrafficOnRoute`](sdk-for-android-explore-api-reference-latesttrafficonroute "class in com.here.sdk.routing")` trafficOnRoute)`

A function which is called by the RoutingEngine after route traffic calculation has completed.

## Method Details

### onTrafficOnRouteCalculated

void onTrafficOnRouteCalculated(@Nullable [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") routingError, @Nullable [TrafficOnRoute](sdk-for-android-explore-api-reference-latesttrafficonroute "class in com.here.sdk.routing") trafficOnRoute)

    A function which is called by the RoutingEngine after route traffic calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument is the calculated route traffic. It is `null` in case of an error.
Parameters:
    `routingError` -

    The error in case of a failure. It is `null` for an operation that succeeds.

    `trafficOnRoute` -

    The calculated route traffic. It is `null` in case of an error.
