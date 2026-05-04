---
title: "VehicleProfile (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestvehicleprofile"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class VehicleProfile

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.transport.VehicleProfile
------------------------------------------------------------------------
public final class VehicleProfile extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
A vehicle profile describes the vehicle being used with the HSDK.

The profile is planned to be used as single source of information describing the vehicle.

Current modules that use this profile:

- Navigation: Tracking mode for truck related vehicle restrictions.

**Note:** This is a beta release of this vehicle profile, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [axleCount](#axleCount)

Defines total number of axles in the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [grossWeightInKilograms](#grossWeightInKilograms)

Vehicle weight including trailers and shipped goods in kilograms.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")`>`

  [hazardousMaterials](#hazardousMaterials)

Specifies a list of hazardous materials shipped in the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [heightInCentimeters](#heightInCentimeters)

Vehicle height in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [lengthInCentimeters](#lengthInCentimeters)

Vehicle length in centimeters.

`int`

  [trailerCount](#trailerCount)

Defines number of trailers attached to the vehicle.

[`TruckCategory`](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport")

  [truckCategory](#truckCategory)

Defines the truck category.

[`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")

  [tunnelCategory](#tunnelCategory)

Specifies the tunnel categories to restrict certain route links.

[`VehicleType`](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")

  [vehicleType](#vehicleType)

Defines the vehicle type.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [weightPerAxleInKilograms](#weightPerAxleInKilograms)

Vehicle weight per axle in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [widthInCentimeters](#widthInCentimeters)

Vehicle width in centimeters.

## Constructor Summary

Constructors

Constructor

  Description

  [VehicleProfile](#%3Cinit%3E(com.here.sdk.transport.VehicleType))`(`[`VehicleType`](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport")` vehicleType)`

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

### vehicleType

@NonNull public [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") vehicleType

    Defines the vehicle type.

### truckCategory

@Nullable public [TruckCategory](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport") truckCategory

    Defines the truck category. Only used when the [`vehicleType`](#vehicleType) is [`VehicleType.TRUCK`](sdk-for-android-explore-api-reference-latestvehicletype#TRUCK) By default, it is not set.

### trailerCount

public int trailerCount

    Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. When not set, possible trailer count restrictions will not be taken into consideration for route calculation. By default, it is 0.

### hazardousMaterials

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")\> hazardousMaterials

    Specifies a list of hazardous materials shipped in the vehicle. Refer to [`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") for the available options.

### tunnelCategory

@Nullable public [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") tunnelCategory

    Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to [`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") for the available options.

### axleCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) axleCount

    Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. When not set, possible axle count restrictions will not be taken into consideration for route calculation. By default, it is not set.

### grossWeightInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) grossWeightInKilograms

    Vehicle weight including trailers and shipped goods in kilograms. By default, it is not set.

### heightInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) heightInCentimeters

    Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

### lengthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lengthInCentimeters

    Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

### widthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) widthInCentimeters

    Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

### weightPerAxleInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) weightPerAxleInKilograms

    Vehicle weight per axle in kilograms. The provided value must be greater or equal to 0. When not set, possible weight per axle restrictions will not be taken into consideration for route calculation. By default, it is not set.

## Constructor Details

  - (com.here.sdk.transport.VehicleType)" class="section detail">

### VehicleProfile

public VehicleProfile(@NonNull [VehicleType](sdk-for-android-explore-api-reference-latestvehicletype "enum class in com.here.sdk.transport") vehicleType)

    Creates a new instance.
Parameters:
    `vehicleType` -

    Defines the vehicle type.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
