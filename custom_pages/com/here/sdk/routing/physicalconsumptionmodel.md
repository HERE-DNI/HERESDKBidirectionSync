---
title: "PhysicalConsumptionModel (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestphysicalconsumptionmodel"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PhysicalConsumptionModel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.PhysicalConsumptionModel
------------------------------------------------------------------------
public final class PhysicalConsumptionModel extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Defines the physical consumption model for electric vehicles, using vehicle-specific parameters to calculate energy consumption along a route. **Note:** \[sdk.transport.VehicleSpecification.current_weight_in_kilograms\] must be set. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [airDragCoefficient](#airDragCoefficient)

The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air.

`double`

  [auxiliaryPowerConsumptionInWatts](#auxiliaryPowerConsumptionInWatts)

Power (in W) consumed by the vehicle's auxiliary systems (for example, air conditioning, lights).

`double`

  [driveTrainEfficiency](#driveTrainEfficiency)

The proportion of the energy drawn from the battery that is used to move the vehicle.

`double`

  [frontalAreaInSquareMeters](#frontalAreaInSquareMeters)

Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.

`double`

  [recuperationEfficiency](#recuperationEfficiency)

The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.

`double`

  [rollingResistanceCoefficient](#rollingResistanceCoefficient)

Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface.

## Constructor Summary

Constructors

Constructor

  Description

  [PhysicalConsumptionModel](#%3Cinit%3E())`()`

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

### driveTrainEfficiency

public double driveTrainEfficiency

    The proportion of the energy drawn from the battery that is used to move the vehicle. (This is to factor in energy losses through heat in the motors, for example.) Supported range from 0 to 1

### recuperationEfficiency

public double recuperationEfficiency

    The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.

    Supported range from 0 to 1

### auxiliaryPowerConsumptionInWatts

public double auxiliaryPowerConsumptionInWatts

    Power (in W) consumed by the vehicle's auxiliary systems (for example, air conditioning, lights).

    The provided value must be greater than or equal to 0.

### frontalAreaInSquareMeters

public double frontalAreaInSquareMeters

    Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters. Physical consumption model is using this value in combination with `airDragCoefficient` to calculate the consumption caused by air resistance. As fallback [`VehicleSpecification.widthInCentimeters`](sdk-for-android-explore-api-reference-latestvehiclespecification#widthInCentimeters) and [`VehicleSpecification.heightInCentimeters`](sdk-for-android-explore-api-reference-latestvehiclespecification#heightInCentimeters) are used.

    This parameter is used to provide a more accurate consumption prediction for electric vehicles.

    In the range from 0.5 to 50

### rollingResistanceCoefficient

public double rollingResistanceCoefficient

    Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface. The main causes of this resistance are tire deformation, wing drag, and friction with the ground. The coefficient of rolling resistance is a numerical value indicating the severity of this factor.

    This parameter is used to provide a more accurate consumption prediction for electric vehicles.

    Supported range from 0 to 1

### airDragCoefficient

public double airDragCoefficient

    The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air. More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.

    This parameter is used to provide a more accurate consumption prediction for electric vehicles.

    Supported range from 0 to 1

## Constructor Details

  - ()" class="section detail">

### PhysicalConsumptionModel

public PhysicalConsumptionModel()

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
