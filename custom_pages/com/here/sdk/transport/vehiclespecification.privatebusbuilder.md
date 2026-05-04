---
title: "VehicleSpecification.PrivateBusBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class VehicleSpecification.PrivateBusBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.transport.VehicleSpecification.PrivateBusBuilder
Enclosing class:
[VehicleSpecification](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport")

------------------------------------------------------------------------
public static final class VehicleSpecification.PrivateBusBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
This class constructs a [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") for a private bus.

## Constructor Summary

Constructors

Constructor

  Description

  [PrivateBusBuilder](#%3Cinit%3E())`()`

Creates a new instance of this class.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport")

  [build](#build())`()`

Builds the [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") object for [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS) with the specifications taken from the [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withAxleCount](#withAxleCount(int))`(int axleCount)`

Sets the vehicle axle count.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withCurrentWeightInKilograms](#withCurrentWeightInKilograms(int))`(int currentWeightInKilograms)`

Sets the vehicle current weight in kilograms.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withEmptyWeightInKilograms](#withEmptyWeightInKilograms(int))`(int emptyWeightInKilograms)`

Sets the vehicle empty weight in kilograms.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withEngineSizeInCubicCentimeters](#withEngineSizeInCubicCentimeters(int))`(int engineSizeInCubicCentimeters)`

Sets the vehicle engine size in cubic centimeters.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withGrossWeightInKilograms](#withGrossWeightInKilograms(int))`(int grossWeightInKilograms)`

Sets the vehicle gross weight in kilograms.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withHeightInCentimeters](#withHeightInCentimeters(int))`(int heightInCentimeters)`

Sets the vehicle height in centimeters.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withIsCommercial](#withIsCommercial(boolean))`(boolean isCommercial)`

Sets the vehicle is commercial flag.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withLastCharacterOfLicensePlate](#withLastCharacterOfLicensePlate(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` lastCharacterOfLicensePlate)`

Sets the vehicle last character of the license plate.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withLengthInCentimeters](#withLengthInCentimeters(int))`(int lengthInCentimeters)`

Sets the vehicle length in centimeters.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withOccupancy](#withOccupancy(int))`(int occupancy)`

Sets the vehicle occupants number.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withTiresCount](#withTiresCount(int))`(int tiresCount)`

Sets the vehicle tires count.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withTrailerAxleCount](#withTrailerAxleCount(int))`(int trailerAxleCount)`

Sets the vehicle trailer axle count.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withTrailerCount](#withTrailerCount(int))`(int trailerCount)`

Sets the vehicle trailer count.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withTunnelCategory](#withTunnelCategory(com.here.sdk.transport.TunnelCategory))`(`[`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")` tunnelCategory)`

Sets the vehicle tunnel category.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withWeightPerAxleGroup](#withWeightPerAxleGroup(com.here.sdk.transport.WeightPerAxleGroup))`(`[`WeightPerAxleGroup`](sdk-for-android-explore-api-reference-latestweightperaxlegroup "class in com.here.sdk.transport")` weightPerAxleGroup)`

Sets the vehicle weight per axle group.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withWeightPerAxleInKilograms](#withWeightPerAxleInKilograms(int))`(int weightPerAxleInKilograms)`

Sets the vehicle weight per axle in kilograms.

[`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport")

  [withWidthInCentimeters](#withWidthInCentimeters(int))`(int widthInCentimeters)`

Sets the vehicle width in centimeters.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### PrivateBusBuilder

public PrivateBusBuilder()

    Creates a new instance of this class.

## Method Details

### withHeightInCentimeters

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withHeightInCentimeters(int heightInCentimeters)

    Sets the vehicle height in centimeters.
Parameters:
    `heightInCentimeters` -

    The vehicle height in centimeters.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the vehicle height set to the new value.

### withWidthInCentimeters

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withWidthInCentimeters(int widthInCentimeters)

    Sets the vehicle width in centimeters.
Parameters:
    `widthInCentimeters` -

    The vehicle width in centimeters.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the vehicle width set to the new value.

### withLengthInCentimeters

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withLengthInCentimeters(int lengthInCentimeters)

    Sets the vehicle length in centimeters.
Parameters:
    `lengthInCentimeters` -

    The vehicle length in centimeters.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the vehicle length set to the new value.

### withAxleCount

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withAxleCount(int axleCount)

    Sets the vehicle axle count.
Parameters:
    `axleCount` -

    The vehicle axle count.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the axle count set to the new value.

### withTrailerCount

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withTrailerCount(int trailerCount)

    Sets the vehicle trailer count.
Parameters:
    `trailerCount` -

    The vehicle trailer count.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the trailer count set to the new value.

### withTrailerAxleCount

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withTrailerAxleCount(int trailerAxleCount)

    Sets the vehicle trailer axle count.
Parameters:
    `trailerAxleCount` -

    The vehicle trailer axle count.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the trailer axle count set to the new value.

### withGrossWeightInKilograms

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withGrossWeightInKilograms(int grossWeightInKilograms)

    Sets the vehicle gross weight in kilograms.
Parameters:
    `grossWeightInKilograms` -

    The vehicle gross weight in kilograms.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the gross weight set to the new value.

### withCurrentWeightInKilograms

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withCurrentWeightInKilograms(int currentWeightInKilograms)

    Sets the vehicle current weight in kilograms.
Parameters:
    `currentWeightInKilograms` -

    The vehicle current weight in kilograms.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the current weight set to the new value.

### withEmptyWeightInKilograms

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withEmptyWeightInKilograms(int emptyWeightInKilograms)

    Sets the vehicle empty weight in kilograms.
Parameters:
    `emptyWeightInKilograms` -

    The vehicle empty weight in kilograms.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the empty weight set to the new value.

### withWeightPerAxleInKilograms

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withWeightPerAxleInKilograms(int weightPerAxleInKilograms)

    Sets the vehicle weight per axle in kilograms.
Parameters:
    `weightPerAxleInKilograms` -

    The vehicle weight per axle in kilograms.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the current weight per axle set to the new value.

### withWeightPerAxleGroup

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withWeightPerAxleGroup(@NonNull [WeightPerAxleGroup](sdk-for-android-explore-api-reference-latestweightperaxlegroup "class in com.here.sdk.transport") weightPerAxleGroup)

    Sets the vehicle weight per axle group.
Parameters:
    `weightPerAxleGroup` -

    The vehicle weight per axle group.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the current weight per axle group set to the new value.

### withIsCommercial

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withIsCommercial(boolean isCommercial)

    Sets the vehicle is commercial flag.
Parameters:
    `isCommercial` -

    The vehicle is commercial flag.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the is commercial flag set to the new value.

### withLastCharacterOfLicensePlate

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withLastCharacterOfLicensePlate(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) lastCharacterOfLicensePlate)

    Sets the vehicle last character of the license plate.
Parameters:
    `lastCharacterOfLicensePlate` -

    The vehicle last character of the license plate.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the last character of the licence plate set to the new value.

### withEngineSizeInCubicCentimeters

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withEngineSizeInCubicCentimeters(int engineSizeInCubicCentimeters)

    Sets the vehicle engine size in cubic centimeters.
Parameters:
    `engineSizeInCubicCentimeters` -

    The vehicle engine size in cubic centimeters.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the engine size set to the new value.

### withTiresCount

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withTiresCount(int tiresCount)

    Sets the vehicle tires count.
Parameters:
    `tiresCount` -

    The vehicle tires count.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the vehicle tires count set to the new value.

### withTunnelCategory

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withTunnelCategory(@NonNull [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") tunnelCategory)

    Sets the vehicle tunnel category.
Parameters:
    `tunnelCategory` -

    The vehicle tunnel category.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the vehicle tunnel category set to the new value.

### withOccupancy

@NonNull public [VehicleSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") withOccupancy(int occupancy)

    Sets the vehicle occupants number.
Parameters:
    `occupancy` -

    The vehicle occupants number.

    Returns:
    The [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object with the vehicle occupants number set to the new value.

### build

@NonNull public [VehicleSpecification](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") build()

    Builds the [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") object for [`TransportMode.BUS`](sdk-for-android-explore-api-reference-latesttransportmode#BUS) with the specifications taken from the [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object.
Returns:
    The [`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") object created from the [`VehicleSpecification.PrivateBusBuilder`](sdk-for-android-explore-api-reference-latestvehiclespecification-privatebusbuilder "class in com.here.sdk.transport") object.
