---
title: "TransportSpecification (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttransportspecification"
hidden: false
---

Package [com.here.sdk.transport](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class TransportSpecification

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.transport.TransportSpecification
------------------------------------------------------------------------
public final class TransportSpecification extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Contains transport attributes details related to the transport mode. **Notes**

- By default all vehicle specifications from `RoutingOptions.transport_specification` are set to `null` and the `RoutingOptions.transport_specification.transport_mode` is set to [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR).
- A route can be calculated with only the `RoutingOptions.transport_specification.transport_mode` set.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [TransportSpecification.BicycleBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-bicyclebuilder)

This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a bicycle.

`static final class `

  [TransportSpecification.BusBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-busbuilder)

This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a bus.

`static final class `

  [TransportSpecification.CarBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-carbuilder)

This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a car.

`static final class `

  [TransportSpecification.PedestrianBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-pedestrianbuilder)

This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for pedestrian.

`static final class `

  [TransportSpecification.PrivateBusBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-privatebusbuilder)

This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a private bus.

`static final class `

  [TransportSpecification.ScooterBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-scooterbuilder)

This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a scooter.

`static final class `

  [TransportSpecification.TaxiBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-taxibuilder)

This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a taxi.

`static final class `

  [TransportSpecification.TruckBuilder](sdk-for-android-explore-api-reference-latesttransportspecification-truckbuilder)

This class constructs a [`TransportSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification "class in com.here.sdk.transport") for a truck.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`PedestrianSpecification`](sdk-for-android-explore-api-reference-latestpedestrianspecification "class in com.here.sdk.transport")

  [pedestrianSpecification](#pedestrianSpecification)

The pedestrian specification for the transport mode.

[`ScooterSpecification`](sdk-for-android-explore-api-reference-latestscooterspecification "class in com.here.sdk.transport")

  [scooterSpecification](#scooterSpecification)

The scooter specification for the transport mode.

[`TaxiSpecification`](sdk-for-android-explore-api-reference-latesttaxispecification "class in com.here.sdk.transport")

  [taxiSpecification](#taxiSpecification)

The taxi specification for the transport mode.

[`TransportMode`](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")

  [transportMode](#transportMode)

Transport mode.

[`VehicleSpecification`](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport")

  [vehicleSpecification](#vehicleSpecification)

The vehicle specification for the transport mode.

## Constructor Summary

Constructors

Constructor

  Description

  [TransportSpecification](#%3Cinit%3E())`()`

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

### transportMode

@NonNull public [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") transportMode

    Transport mode. Defaults to `CAR`.

### vehicleSpecification

@Nullable public [VehicleSpecification](sdk-for-android-explore-api-reference-latestvehiclespecification "class in com.here.sdk.transport") vehicleSpecification

    The vehicle specification for the transport mode. By default, it is not set.

### pedestrianSpecification

@Nullable public [PedestrianSpecification](sdk-for-android-explore-api-reference-latestpedestrianspecification "class in com.here.sdk.transport") pedestrianSpecification

    The pedestrian specification for the transport mode. By default, it is not set.

### taxiSpecification

@Nullable public [TaxiSpecification](sdk-for-android-explore-api-reference-latesttaxispecification "class in com.here.sdk.transport") taxiSpecification

    The taxi specification for the transport mode. By default, it is not set.

### scooterSpecification

@Nullable public [ScooterSpecification](sdk-for-android-explore-api-reference-latestscooterspecification "class in com.here.sdk.transport") scooterSpecification

    The scooter specification for the transport mode. By default, it is not set.

## Constructor Details

  - ()" class="section detail">

### TransportSpecification

public TransportSpecification()

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
