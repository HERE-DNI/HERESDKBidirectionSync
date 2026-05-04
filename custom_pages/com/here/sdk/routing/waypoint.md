---
title: "Waypoint (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestwaypoint"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Waypoint

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.Waypoint
------------------------------------------------------------------------
public final class Waypoint extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a waypoint, used as input for route calculation.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [`ChargingStop`](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing")

  [chargingStop](#chargingStop)

Specifies of a user-planned charging stop.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [coordinates](#coordinates)

The waypoint's geographic coordinates.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [currentWeightChangeInKilograms](#currentWeightChangeInKilograms)

Changes the value of `vehicle[currentWeight]` by this value.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [displayLocation](#displayLocation)

Optional coordinates to indicate physical location of the Points of Interest (PoI).

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [duration](#duration)

The duration in seconds that should be spent at a waypoint of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [headingInDegrees](#headingInDegrees)

Optional heading angle referenced by true North, clockwise specifying the direction of travel.

[`MatchSideOfStreet`](sdk-for-android-explore-api-reference-latestmatchsideofstreet "enum class in com.here.sdk.routing")

  [matchSideOfStreet](#matchSideOfStreet)

Specifies how the location set by [`sideOfStreetHint`](#sideOfStreetHint) should be handled.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [minCourseDistanceInMeters](#minCourseDistanceInMeters)

Optional distance in meters during which the user wants to avoid taking actions.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [nameHint](#nameHint)

Optional name hint causes the router to look for the place with the most similar name.

[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)

  [onRoadThresholdInMeters](#onRoadThresholdInMeters)

Optional threshold allows specifying a distance within which the waypoint could be considered as being on a highway/bridge/tunnel/sliproad.

[`SegmentReference`](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing")

  [segmentHint](#segmentHint)

Optional segment hint causes the router to try and match to the specified segment.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [sideOfStreetHint](#sideOfStreetHint)

Optional coordinates to indicate which side of the street should be used to reach the waypoint.

`int`

  [transitRadiusInMeters](#transitRadiusInMeters)

The maximum allowed distance from the waypoint that the calculated route may pass through.

[`WaypointType`](sdk-for-android-explore-api-reference-latestwaypointtype "enum class in com.here.sdk.routing")

  [type](#type)

Defines how a waypoint should be considered for route calculation.

## Constructor Summary

Constructors

Constructor

  Description

  [Waypoint](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates)`

Creates a new instance.

[Waypoint](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,com.here.time.Duration))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates, `[`WaypointType`](sdk-for-android-explore-api-reference-latestwaypointtype "enum class in com.here.sdk.routing")` type, int transitRadiusInMeters, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` headingInDegrees, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` sideOfStreetHint, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` minCourseDistanceInMeters, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

Creates a new instance.

[Waypoint](#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,java.lang.String,com.here.time.Duration))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates, `[`WaypointType`](sdk-for-android-explore-api-reference-latestwaypointtype "enum class in com.here.sdk.routing")` type, int transitRadiusInMeters, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` headingInDegrees, `[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` sideOfStreetHint, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` minCourseDistanceInMeters, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` nameHint, `[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")` duration)`

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

### coordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates

    The waypoint's geographic coordinates.

### type

@NonNull public [WaypointType](sdk-for-android-explore-api-reference-latestwaypointtype "enum class in com.here.sdk.routing") type

    Defines how a waypoint should be considered for route calculation. The default waypoint type is [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

### transitRadiusInMeters

public int transitRadiusInMeters

    The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that [`sideOfStreetHint`](#sideOfStreetHint) option is ignored if the user sets this option with a value greater than zero.

### headingInDegrees

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) headingInDegrees

    Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when `null` is set, heading is ignored for route calculation.

### sideOfStreetHint

@Nullable public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") sideOfStreetHint

    Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets [`transitRadiusInMeters`](#transitRadiusInMeters) option with a value greater than zero.

### displayLocation

@Nullable public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") displayLocation

    Optional coordinates to indicate physical location of the Points of Interest (PoI). It is different from coordinates and [`sideOfStreetHint`](#sideOfStreetHint) which are generally expected to to be on the navigable road network and can be different from actual location of the PoI. display_location is used for visualization of the PoI regardless of road network.

### minCourseDistanceInMeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) minCourseDistanceInMeters

    Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.

### nameHint

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) nameHint

    Optional name hint causes the router to look for the place with the most similar name. This can e.g. include things like: `North` being used to differentiate between interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly select a residential street.

### matchSideOfStreet

@Nullable public [MatchSideOfStreet](sdk-for-android-explore-api-reference-latestmatchsideofstreet "enum class in com.here.sdk.routing") matchSideOfStreet

    Specifies how the location set by [`sideOfStreetHint`](#sideOfStreetHint) should be handled. Note that this setting might affect the geometry of the resulting route.

### duration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration

    The duration in seconds that should be spent at a waypoint of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER). Impacts time-aware calculations. Ignored for waypoints of type [`WaypointType.PASS_THROUGH`](sdk-for-android-explore-api-reference-latestwaypointtype#PASS_THROUGH). The default duration is 0 seconds.

### segmentHint

@Nullable public [SegmentReference](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing") segmentHint

    Optional segment hint causes the router to try and match to the specified segment. Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint. This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. Only topology segment id and travel direction are used to define the segment hint

    **Note:** The feature is not supported by the `OfflineRoutingEngine`.

### onRoadThresholdInMeters

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) onRoadThresholdInMeters

    Optional threshold allows specifying a distance within which the waypoint could be considered as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching. Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.

### chargingStop

@Nullable public [ChargingStop](sdk-for-android-explore-api-reference-latestchargingstop "class in com.here.sdk.routing") chargingStop

    Specifies of a user-planned charging stop. The resulting `Route` may contain this waypoint as a `RoutePlace` with a non-null `ChargingStation` member when the provided specifications indicate that a stop is required to charge the EV battery. **Note:** If \[EVCarOptions.ensure_reachability\] is not set as `true` and \[ChargingStop.min_duration\] is not provided, route calculation may suggest a better charging stop instead of this stop.

### currentWeightChangeInKilograms

@Nullable public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) currentWeightChangeInKilograms

    Changes the value of `vehicle[currentWeight]` by this value. Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route. Changes to the configuration of the vehicle, such as adding a trailer, aren't supported. Relative value in kilograms. Available range: from -40000 to 40000 (inclusive). **Note:**

    - A route request with this parameter requires to set [`VehicleSpecification.currentWeightInKilograms`](sdk-for-android-explore-api-reference-latestvehiclespecification#currentWeightInKilograms) and [`VehicleSpecification.grossWeightInKilograms`](sdk-for-android-explore-api-reference-latestvehiclespecification#grossWeightInKilograms).
    - This feature is supported in transport modes of [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TAXI`](sdk-for-android-explore-api-reference-latesttransportmode#TAXI), or [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK).

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Constructor Details

  - (com.here.sdk.core.GeoCoordinates)" class="section detail">

### Waypoint

public Waypoint(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates)

    Creates a new instance.
Parameters:
    `coordinates` -

    The waypoint's geographic coordinates.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,com.here.time.Duration)" class="section detail">

### Waypoint

public Waypoint(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [WaypointType](sdk-for-android-explore-api-reference-latestwaypointtype "enum class in com.here.sdk.routing") type, int transitRadiusInMeters, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) headingInDegrees, @Nullable [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") sideOfStreetHint, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) minCourseDistanceInMeters, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Creates a new instance.
Parameters:
    `coordinates` -

    The waypoint's geographic coordinates.

    `type` -

    Defines how a waypoint should be considered for route calculation. The default waypoint type is [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `transitRadiusInMeters` -

    The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that [`sideOfStreetHint`](#sideOfStreetHint) option is ignored if the user sets this option with a value greater than zero.

    `headingInDegrees` -

    Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when `null` is set, heading is ignored for route calculation.

    `sideOfStreetHint` -

    Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets [`transitRadiusInMeters`](#transitRadiusInMeters) option with a value greater than zero.

    `minCourseDistanceInMeters` -

    Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.

    `duration` -

    The duration in seconds that should be spent at a waypoint of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER). Impacts time-aware calculations. Ignored for waypoints of type [`WaypointType.PASS_THROUGH`](sdk-for-android-explore-api-reference-latestwaypointtype#PASS_THROUGH). The default duration is 0 seconds.
- (com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,java.lang.String,com.here.time.Duration)" class="section detail">

### Waypoint

public Waypoint(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates, @NonNull [WaypointType](sdk-for-android-explore-api-reference-latestwaypointtype "enum class in com.here.sdk.routing") type, int transitRadiusInMeters, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) headingInDegrees, @Nullable [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") sideOfStreetHint, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) minCourseDistanceInMeters, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) nameHint, @NonNull [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") duration)

    Creates a new instance.
Parameters:
    `coordinates` -

    The waypoint's geographic coordinates.

    `type` -

    Defines how a waypoint should be considered for route calculation. The default waypoint type is [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `transitRadiusInMeters` -

    The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that [`sideOfStreetHint`](#sideOfStreetHint) option is ignored if the user sets this option with a value greater than zero.

    `headingInDegrees` -

    Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when `null` is set, heading is ignored for route calculation.

    `sideOfStreetHint` -

    Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets [`transitRadiusInMeters`](#transitRadiusInMeters) option with a value greater than zero.

    `minCourseDistanceInMeters` -

    Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.

    `nameHint` -

    Optional name hint causes the router to look for the place with the most similar name. This can e.g. include things like: `North` being used to differentiate between interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly select a residential street.

    `duration` -

    The duration in seconds that should be spent at a waypoint of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER). Impacts time-aware calculations. Ignored for waypoints of type [`WaypointType.PASS_THROUGH`](sdk-for-android-explore-api-reference-latestwaypointtype#PASS_THROUGH). The default duration is 0 seconds.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
