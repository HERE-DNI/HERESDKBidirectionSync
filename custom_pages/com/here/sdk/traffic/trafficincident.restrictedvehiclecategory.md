---
title: "TrafficIncident.RestrictedVehicleCategory (API Reference)"
slug: "sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory"
hidden: false
---

Package [com.here.sdk.traffic](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class TrafficIncident.RestrictedVehicleCategory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")\>
com.here.sdk.traffic.TrafficIncident.RestrictedVehicleCategory
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`TrafficIncident.RestrictedVehicleCategory`](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

<!-- -->

Enclosing class:
[TrafficIncident](sdk-for-android-explore-api-reference-latesttrafficincident "class in com.here.sdk.traffic")

------------------------------------------------------------------------
public static enum TrafficIncident.RestrictedVehicleCategory extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")\>
The vehicle categories that can be restricted. Note, a vehicle can belong to several categories (e.g. a passenger motor car belongs to [`CAR`](#CAR), [`MOTOR_VEHICLE`](#MOTOR_VEHICLE), and [`ALL`](#ALL)). A vehicle is restricted if it belongs to the category presented in the map [`TrafficIncident.getVehicleRestrictions()`](sdk-for-android-explore-api-reference-latesttrafficincident#getVehicleRestrictions()) and at least one of the vehicle properties is under the matching [`TrafficIncident.VehicleRestriction`](sdk-for-android-explore-api-reference-latesttrafficincident-vehiclerestriction "class in com.here.sdk.traffic").

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [ALL](#ALL)

All the vehicles are applicable for this category.

[BUS](#BUS)

Bus.

[CAR](#CAR)

Car.

[HEAVY_GOODS_VEHICLE](#HEAVY_GOODS_VEHICLE)

Heavy goods vehicle (or large goods vehicle).

[MOTOR_VEHICLE](#MOTOR_VEHICLE)

Motor vehicle.

[MOTORCYCLE](#MOTORCYCLE)

Motorcycle.

[OTHER](#OTHER)

Other vehicles.

[TAXI](#TAXI)

Taxi.

[TRAIN](#TRAIN)

Train.

[TRANSPORTING_ABNORMAL_SIZE_LOAD](#TRANSPORTING_ABNORMAL_SIZE_LOAD)

Transporting an abnormal size load.

[TRANSPORTING_HAZARDOUS_GOODS](#TRANSPORTING_HAZARDOUS_GOODS)

Transporting hazardous goods.

[TRUCK](#TRUCK)

Truck.

[VEHICLE_WITH_TRAILER](#VEHICLE_WITH_TRAILER)

Vehicle with trailer.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`TrafficIncident.RestrictedVehicleCategory`](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`TrafficIncident.RestrictedVehicleCategory`](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### BUS

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") BUS

    Bus.

### CAR

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") CAR

    Car.

### HEAVY_GOODS_VEHICLE

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") HEAVY_GOODS_VEHICLE

    Heavy goods vehicle (or large goods vehicle). In the European Union heavy goods vehicle is any truck with a gross combination mass (GCM) of over 3,500 kg.

### TRUCK

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") TRUCK

    Truck.

### MOTORCYCLE

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") MOTORCYCLE

    Motorcycle.

### MOTOR_VEHICLE

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") MOTOR_VEHICLE

    Motor vehicle. Definition: it is a self-propelled vehicle, that does not operate on rails and is used for the transportation of people or cargo.

### TAXI

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") TAXI

    Taxi.

### TRAIN

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") TRAIN

    Train.

### TRANSPORTING_ABNORMAL_SIZE_LOAD

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") TRANSPORTING_ABNORMAL_SIZE_LOAD

    Transporting an abnormal size load. See rules of the exact country that describe the exact parameters.

### TRANSPORTING_HAZARDOUS_GOODS

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") TRANSPORTING_HAZARDOUS_GOODS

    Transporting hazardous goods.

### VEHICLE_WITH_TRAILER

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") VEHICLE_WITH_TRAILER

    Vehicle with trailer.

### OTHER

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") OTHER

    Other vehicles.

### ALL

public static final [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") ALL

    All the vehicles are applicable for this category.

## Method Details

### values

public static [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [TrafficIncident.RestrictedVehicleCategory](sdk-for-android-explore-api-reference-latesttrafficincident-restrictedvehiclecategory "enum class in com.here.sdk.traffic") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
