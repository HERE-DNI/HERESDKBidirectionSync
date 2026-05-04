---
title: "AllowOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestallowoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class AllowOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.AllowOptions
------------------------------------------------------------------------
public final class AllowOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options explicitly allowed by user for route calculations.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [allowHot](#allowHot)

A flag that specifies whether HOT lanes can be used in the calculation.

`boolean`

  [allowHov](#allowHov)

A flag that specifies whether HOV lanes can be used in the route calculation.

## Constructor Summary

Constructors

Constructor

  Description

  [AllowOptions](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### allowHov

public boolean allowHov

    A flag that specifies whether HOV lanes can be used in the route calculation.

    A HOV (High occupancy Vehicle) lane or carpool lane is reserved for carpool usage. Carpool lane requires a minimum number of passengers in order for the car to use the carpool lane.

    **Note:** Can be used with `RoutingOptions.transport_specification.vehicle_specification.occupancy` to specify the number of occupants in the vehicle.

### allowHot

public boolean allowHot

    A flag that specifies whether HOT lanes can be used in the calculation.

    HOT (high-occupancy toll) lanes are HOV lanes where vehicles that do not qualify as high-occupancy are allowed to pass by paying a toll.

    **Note:** Can be used with `RoutingOptions.transport_specification.vehicle_specification.occupancy` to specify the number of occupants in the vehicle.

## Constructor Details

  - ()" class="section detail">

### AllowOptions

public AllowOptions()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
