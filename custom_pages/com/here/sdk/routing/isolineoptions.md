---
title: "IsolineOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestisolineoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class IsolineOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.IsolineOptions
------------------------------------------------------------------------
public final class IsolineOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Specifies options for isolines calculation.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [IsolineOptions.Calculation](sdk-for-android-explore-api-reference-latestisolineoptions-calculation)

Specifies isoline parameters.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`IsolineOptions.Calculation`](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing")

  [calculationOptions](#calculationOptions)

Specifies isoline parameters.

[`CarOptions`](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing")

  [carOptions](#carOptions)

Deprecated.
Will be removed in v4.28.0.

  [`EVCarOptions`](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing")

  [evCarOptions](#evCarOptions)

Deprecated.
Will be removed in v4.28.0.

  [`EVTruckOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing")

  [evTruckOptions](#evTruckOptions)

Deprecated.
Will be removed in v4.28.0.

  [`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")

  [routingOptions](#routingOptions)

Specifies options for calculation of isolines for any vehicle type.

[`TruckOptions`](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing")

  [truckOptions](#truckOptions)

Deprecated.
Will be removed in v4.28.0.

## Constructor Summary

Constructors

Constructor

  Description

  [IsolineOptions](#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.CarOptions))`(`[`IsolineOptions.Calculation`](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing")` calculationOptions, `[`CarOptions`](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing")` carOptions)`

Deprecated.
Will be removed in v4.28.0.

  [IsolineOptions](#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.EVCarOptions))`(`[`IsolineOptions.Calculation`](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing")` calculationOptions, `[`EVCarOptions`](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing")` evCarOptions)`

Deprecated.
Will be removed in v4.28.0.

  [IsolineOptions](#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.EVTruckOptions))`(`[`IsolineOptions.Calculation`](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing")` calculationOptions, `[`EVTruckOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing")` evTruckOptions)`

Deprecated.
Will be removed in v4.28.0.

  [IsolineOptions](#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.RoutingOptions))`(`[`IsolineOptions.Calculation`](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing")` calculationOptions, `[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")` routingOptions)`

Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and routing options.

[IsolineOptions](#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.TruckOptions))`(`[`IsolineOptions.Calculation`](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing")` calculationOptions, `[`TruckOptions`](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing")` truckOptions)`

Deprecated.
Will be removed in v4.28.0.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### calculationOptions

@NonNull public [IsolineOptions.Calculation](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing") calculationOptions

    Specifies isoline parameters.

### carOptions

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @Nullable public [CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing") carOptions

    Deprecated.
Will be removed in v4.28.0. Use the `routing_options` instead.

Specifies options for calculation of isolines for car. Mutually exclusive with [`truckOptions`](#truckOptions), [`evCarOptions`](#evCarOptions), [`evTruckOptions`](#evTruckOptions) and [`routingOptions`](#routingOptions).

### truckOptions

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @Nullable public [TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing") truckOptions

    Deprecated.
Will be removed in v4.28.0. Use the `routing_options` instead.

Specifies options for calculation of isolines for truck. Mutually exclusive with [`carOptions`](#carOptions), [`evCarOptions`](#evCarOptions), [`evTruckOptions`](#evTruckOptions) and [`routingOptions`](#routingOptions).

### evCarOptions

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @Nullable public [EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing") evCarOptions

    Deprecated.
Will be removed in v4.28.0. Use the `routing_options` instead.

Specifies options for calculation of isolines for electric car. Mutually exclusive with [`carOptions`](#carOptions), [`truckOptions`](#truckOptions), [`evTruckOptions`](#evTruckOptions) and [`routingOptions`](#routingOptions).

### evTruckOptions

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @Nullable public [EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing") evTruckOptions

    Deprecated.
Will be removed in v4.28.0. Use the `routing_options` instead.

Specifies options for calculation of isolines for electric truck. Mutually exclusive with [`carOptions`](#carOptions), [`truckOptions`](#truckOptions), [`evCarOptions`](#evCarOptions) and [`routingOptions`](#routingOptions).

### routingOptions

@Nullable public [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") routingOptions

    Specifies options for calculation of isolines for any vehicle type. Mutually exclusive with [`carOptions`](#carOptions), [`truckOptions`](#truckOptions), [`evCarOptions`](#evCarOptions) and [`evTruckOptions`](#evTruckOptions).

## Constructor Details

  - (com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.CarOptions)" class="section detail">

### IsolineOptions

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public IsolineOptions(@NonNull [IsolineOptions.Calculation](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing") calculationOptions, @NonNull [CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing") carOptions)

    Deprecated.
Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.

Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and car routing options.
Parameters:
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `carOptions` -

    The options that should influence the possible routes within the isoline. This determines also the transportation type.
- (com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.TruckOptions)" class="section detail">

### IsolineOptions

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public IsolineOptions(@NonNull [IsolineOptions.Calculation](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing") calculationOptions, @NonNull [TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing") truckOptions)

    Deprecated.
Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.

Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and truck routing options.
Parameters:
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `truckOptions` -

    The options that should influence the possible routes within the isoline. This determines also the transportation type.
- (com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.EVCarOptions)" class="section detail">

### IsolineOptions

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public IsolineOptions(@NonNull [IsolineOptions.Calculation](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing") calculationOptions, @NonNull [EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing") evCarOptions)

    Deprecated.
Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.

Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric car routing options.
Parameters:
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `evCarOptions` -

    The options that should influence the possible routes within the isoline. This determines also the transportation type.
- (com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.EVTruckOptions)" class="section detail">

### IsolineOptions

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public IsolineOptions(@NonNull [IsolineOptions.Calculation](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing") calculationOptions, @NonNull [EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing") evTruckOptions)

    Deprecated.
Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.

Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and electric truck routing options.
Parameters:
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `evTruckOptions` -

    The options that should influence the possible routes within the isoline. This determines also the transportation type.
- (com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.RoutingOptions)" class="section detail">

### IsolineOptions

public IsolineOptions(@NonNull [IsolineOptions.Calculation](sdk-for-android-explore-api-reference-latestisolineoptions-calculation "class in com.here.sdk.routing") calculationOptions, @NonNull [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") routingOptions)

    Constructs options to calculate isolines from destination or origin, with preferences for isoline calculation and routing options. **Notes**

    - By default all vehicle specifications from [`RoutingOptions.transportSpecification`](sdk-for-android-explore-api-reference-latestroutingoptions#transportSpecification) are set to `null` and the [`TransportSpecification.transportMode`](sdk-for-android-explore-api-reference-latesttransportspecification#transportMode) from [`RoutingOptions.transportSpecification`](sdk-for-android-explore-api-reference-latestroutingoptions#transportSpecification) is set to [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR).
    - A route can be calculated with only the [`TransportSpecification.transportMode`](sdk-for-android-explore-api-reference-latesttransportspecification#transportMode) from [`RoutingOptions.transportSpecification`](sdk-for-android-explore-api-reference-latestroutingoptions#transportSpecification) set.
Parameters:
    `calculationOptions` -

    The options to be used to calculate this isoline.

    `routingOptions` -

    The options that should influence the possible routes within the isoline. This determines also the transportation type.
