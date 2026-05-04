---
title: "CalculateIsolineCallback (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcalculateisolinecallback"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface CalculateIsolineCallback

Functional Interface:
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

------------------------------------------------------------------------
[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html) public interface CalculateIsolineCallback
A function which is called by the RoutingEngine after isoline calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument holds a list of calculated isolines. The list is `null` in case of an error. The size of the list matches the size of the provided sdk.routing.IsolineOptions.range_values: For each range limit, one isoline is calculated.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  `void`

  [onIsolineCalculated](#onIsolineCalculated(com.here.sdk.routing.RoutingError,java.util.List))`(`[`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")` routingError, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Isoline`](sdk-for-android-explore-api-reference-latestisoline "class in com.here.sdk.routing")`> isolines)`

A function which is called by the RoutingEngine after isoline calculation has completed.

## Method Details

### onIsolineCalculated

void onIsolineCalculated(@Nullable [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") routingError, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Isoline](sdk-for-android-explore-api-reference-latestisoline "class in com.here.sdk.routing")\> isolines)

    A function which is called by the RoutingEngine after isoline calculation has completed. It is always called on the main thread. The first argument is the error in case of a failure. It is `null` for an operation that succeeds. The second argument holds a list of calculated isolines. The list is `null` in case of an error. The size of the list matches the size of the provided sdk.routing.IsolineOptions.range_values: For each range limit, one isoline is calculated.
Parameters:
    `routingError` -

    The error in case of a failure. It is `null` for an operation that succeeds.

    `isolines` -

    Holds a list of calculated isolines. The list is `null` in case of an error.
