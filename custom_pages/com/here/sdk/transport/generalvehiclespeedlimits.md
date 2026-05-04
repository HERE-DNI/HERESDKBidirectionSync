---
title: "GeneralVehicleSpeedLimits (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestgeneralvehiclespeedlimits"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class GeneralVehicleSpeedLimits

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.transport.GeneralVehicleSpeedLimits
------------------------------------------------------------------------
public final class GeneralVehicleSpeedLimits extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains the speed limits for vehicles in a country / state.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxSpeedHighwaysInMetersPerSecond](#maxSpeedHighwaysInMetersPerSecond)

The general speed limit on highways for the country / state.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxSpeedNightInMetersPerSecond](#maxSpeedNightInMetersPerSecond)

The general speed limit at night for the country / state.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxSpeedRainingInMetersPerSecond](#maxSpeedRainingInMetersPerSecond)

The general speed limit when raining for the country / state.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxSpeedRuralInMetersPerSecond](#maxSpeedRuralInMetersPerSecond)

The general speed limit on rural roads for the country / state.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxSpeedSnowingInMetersPerSecond](#maxSpeedSnowingInMetersPerSecond)

The general speed limit when snowing for the country / state.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [maxSpeedUrbanInMetersPerSecond](#maxSpeedUrbanInMetersPerSecond)

The general speed limit on urban roads for the country / state.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [minSpeedHighwaysInMetersPerSecond](#minSpeedHighwaysInMetersPerSecond)

The minimum speed on highways for the country / state.

## Constructor Summary

Constructors

Constructor

  Description

  [GeneralVehicleSpeedLimits](#%3Cinit%3E())`()`

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

### maxSpeedHighwaysInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxSpeedHighwaysInMetersPerSecond

    The general speed limit on highways for the country / state. It is `null` if the general speed limit on highways for the country / state is not specified.

### maxSpeedRuralInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxSpeedRuralInMetersPerSecond

    The general speed limit on rural roads for the country / state. It is `null` if the general speed limit on rural roads for the country / state is not specified.

### maxSpeedUrbanInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxSpeedUrbanInMetersPerSecond

    The general speed limit on urban roads for the country / state. It is `null` if the general speed limit on urban roads for the country / state is not specified.

### maxSpeedRainingInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxSpeedRainingInMetersPerSecond

    The general speed limit when raining for the country / state. It is `null` if the general speed limit when raining for the country / state is not specified.

### maxSpeedSnowingInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxSpeedSnowingInMetersPerSecond

    The general speed limit when snowing for the country / state. It is `null` if the general speed limit when snowing for the country / state is not specified.

### maxSpeedNightInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) maxSpeedNightInMetersPerSecond

    The general speed limit at night for the country / state. It is `null` if the general speed limit at night for the country / state is not specified.

### minSpeedHighwaysInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) minSpeedHighwaysInMetersPerSecond

    The minimum speed on highways for the country / state. It is `null` if the minimum speed on highways for the country / state is not specified.

## Constructor Details

  - ()" class="section detail">

### GeneralVehicleSpeedLimits

public GeneralVehicleSpeedLimits()

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
