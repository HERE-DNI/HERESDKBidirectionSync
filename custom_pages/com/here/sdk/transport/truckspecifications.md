---
title: "TruckSpecifications (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttruckspecifications"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TruckSpecifications

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.transport.TruckSpecifications
------------------------------------------------------------------------
public final class TruckSpecifications extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Truck specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.

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

  [grossWeightInKilograms](#grossWeightInKilograms)

Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [heightInCentimeters](#heightInCentimeters)

Truck height in centimeters.

`boolean`

  [isTruckLight](#isTruckLight)

A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [lengthInCentimeters](#lengthInCentimeters)

Truck length in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [payloadCapacityInKilograms](#payloadCapacityInKilograms)

Allowed payload capacity, including trailers, specified in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [trailerAxleCount](#trailerAxleCount)

Defines total number of axles across all the trailers attached to the vehicle.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [trailerCount](#trailerCount)

Defines number of trailers attached to the vehicle.

[`TruckType`](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport")

  [truckType](#truckType)

Defines the type of truck.

[`WeightPerAxleGroup`](sdk-for-android-explore-api-reference-latestweightperaxlegroup "class in com.here.sdk.transport")

  [weightPerAxleGroup](#weightPerAxleGroup)

Allows specification of axle weights in a more fine-grained way than `weight_per_axle_in_kilograms`.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [weightPerAxleInKilograms](#weightPerAxleInKilograms)

Heaviest weight per axle, regardless of axle type or axle group.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [widthInCentimeters](#widthInCentimeters)

Truck width in centimeters.

## Constructor Summary

Constructors

Constructor

  Description

  [TruckSpecifications](#%3Cinit%3E())`()`

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

### grossWeightInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) grossWeightInKilograms

    Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to [`currentWeightInKilograms`](#currentWeightInKilograms). By default, it is not set.

### currentWeightInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) currentWeightInKilograms

    Current truck weight, including trailers and shipped goods currently loaded, specified in kilograms. The provided value must be greater than or equal to 0. If unspecified, it will default to [`grossWeightInKilograms`](#grossWeightInKilograms). By default, it is not set.

### weightPerAxleInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) weightPerAxleInKilograms

    Heaviest weight per axle, regardless of axle type or axle group. It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions. The provided value must be greater or equal to 0. By default, it is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.

### weightPerAxleGroup

@Nullable public [WeightPerAxleGroup](sdk-for-android-explore-api-reference-latestweightperaxlegroup "class in com.here.sdk.transport") weightPerAxleGroup

    Allows specification of axle weights in a more fine-grained way than `weight_per_axle_in_kilograms`. This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden. By default is not set. **Note:** `weight_per_axle_in_kilograms` and `weight_per_axle_group` are incompatible. When available for your edition, if both attributes are set, during online RoutingEngine an \[sdk.routing.RoutingError.INVALID_PARAMETER\] error is generated. Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.

### heightInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) heightInCentimeters

    Truck height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

### widthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) widthInCentimeters

    Truck width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.

### lengthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lengthInCentimeters

    Truck length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.

### axleCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) axleCount

    Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. Rendering `sdk.mapview.TruckProfile`: When set, truck restriction icons for an axle count greater than [`axleCount`](#axleCount) will not be displayed. When specifying [`trailerAxleCount`](#trailerAxleCount), then [`axleCount`](#axleCount) is required and must be greater than [`trailerAxleCount`](#trailerAxleCount).

### trailerCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) trailerCount

    Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 255\]. By default, it is not set. When specifying [`trailerAxleCount`](#trailerAxleCount), then [`trailerCount`](#trailerCount) is required and must be greater than 0.

### truckType

@NonNull public [TruckType](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport") truckType

    Defines the type of truck. By default, it is [`TruckType.STRAIGHT`](sdk-for-android-explore-api-reference-latesttrucktype#STRAIGHT). Rendering `sdk.mapview.TruckProfile`: [`truckType`](#truckType) is ignored and has no effect.

### isTruckLight

public boolean isTruckLight

    A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan. The flag should not be set to `true` in other countries than Japan. The flag defaults to `false`.

    A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets the vehicle can access, which access restrictions apply, and which speed limits are applicable. Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.

    In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true, you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.

    When `TruckSpecifications` are set as part of `MapContentSettings`, then this flag will be ignored and has no effect.

    **Note:** This flag and the concept of light trucks are supported only in Japan as beta and are considered to be experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan. Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases with a deprecation process.

### payloadCapacityInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) payloadCapacityInKilograms

    Allowed payload capacity, including trailers, specified in kilograms. The provided value must be greater then or equal to 0. By default, it is not set.

### trailerAxleCount

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) trailerAxleCount

    Defines total number of axles across all the trailers attached to the vehicle. This number is included in [`axleCount`](#axleCount), hence [`trailerAxleCount`](#trailerAxleCount) must be less than [`axleCount`](#axleCount) and greater than or equal to 1. [`axleCount`](#axleCount) and [`trailerCount`](#trailerCount) are required to specify [`trailerAxleCount`](#trailerAxleCount). By default, it is not set. Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.

## Constructor Details

  - ()" class="section detail">

### TruckSpecifications

public TruckSpecifications()

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
