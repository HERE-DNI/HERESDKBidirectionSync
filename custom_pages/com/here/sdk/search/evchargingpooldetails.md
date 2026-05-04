---
title: "EVChargingPoolDetails (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestevchargingpooldetails"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class EVChargingPoolDetails

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.EVChargingPoolDetails
------------------------------------------------------------------------
public final class EVChargingPoolDetails extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Electric vehicle charging pool details.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [evChargingOnSite](#evChargingOnSite)

Indicates if the Place offers EV charging to customer or the general public.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [evNetwork](#evNetwork)

The name of the EV Network that operates the charging station.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [ownerInformation](#ownerInformation)

Represents the party of ownership provided by some suppliers.

[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html)

  [reservable](#reservable)

Indicates if the charging stations can be reserved.

[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html)

  [totalNumberOfStations](#totalNumberOfStations)

Indicates the total number of stations available on the charging pool.

## Constructor Summary

Constructors

Constructor

  Description

  [EVChargingPoolDetails](#%3Cinit%3E())`()`

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

### evChargingOnSite

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) evChargingOnSite

    Indicates if the Place offers EV charging to customer or the general public.

### evNetwork

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) evNetwork

    The name of the EV Network that operates the charging station. Note: not all stations participate in a network.

### ownerInformation

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) ownerInformation

    Represents the party of ownership provided by some suppliers.

### reservable

@Nullable public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html) reservable

    Indicates if the charging stations can be reserved. Note: Reservable charging stations operate on a first-come/first served basis.

### totalNumberOfStations

@Nullable public [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html) totalNumberOfStations

    Indicates the total number of stations available on the charging pool.

## Constructor Details

  - ()" class="section detail">

### EVChargingPoolDetails

public EVChargingPoolDetails()

    Creates a new instance. For offline EV rich attributes, also enable [`LayerConfiguration.Feature.EV`](sdk-for-android-explore-api-reference-latestlayerconfiguration-feature#EV) in [`SDKOptions.layerConfiguration`](sdk-for-android-explore-api-reference-latestsdkoptions#layerConfiguration).

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
