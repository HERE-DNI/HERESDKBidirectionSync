---
title: "VehicleSpecification (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestvehiclespecification"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class VehicleSpecification

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.transport.VehicleSpecification
------------------------------------------------------------------------
public final class VehicleSpecification extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [VehicleSpecification.BusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-busbuilder)

This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a bus.

`static final class `

  [VehicleSpecification.CarBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-carbuilder)

This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a car.

`static final class `

  [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder)

This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a private bus.

`static final class `

  [VehicleSpecification.ScooterBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-scooterbuilder)

This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a scooter.

`static final class `

  [VehicleSpecification.TaxiBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-taxibuilder)

This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a taxi.

`static final class `

  [VehicleSpecification.TruckBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-truckbuilder)

This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a truck.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [axleCount](#axleCount)

Defines total number of axles in the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [currentWeightInKilograms](#currentWeightInKilograms)

Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [emptyWeightInKilograms](#emptyWeightInKilograms)

Empty weight of the vehicle without any load, excluding trailers, specified in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [engineSizeInCubicCentimeters](#engineSizeInCubicCentimeters)

Engine size of the scooter in cubic centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [grossWeightInKilograms](#grossWeightInKilograms)

Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")`>`

  [hazardousMaterials](#hazardousMaterials)

Specifies a list of hazardous materials shipped in the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [heightInCentimeters](#heightInCentimeters)

Vehicle height in centimeters.

`boolean`

  [isCommercial](#isCommercial)

Specifies whether the vehicle is a commercial or a non-commercial vehicle.

`boolean`

  [isTruckLight](#isTruckLight)

A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [kingpinToRearAxleDistanceInCentimeters](#kingpinToRearAxleDistanceInCentimeters)

Defines the kingpin to rear axle distance, in centimeters.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [lastCharacterOfLicensePlate](#lastCharacterOfLicensePlate)

Last character of license plate in String format.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [lengthInCentimeters](#lengthInCentimeters)

Vehicle length in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [occupancy](#occupancy)

Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [payloadCapacityInKilograms](#payloadCapacityInKilograms)

Allowed payload capacity, including trailers, specified in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [tiresCount](#tiresCount)

The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [trailerAxleCount](#trailerAxleCount)

Defines total number of axles across all the trailers attached to the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [trailerCount](#trailerCount)

Defines number of trailers attached to the vehicle.

[`TruckCategory`](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport")

  [truckCategory](#truckCategory)

Defines the truck category.

[`TruckType`](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport")

  [truckType](#truckType)

Deprecated.
Will be removed in v4.27.0.

  [`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")

  [tunnelCategory](#tunnelCategory)

Specifies the tunnel categories to restrict certain route links.

[`WeightPerAxleGroup`](sdk-for-android-explore-api-reference-latestweightperaxlegroup "class in com.here.sdk.transport")

  [weightPerAxleGroup](#weightPerAxleGroup)

Allows specification of axle weights in a more fine-grained way than [`weightPerAxleInKilograms`](#weightPerAxleInKilograms).

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [weightPerAxleInKilograms](#weightPerAxleInKilograms)

Heaviest weight per axle, regardless of axle type or axle group.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [widthInCentimeters](#widthInCentimeters)

Vehicle width in centimeters.

## Constructor Summary

Constructors

Constructor

  Description

  [VehicleSpecification](#%3Cinit%3E())`()`

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

### heightInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) heightInCentimeters

    Vehicle height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

    **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### widthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) widthInCentimeters

    Vehicle width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

    **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### lengthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lengthInCentimeters

    Vehicle length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

    **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### axleCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) axleCount

    Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering: When set, truck restriction icons for an axle count greater than [`axleCount`](#axleCount) will not be displayed. When specifying [`trailerAxleCount`](#trailerAxleCount), then [`axleCount`](#axleCount) is required and must be greater than [`trailerAxleCount`](#trailerAxleCount).

    **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### trailerCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) trailerCount

    Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying [`trailerAxleCount`](#trailerAxleCount), then [`trailerCount`](#trailerCount) is required and must be greater than 0.

### truckType

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TruckType](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport") truckType

    Deprecated.
Will be removed in v4.27.0. Use `VehicleSpecification.truckCategory` instead.

Will be replaced with `truckCategory` when the `TruckSpecification` will be replaced by `VehicleSpecification`. Defines the type of truck. Defaults to [`TruckType.STRAIGHT`](sdk-for-android-explore-api-reference-latesttrucktype#STRAIGHT). Rendering `sdk.mapview.TruckProfile`: [`truckType`](#truckType) is ignored and has no effect.

### truckCategory

@Nullable public [TruckCategory](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport") truckCategory

    Defines the truck category. By default, it is not set. Rendering: [`truckCategory`](#truckCategory) is ignored and has no effect.

### isTruckLight

public boolean isTruckLight

    A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. Defaults to `false`.

    A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.

    In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to `true`, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to `true`, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

    When on `MapContentSettings`, then this flag will be ignored and has no effect.

    **Notes:**

    - This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.
    - Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
    - Supported only in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK) transport mode.

### payloadCapacityInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) payloadCapacityInKilograms

    Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.

    **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### trailerAxleCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) trailerAxleCount

    Defines total number of axles across all the trailers attached to the vehicle. This number is included in [`axleCount`](#axleCount), hence [`trailerAxleCount`](#trailerAxleCount) must be less than [`axleCount`](#axleCount) and greater than or equal to 1. [`axleCount`](#axleCount) and [`trailerCount`](#trailerCount) are required to specify [`trailerAxleCount`](#trailerAxleCount). By default, it is not set.

    **Note:**: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

### kingpinToRearAxleDistanceInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) kingpinToRearAxleDistanceInCentimeters

    Defines the kingpin to rear axle distance, in centimeters.

    **NOTE:** Currently, the KPRA restrictions are only present in California and Idaho. **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### emptyWeightInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) emptyWeightInKilograms

    Empty weight of the vehicle without any load, excluding trailers, specified in kilograms. The provided value must be greater than or equal to 0. By default, it is not set.

    **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### grossWeightInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) grossWeightInKilograms

    Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to [`currentWeightInKilograms`](#currentWeightInKilograms). By default, it is not set.

    **Notes:**

    - Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.
    - Maximum weight for a car or taxi *without* a trailer is 4250 kg.
    - Maximum weight for a car or taxi *with* a trailer is 7550 kg.

### currentWeightInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) currentWeightInKilograms

    Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to [`grossWeightInKilograms`](#grossWeightInKilograms). By default, it is not set.

    **Notes:**

    - Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.
    - Maximum weight for a car or taxi *without* a trailer is 5000 kg.
    - Maximum weight for a car or taxi *with* a trailer is 8500 kg.
    - A route request with [`currentWeightInKilograms`](#currentWeightInKilograms) above [`grossWeightInKilograms`](#grossWeightInKilograms) may result in non-compliant or invalid routes.

### weightPerAxleInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) weightPerAxleInKilograms

    Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set.

    **Notes:**

    - [`weightPerAxleInKilograms`](#weightPerAxleInKilograms) and [`weightPerAxleGroup`](#weightPerAxleGroup) are incompatible. When available for your edition, if both attributes are set, during online `RoutingEngine` an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline `RoutingEngine` is in place, both parameters are evaluated and the maximum value between them will be used.
    - Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### weightPerAxleGroup

@Nullable public [WeightPerAxleGroup](sdk-for-android-explore-api-reference-latestweightperaxlegroup "class in com.here.sdk.transport") weightPerAxleGroup

    Allows specification of axle weights in a more fine-grained way than [`weightPerAxleInKilograms`](#weightPerAxleInKilograms). This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set.

    **Notes:**

    - [`weightPerAxleInKilograms`](#weightPerAxleInKilograms) and [`weightPerAxleGroup`](#weightPerAxleGroup) are incompatible. When available for your edition, if both attributes are set, during online `RoutingEngine` an `RoutingError.INVALID_PARAMETER` error is generated. Otherwise, when offline `RoutingEngine` is in place, both parameters are evaluated and the maximum value between them will be used.
    - Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### isCommercial

public boolean isCommercial

    Specifies whether the vehicle is a commercial or a non-commercial vehicle. Defaults to `false`.

    **Notes**

    - Only supported for online routing.
    - This parameter is currently used only for the calculation of tolls in regions where it is applicable.
    - Not used for offline calculations.
    - Supported for [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS) and [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI).

### lastCharacterOfLicensePlate

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lastCharacterOfLicensePlate

    Last character of license plate in String format. This value can be used to evaluate restrictions in environmental zones. By default, it is not set.

### engineSizeInCubicCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) engineSizeInCubicCentimeters

    Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535. Default value is `null`, which means the scooter route calculation ignores all engine size limits on the road.

    **Notes**

    - For now, this option is only relevant in Japan and will be ignored for other countries. Currently, map data for this option is only available for Japan.
    - Supported only in [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) (Alpha) transport mode.

### tiresCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) tiresCount

    The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers. By default, it is not set. Otherwise it is guaranteed to be in the range \[1, 255\].

    **Note**: This parameter is not supported in isoline routing.

### tunnelCategory

@Nullable public [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") tunnelCategory

    Specifies the tunnel categories to restrict certain route links. The route will pass only through tunnels of a less strict category. Refer to [`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") for the available options. By default, it is not set.

    **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### hazardousMaterials

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")\> hazardousMaterials

    Specifies a list of hazardous materials shipped in the vehicle. Refer to [`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport") for the available options. By default, it is an empty list.

    **Note:** Supported in [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK), [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS), [`TransportMode.PRIVATE_BUS`](sdk-for-android-explore-api-reference-latesttransportmode#PRIVATE_BUS), [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR) (Beta), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI) (Beta) transport modes.

### occupancy

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) occupancy

    Specifies the number of occupants in the vehicle, including driver, can affect the vehicle's ability to use HOV/carpool restricted lanes. Should not be less than 1 or greater than 255. By default, it is not set.

## Constructor Details

  - ()" class="section detail">

### VehicleSpecification

public VehicleSpecification()

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
