---
title: "EmpiricalConsumptionModel (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestempiricalconsumptionmodel"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class EmpiricalConsumptionModel

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.EmpiricalConsumptionModel
------------------------------------------------------------------------
public final class EmpiricalConsumptionModel extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This model defines a data-driven energy consumption model for electric vehicles.

It estimates the electrical energy required to traverse a route by combining empirically derived vehicle parameters with route characteristics such as distance, elevation changes, and driving speed. Rather than relying on a full physical simulation, this model uses observed consumption behavior to produce realistic and efficient energy estimates suitable for routing, range prediction, and navigation use cases.

Parameters specific to the electric vehicle are used to calculate energy consumption on a given route. At minimum, you must provide [`ascentConsumptionInWattHoursPerMeter`](#ascentConsumptionInWattHoursPerMeter), [`descentRecoveryInWattHoursPerMeter`](#descentRecoveryInWattHoursPerMeter) and a [`freeFlowSpeedTable`](#freeFlowSpeedTable). **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `double`

  [ascentConsumptionInWattHoursPerMeter](#ascentConsumptionInWattHoursPerMeter)

Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).

`double`

  [auxiliaryConsumptionInWattHoursPerSecond](#auxiliaryConsumptionInWattHoursPerSecond)

Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems (e.g., air conditioning, lights) per second of travel.

`double`

  [descentRecoveryInWattHoursPerMeter](#descentRecoveryInWattHoursPerMeter)

Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).

[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`>`

  [freeFlowSpeedTable](#freeFlowSpeedTable)

Free flow speed table describes energy consumption when traveling at constant speed.

[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html), [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)`>`

  [trafficSpeedTable](#trafficSpeedTable)

Traffic speed table describes energy consumption when traveling under heavy traffic conditions, i.e.

## Constructor Summary

Constructors

Constructor

  Description

  [EmpiricalConsumptionModel](#%3Cinit%3E())`()`

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

### ascentConsumptionInWattHoursPerMeter

public double ascentConsumptionInWattHoursPerMeter

    Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).

### descentRecoveryInWattHoursPerMeter

public double descentRecoveryInWattHoursPerMeter

    Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).

### freeFlowSpeedTable

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> freeFlowSpeedTable

    Free flow speed table describes energy consumption when traveling at constant speed. It defines a function curve specifying consumption rate at a given free flow speed on a flat stretch of road. Map keys represent speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. At minimum, one key/value pair must be set. In this case the consumption value is used for all possible speed keys.

### trafficSpeedTable

@NonNull public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)\> trafficSpeedTable

    Traffic speed table describes energy consumption when traveling under heavy traffic conditions, i.e. when the vehicle is expected to often change the travel speed. It defines a function curve specifying consumption rate at a given speed under traffic conditions on a flat stretch of road. Map keys represent traffic speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. If only one key/value pair is set, the consumption value is used for all possible traffic speed keys. If [`trafficSpeedTable`](#trafficSpeedTable) is empty then only [`freeFlowSpeedTable`](#freeFlowSpeedTable) is used for calculating speed-related energy consumption.

### auxiliaryConsumptionInWattHoursPerSecond

public double auxiliaryConsumptionInWattHoursPerSecond

    Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems (e.g., air conditioning, lights) per second of travel.

## Constructor Details

  - ()" class="section detail">

### EmpiricalConsumptionModel

public EmpiricalConsumptionModel()

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
