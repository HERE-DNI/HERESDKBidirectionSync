---
title: "TruckAmenities (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttruckamenities"
hidden: false
---

Package [com.here.sdk.search](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TruckAmenities

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.search.TruckAmenities
------------------------------------------------------------------------
public final class TruckAmenities extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Truck amenities struct, represents availability (true/false) for each feature, except shower_count - number of showers, if data is available. Note: This is a BETA feature and thus subject to change.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [hasCarWash](#hasCarWash)

Has car wash

`boolean`

  [hasChemicalToiletDisposal](#hasChemicalToiletDisposal)

Has chemical toilet disposal

`boolean`

  [hasHighCanopy](#hasHighCanopy)

Has high canopy

`boolean`

  [hasIdleReductionSystem](#hasIdleReductionSystem)

Has idle reduction system

`boolean`

  [hasParking](#hasParking)

Has parking

`boolean`

  [hasPowerSupply](#hasPowerSupply)

Has power supply

`boolean`

  [hasSecureParking](#hasSecureParking)

Has secure parking

`boolean`

  [hasShower](#hasShower)

Has shower

`boolean`

  [hasTruckScales](#hasTruckScales)

Has truck scales

`boolean`

  [hasTruckService](#hasTruckService)

Has truck service

`boolean`

  [hasTruckStop](#hasTruckStop)

Has truck stop

`boolean`

  [hasTruckWash](#hasTruckWash)

Has truck wash

`boolean`

  [hasWifi](#hasWifi)

Has WiFi

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [showerCount](#showerCount)

Shower count, if shower data is present

## Constructor Summary

Constructors

Constructor

  Description

  [TruckAmenities](#%3Cinit%3E())`()`

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

### hasParking

public boolean hasParking

    Has parking

### hasSecureParking

public boolean hasSecureParking

    Has secure parking

### hasCarWash

public boolean hasCarWash

    Has car wash

### hasTruckWash

public boolean hasTruckWash

    Has truck wash

### hasHighCanopy

public boolean hasHighCanopy

    Has high canopy

### hasIdleReductionSystem

public boolean hasIdleReductionSystem

    Has idle reduction system

### hasTruckScales

public boolean hasTruckScales

    Has truck scales

### hasPowerSupply

public boolean hasPowerSupply

    Has power supply

### hasChemicalToiletDisposal

public boolean hasChemicalToiletDisposal

    Has chemical toilet disposal

### hasTruckStop

public boolean hasTruckStop

    Has truck stop

### hasWifi

public boolean hasWifi

    Has WiFi

### hasTruckService

public boolean hasTruckService

    Has truck service

### hasShower

public boolean hasShower

    Has shower

### showerCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) showerCount

    Shower count, if shower data is present

## Constructor Details

  - ()" class="section detail">

### TruckAmenities

public TruckAmenities()

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
