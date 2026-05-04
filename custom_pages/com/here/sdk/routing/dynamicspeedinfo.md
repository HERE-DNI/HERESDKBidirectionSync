---
title: "DynamicSpeedInfo (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdynamicspeedinfo"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class DynamicSpeedInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.DynamicSpeedInfo
------------------------------------------------------------------------
public final class DynamicSpeedInfo extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Provides estimated speed information.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [baseSpeedInMetersPerSecond](#baseSpeedInMetersPerSecond)

The speed in meters per second without taking traffic into consideration.

`double`

  [trafficSpeedInMetersPerSecond](#trafficSpeedInMetersPerSecond)

The speed in meters per second considering traffic.

`int`

  [turnTimeInSeconds](#turnTimeInSeconds)

The time it takes to make a turn, represented in seconds.

## Constructor Summary

Constructors

Constructor

  Description

  [DynamicSpeedInfo](#%3Cinit%3E(double,double,int))`(double baseSpeedInMetersPerSecond, double trafficSpeedInMetersPerSecond, int turnTimeInSeconds)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `double`

  [calculateJamFactor](#calculateJamFactor())`()`

Calculates the traffic jam factor that shows the traffic condition in a numeric way.

`boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### baseSpeedInMetersPerSecond

public double baseSpeedInMetersPerSecond

    The speed in meters per second without taking traffic into consideration.

### trafficSpeedInMetersPerSecond

public double trafficSpeedInMetersPerSecond

    The speed in meters per second considering traffic.

### turnTimeInSeconds

public int turnTimeInSeconds

    The time it takes to make a turn, represented in seconds.

## Constructor Details

  - (double,double,int)" class="section detail">

### DynamicSpeedInfo

public DynamicSpeedInfo(double baseSpeedInMetersPerSecond, double trafficSpeedInMetersPerSecond, int turnTimeInSeconds)

    Creates a new instance.
Parameters:
    `baseSpeedInMetersPerSecond` -

    The speed in meters per second without taking traffic into consideration.

    `trafficSpeedInMetersPerSecond` -

    The speed in meters per second considering traffic.

    `turnTimeInSeconds` -

    The time it takes to make a turn, represented in seconds.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### calculateJamFactor

public double calculateJamFactor()

    Calculates the traffic jam factor that shows the traffic condition in a numeric way.
Returns:
    Returns calculated jam factor in the range \[0.0, 10.0\]. A large jamFactor value means more traffic jam in general. Specifically, 0.0 means free traffic and 10.0 means stationary traffic.
