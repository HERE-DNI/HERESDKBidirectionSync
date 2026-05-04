---
title: "ViolatedRestriction.Details (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestviolatedrestriction-details"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class ViolatedRestriction.Details

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.ViolatedRestriction.Details
Enclosing class:
[ViolatedRestriction](sdk-for-android-explore-api-reference-latestviolatedrestriction "class in com.here.sdk.routing")

------------------------------------------------------------------------
public static final class ViolatedRestriction.Details extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set. For example, if the vehicle violates the maximum allowed height during the trip, then the member `max_height_in_centimeters` will be set with the maximum allowed height value.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`IntegerRange`](sdk-for-android-explore-api-reference-latestintegerrange "class in com.here.sdk.core")

  [forbiddenAxleCount](#forbiddenAxleCount)

The restriction to trucks with axles number within specified range during the trip.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`HazardousMaterial`](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")`>`

  [forbiddenHazardousGoods](#forbiddenHazardousGoods)

There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using [`VehicleSpecification.hazardousMaterials`](sdk-for-android-explore-api-reference-latestvehiclespecification#hazardousMaterials) from [`TransportSpecification.vehicleSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification#vehicleSpecification) from [`RoutingOptions.transportSpecification`](sdk-for-android-explore-api-reference-latestroutingoptions#transportSpecification).

[`IntegerRange`](sdk-for-android-explore-api-reference-latestintegerrange "class in com.here.sdk.core")

  [forbiddenTrailerCount](#forbiddenTrailerCount)

Constrains the restriction to trucks with number of trailer within specified range during the trip.

[`TruckCategory`](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport")

  [forbiddenTruckCategory](#forbiddenTruckCategory)

This property will be set if a restriction applies to the value of [`TruckCategory`](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport") parameter used for route calculation.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TruckRoadType`](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport")`>`

  [forbiddenTruckRoadTypes](#forbiddenTruckRoadTypes)

Contains violated restrictions for truck road types.

[`TruckType`](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport")

  [forbiddenTruckType](#forbiddenTruckType)

Deprecated.
Will be removed in v4.27.0.

  [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxHeightInCentimeters](#maxHeightInCentimeters)

Max permitted height during the trip, in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxKingpinToRearAxleDistanceInCentimeters](#maxKingpinToRearAxleDistanceInCentimeters)

Contains the maximum permitted distance from kingpin to the rear axle in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxLengthInCentimeters](#maxLengthInCentimeters)

Max permitted length during the trip, in centimeters.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxNumberOfTires](#maxNumberOfTires)

Contains the maximum permitted number of tires.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxPayloadCapacityInKilograms](#maxPayloadCapacityInKilograms)

Max permitted payload capacity during the trip, in kilograms.

[`TunnelCategory`](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport")

  [maxTunnelCategory](#maxTunnelCategory)

Tunnel category to restrict transport of specific goods during the trip.

[`VehicleRestrictionMaxWeight`](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweight "class in com.here.sdk.routing")

  [maxWeight](#maxWeight)

Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.

[`MaxAxleGroupWeight`](sdk-for-android-explore-api-reference-latestmaxaxlegroupweight "class in com.here.sdk.routing")

  [maxWeightPerAxleGroupInKilograms](#maxWeightPerAxleGroupInKilograms)

Max permitted weight per axle group during the trip, in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxWeightPerAxleInKilograms](#maxWeightPerAxleInKilograms)

Max permitted weight per axle during the trip, in kilograms.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [maxWidthInCentimeters](#maxWidthInCentimeters)

Max permitted width during the trip, in centimeters.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [routingZoneReference](#routingZoneReference)

Contains the restricted routing zone reference This property will be set if the [`AvoidanceOptions.zoneCategories`](sdk-for-android-explore-api-reference-latestavoidanceoptions#zoneCategories) is not empty

[`TimeRule`](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core")

  [timeRule](#timeRule)

Time intervals during which restrictions are enforced.

## Constructor Summary

Constructors

Constructor

  Description

  [Details](#%3Cinit%3E())`()`

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

### maxWeightPerAxleInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxWeightPerAxleInKilograms

    Max permitted weight per axle during the trip, in kilograms. This property will be set if the [`TruckSpecifications.weightPerAxleInKilograms`](sdk-for-android-explore-api-reference-latesttruckspecifications#weightPerAxleInKilograms) exceeds this value.

### maxWeightPerAxleGroupInKilograms

@Nullable public [MaxAxleGroupWeight](sdk-for-android-explore-api-reference-latestmaxaxlegroupweight "class in com.here.sdk.routing") maxWeightPerAxleGroupInKilograms

    Max permitted weight per axle group during the trip, in kilograms. This property will be set if the [`TruckSpecifications.weightPerAxleGroup`](sdk-for-android-explore-api-reference-latesttruckspecifications#weightPerAxleGroup) exceeds this value.

### maxHeightInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxHeightInCentimeters

    Max permitted height during the trip, in centimeters. This property will be set if the [`TruckSpecifications.heightInCentimeters`](sdk-for-android-explore-api-reference-latesttruckspecifications#heightInCentimeters) exceeds this value.

### maxWidthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxWidthInCentimeters

    Max permitted width during the trip, in centimeters. This property will be set if the [`TruckSpecifications.widthInCentimeters`](sdk-for-android-explore-api-reference-latesttruckspecifications#widthInCentimeters) exceeds this value.

### maxLengthInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxLengthInCentimeters

    Max permitted length during the trip, in centimeters. This property will be set if the [`TruckSpecifications.lengthInCentimeters`](sdk-for-android-explore-api-reference-latesttruckspecifications#lengthInCentimeters) exceeds this value.

### forbiddenAxleCount

@Nullable public [IntegerRange](sdk-for-android-explore-api-reference-latestintegerrange "class in com.here.sdk.core") forbiddenAxleCount

    The restriction to trucks with axles number within specified range during the trip. This property will be set if the [`TruckSpecifications.axleCount`](sdk-for-android-explore-api-reference-latesttruckspecifications#axleCount) is within this range.

### forbiddenTrailerCount

@Nullable public [IntegerRange](sdk-for-android-explore-api-reference-latestintegerrange "class in com.here.sdk.core") forbiddenTrailerCount

    Constrains the restriction to trucks with number of trailer within specified range during the trip. This property will be set if the [`TruckSpecifications.trailerCount`](sdk-for-android-explore-api-reference-latesttruckspecifications#trailerCount) is within this range.

### forbiddenHazardousGoods

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[HazardousMaterial](sdk-for-android-explore-api-reference-latesthazardousmaterial "enum class in com.here.sdk.transport")\> forbiddenHazardousGoods

    There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used for the route calculation provided using [`VehicleSpecification.hazardousMaterials`](sdk-for-android-explore-api-reference-latestvehiclespecification#hazardousMaterials) from [`TransportSpecification.vehicleSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification#vehicleSpecification) from [`RoutingOptions.transportSpecification`](sdk-for-android-explore-api-reference-latestroutingoptions#transportSpecification). This property is the intersection of the two lists.

    **Note** `RoadSignWarning` events and `RouteViolations` are only given for violations that are indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.

### maxTunnelCategory

@Nullable public [TunnelCategory](sdk-for-android-explore-api-reference-latesttunnelcategory "enum class in com.here.sdk.transport") maxTunnelCategory

    Tunnel category to restrict transport of specific goods during the trip. This property will be set if the [`VehicleSpecification.tunnelCategory`](sdk-for-android-explore-api-reference-latestvehiclespecification#tunnelCategory) from [`TransportSpecification.vehicleSpecification`](sdk-for-android-explore-api-reference-latesttransportspecification#vehicleSpecification) from [`RoutingOptions.transportSpecification`](sdk-for-android-explore-api-reference-latestroutingoptions#transportSpecification) exceeds this value.

### forbiddenTruckType

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @Nullable public [TruckType](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport") forbiddenTruckType

    Deprecated.
Will be removed in v4.27.0. Use `forbidden_truck_category` instead.

This property will be set if a restriction applies to the value of [`TruckType`](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport") parameter used for route calculation.

### forbiddenTruckCategory

@Nullable public [TruckCategory](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport") forbiddenTruckCategory

    This property will be set if a restriction applies to the value of [`TruckCategory`](sdk-for-android-explore-api-reference-latesttruckcategory "enum class in com.here.sdk.transport") parameter used for route calculation.

### forbiddenTruckRoadTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TruckRoadType](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport")\> forbiddenTruckRoadTypes

    Contains violated restrictions for truck road types.

### routingZoneReference

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) routingZoneReference

    Contains the restricted routing zone reference This property will be set if the [`AvoidanceOptions.zoneCategories`](sdk-for-android-explore-api-reference-latestavoidanceoptions#zoneCategories) is not empty

### maxPayloadCapacityInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxPayloadCapacityInKilograms

    Max permitted payload capacity during the trip, in kilograms. This property will be set if the [`TruckSpecifications.payloadCapacityInKilograms`](sdk-for-android-explore-api-reference-latesttruckspecifications#payloadCapacityInKilograms) exceeds this value.

### timeRule

@Nullable public [TimeRule](sdk-for-android-explore-api-reference-latesttimerule "class in com.here.sdk.core") timeRule

    Time intervals during which restrictions are enforced.

### maxWeight

@Nullable public [VehicleRestrictionMaxWeight](sdk-for-android-explore-api-reference-latestvehiclerestrictionmaxweight "class in com.here.sdk.routing") maxWeight

    Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction. This property will be set if the [`TruckSpecifications.grossWeightInKilograms`](sdk-for-android-explore-api-reference-latesttruckspecifications#grossWeightInKilograms) parameter used for route calculation exceeds this value.

### maxNumberOfTires

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxNumberOfTires

    Contains the maximum permitted number of tires. This property will be set if the [`VehicleSpecification.tiresCount`](sdk-for-android-explore-api-reference-latestvehiclespecification#tiresCount) exceeds the specified value.

### maxKingpinToRearAxleDistanceInCentimeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) maxKingpinToRearAxleDistanceInCentimeters

    Contains the maximum permitted distance from kingpin to the rear axle in centimeters. This property will be set if the [`VehicleSpecification.kingpinToRearAxleDistanceInCentimeters`](sdk-for-android-explore-api-reference-latestvehiclespecification#kingpinToRearAxleDistanceInCentimeters) exceeds the specified value.

## Constructor Details

  - ()" class="section detail">

### Details

public Details()

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
