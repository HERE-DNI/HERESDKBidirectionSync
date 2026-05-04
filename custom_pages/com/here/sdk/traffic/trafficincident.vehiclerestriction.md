---
title: "TrafficIncident.VehicleRestriction (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficincident-vehiclerestriction"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TrafficIncident.VehicleRestriction

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.traffic.TrafficIncident.VehicleRestriction
Enclosing class:
[TrafficIncident](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic")

------------------------------------------------------------------------
public static final class TrafficIncident.VehicleRestriction extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The vehicle restriction representing a vehicle category and relevant restriction rules.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `boolean`

  [isCaravanRestricted](#isCaravanRestricted)

The flag indicating if a driving with a caravan is restricted for vehicles of the matching category.

`boolean`

  [isDestinationInIncidentAreaRestricted](#isDestinationInIncidentAreaRestricted)

The flag indicating if a traffic destination in the incident area is restricted for vehicles of the matching category.

`boolean`

  [isDieselFuelRestricted](#isDieselFuelRestricted)

The flag indicating if diesel fuel is restricted for vehicles of the matching category.

`boolean`

  [isDrivingWithoutSnowChainsRestricted](#isDrivingWithoutSnowChainsRestricted)

The flag indicating if a driving without snow chains is restricted for vehicles of the matching category.

`boolean`

  [isDrivingWithoutWinterTyresRestricted](#isDrivingWithoutWinterTyresRestricted)

The flag indicating if a driving without winter tyres is restricted for vehicles of the matching category.

`boolean`

  [isEuro3EmissionStandardRestricted](#isEuro3EmissionStandardRestricted)

The flag indicating if euro3 and weaker emission standards are restricted for vehicles of the matching category.

`boolean`

  [isEuro4EmissionStandardRestricted](#isEuro4EmissionStandardRestricted)

The flag indicating if euro4 and weaker emission standards are restricted for vehicles of the matching category.

`boolean`

  [isEuro5EmissionStandardRestricted](#isEuro5EmissionStandardRestricted)

The flag indicating if euro5 and weaker emission standards are restricted for vehicles of the matching category.

`boolean`

  [isEvenNumberPlateRestricted](#isEvenNumberPlateRestricted)

The flag indicating if a plate with even number is restricted for vehicles of the matching category.

`boolean`

  [isLpgFuelRestricted](#isLpgFuelRestricted)

The flag indicating if LPG fuel is restricted for vehicles of the matching category.

`boolean`

  [isOddNumberPlateRestricted](#isOddNumberPlateRestricted)

The flag indicating if a plate with odd number is restricted for vehicles of the matching category.

`boolean`

  [isPetrolFuelRestricted](#isPetrolFuelRestricted)

The flag indicating if petrol fuel is restricted for vehicles of the matching category.

`boolean`

  [isResidentsTrafficRestricted](#isResidentsTrafficRestricted)

The flag indicating if a residents traffic is restricted for vehicles of the matching category.

`boolean`

  [isRestrictedAlways](#isRestrictedAlways)

The flag indicating if vehicles of the matching category are restricted anyway (not depending on any vehicle parameter).

`boolean`

  [isThroughTrafficRestricted](#isThroughTrafficRestricted)

The flag indicating if a through traffic is restricted for vehicles of the matching category.

`boolean`

  [isTrailerRestricted](#isTrailerRestricted)

The flag indicating if a driving with a trailer is restricted for vehicles of the matching category.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfAxleWeightLessThanInKilograms](#restrictedIfAxleWeightLessThanInKilograms)

Vehicles of the matching category are restricted if the vehicle weight per axle is less than the weight in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfAxleWeightMoreThanInKilograms](#restrictedIfAxleWeightMoreThanInKilograms)

Vehicles of the matching category are restricted if the vehicle weight per axle is more than the weight in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfGrossWeightLessThanInKilograms](#restrictedIfGrossWeightLessThanInKilograms)

Vehicles of the matching category are restricted if the vehicle gross weight is less than the weight in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfGrossWeightMoreThanInKilograms](#restrictedIfGrossWeightMoreThanInKilograms)

Vehicles of the matching category are restricted if the vehicle gross weight is more than the weight in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfHigherThanInCentimeters](#restrictedIfHigherThanInCentimeters)

Vehicles of the matching category are restricted if the vehicle is higher than the height in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfLongerThanInCentimeters](#restrictedIfLongerThanInCentimeters)

Vehicles of the matching category are restricted if the vehicle is longer than the length in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfLowerThanInCentimeters](#restrictedIfLowerThanInCentimeters)

Vehicles of the matching category are restricted if the vehicle is lower than the height in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfNarrowerThanInCentimeters](#restrictedIfNarrowerThanInCentimeters)

Vehicles of the matching category are restricted if the vehicle is narrower than the width in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfOccupantsFewerThan](#restrictedIfOccupantsFewerThan)

Vehicles of the matching category are restricted if the occupants number is fewer than the value.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfOccupantsMoreThan](#restrictedIfOccupantsMoreThan)

Vehicles of the matching category are restricted if the occupants number is more than the value.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfShorterThanInCentimeters](#restrictedIfShorterThanInCentimeters)

Vehicles of the matching category are restricted if the vehicle is shorter than the length in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [restrictedIfWiderThanInCentimeters](#restrictedIfWiderThanInCentimeters)

Vehicles of the matching category are restricted if the vehicle is wider than the width in centimeters.

## Constructor Summary

Constructors

Constructor

  Description

  [VehicleRestriction](#%3Cinit%3E())`()`

Creates a new instance with default values.

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

### isRestrictedAlways

public boolean isRestrictedAlways

    The flag indicating if vehicles of the matching category are restricted anyway (not depending on any vehicle parameter).

### isDieselFuelRestricted

public boolean isDieselFuelRestricted

    The flag indicating if diesel fuel is restricted for vehicles of the matching category.

### isPetrolFuelRestricted

public boolean isPetrolFuelRestricted

    The flag indicating if petrol fuel is restricted for vehicles of the matching category.

### isLpgFuelRestricted

public boolean isLpgFuelRestricted

    The flag indicating if LPG fuel is restricted for vehicles of the matching category.

### isCaravanRestricted

public boolean isCaravanRestricted

    The flag indicating if a driving with a caravan is restricted for vehicles of the matching category.

### isTrailerRestricted

public boolean isTrailerRestricted

    The flag indicating if a driving with a trailer is restricted for vehicles of the matching category.

### isDrivingWithoutSnowChainsRestricted

public boolean isDrivingWithoutSnowChainsRestricted

    The flag indicating if a driving without snow chains is restricted for vehicles of the matching category.

### isDrivingWithoutWinterTyresRestricted

public boolean isDrivingWithoutWinterTyresRestricted

    The flag indicating if a driving without winter tyres is restricted for vehicles of the matching category.

### isEvenNumberPlateRestricted

public boolean isEvenNumberPlateRestricted

    The flag indicating if a plate with even number is restricted for vehicles of the matching category.

### isOddNumberPlateRestricted

public boolean isOddNumberPlateRestricted

    The flag indicating if a plate with odd number is restricted for vehicles of the matching category.

### isThroughTrafficRestricted

public boolean isThroughTrafficRestricted

    The flag indicating if a through traffic is restricted for vehicles of the matching category.

### isResidentsTrafficRestricted

public boolean isResidentsTrafficRestricted

    The flag indicating if a residents traffic is restricted for vehicles of the matching category.

### isDestinationInIncidentAreaRestricted

public boolean isDestinationInIncidentAreaRestricted

    The flag indicating if a traffic destination in the incident area is restricted for vehicles of the matching category.

### isEuro3EmissionStandardRestricted

public boolean isEuro3EmissionStandardRestricted

    The flag indicating if euro3 and weaker emission standards are restricted for vehicles of the matching category.

### isEuro4EmissionStandardRestricted

public boolean isEuro4EmissionStandardRestricted

    The flag indicating if euro4 and weaker emission standards are restricted for vehicles of the matching category.

### isEuro5EmissionStandardRestricted

public boolean isEuro5EmissionStandardRestricted

    The flag indicating if euro5 and weaker emission standards are restricted for vehicles of the matching category.

### restrictedIfGrossWeightMoreThanInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfGrossWeightMoreThanInKilograms

    Vehicles of the matching category are restricted if the vehicle gross weight is more than the weight in kilograms. If the value is `null` the upper gross weight bound is not specified.

### restrictedIfGrossWeightLessThanInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfGrossWeightLessThanInKilograms

    Vehicles of the matching category are restricted if the vehicle gross weight is less than the weight in kilograms. If the value is `null` the lower gross weight bound is not specified.

### restrictedIfAxleWeightMoreThanInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfAxleWeightMoreThanInKilograms

    Vehicles of the matching category are restricted if the vehicle weight per axle is more than the weight in kilograms. If the value is `null` the upper weight per axle bound is not specified.

### restrictedIfAxleWeightLessThanInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfAxleWeightLessThanInKilograms

    Vehicles of the matching category are restricted if the vehicle weight per axle is less than the weight in kilograms. If the value is `null` the lower weight per axle bound is not specified.

### restrictedIfLongerThanInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfLongerThanInCentimeters

    Vehicles of the matching category are restricted if the vehicle is longer than the length in centimeters. If the value is `null` the upper length bound is not specified.

### restrictedIfShorterThanInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfShorterThanInCentimeters

    Vehicles of the matching category are restricted if the vehicle is shorter than the length in centimeters. If the value is `null` the lower length bound is not specified.

### restrictedIfHigherThanInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfHigherThanInCentimeters

    Vehicles of the matching category are restricted if the vehicle is higher than the height in centimeters. If the value is `null` the upper height bound is not specified.

### restrictedIfLowerThanInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfLowerThanInCentimeters

    Vehicles of the matching category are restricted if the vehicle is lower than the height in centimeters. If the value is `null` the lower height bound is not specified.

### restrictedIfWiderThanInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfWiderThanInCentimeters

    Vehicles of the matching category are restricted if the vehicle is wider than the width in centimeters. If the value is `null` the upper width bound is not specified.

### restrictedIfNarrowerThanInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfNarrowerThanInCentimeters

    Vehicles of the matching category are restricted if the vehicle is narrower than the width in centimeters. If the value is `null` the lower width bound is not specified.

### restrictedIfOccupantsMoreThan

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfOccupantsMoreThan

    Vehicles of the matching category are restricted if the occupants number is more than the value. If the value is `null` the upper occupants bound is not specified.

### restrictedIfOccupantsFewerThan

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) restrictedIfOccupantsFewerThan

    Vehicles of the matching category are restricted if the occupants number is fewer than the value. If the value is `null` the lower occupants bound is not specified.

## Constructor Details

  - ()" class="section detail">

### VehicleRestriction

public VehicleRestriction()

    Creates a new instance with default values.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
