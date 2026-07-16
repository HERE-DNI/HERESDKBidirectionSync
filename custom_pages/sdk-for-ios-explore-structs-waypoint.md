---
title: "Waypoint Structure Reference"
slug: "sdk-for-ios-explore-structs-waypoint"
---

# Waypoint

<div class="declaration">

<div class="language">

``` highlight
public struct Waypoint : Hashable
```

</div>

</div>

Represents a waypoint, used as input for route calculation.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV11coordinatesAA14GeoCoordinatesVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-coordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The waypoint’s geographic coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV4typeAA0B4TypeOvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV4typeAA0B4TypeOvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines how a waypoint should be considered for route calculation. The default waypoint type is <a href="sdk-for-ios-explore-enums-waypointtype#sdk-for-ios-explore-s-7heresdk12WaypointTypeO8stopoveryA2CmF">`WaypointType.stopover`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: WaypointType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-waypointtype">WaypointType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV21transitRadiusInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-transitRadiusInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV21transitRadiusInMeterss5Int32Vvp" class="token"><code>transitRadiusInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">`Waypoint.sideOfStreetHint`</a> option is ignored if the user sets this option with a value greater than zero.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transitRadiusInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV16headingInDegreesSdSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-headingInDegrees" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV16headingInDegreesSdSgvp" class="token"><code>headingInDegrees</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when `nil` is set, heading is ignored for route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var headingInDegrees: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-sideOfStreetHint" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp" class="token"><code>sideOfStreetHint</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV21transitRadiusInMeterss5Int32Vvp">`Waypoint.transitRadiusInMeters`</a> option with a value greater than zero.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sideOfStreetHint: GeoCoordinates?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV15displayLocationAA14GeoCoordinatesVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-displayLocation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV15displayLocationAA14GeoCoordinatesVSgvp" class="token"><code>displayLocation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional coordinates to indicate physical location of the Points of Interest (PoI). It is different from coordinates and <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">`Waypoint.sideOfStreetHint`</a> which are generally expected to to be on the navigable road network and can be different from actual location of the PoI. display_location is used for visualization of the PoI regardless of road network.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var displayLocation: GeoCoordinates?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV25minCourseDistanceInMeterss5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-minCourseDistanceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV25minCourseDistanceInMeterss5Int32VSgvp" class="token"><code>minCourseDistanceInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var minCourseDistanceInMeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV8nameHintSSSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-nameHint" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV8nameHintSSSgvp" class="token"><code>nameHint</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional name hint causes the router to look for the place with the most similar name. This can e.g. include things like: `North` being used to differentiate between interstates `I66 North` and `I66 South, Downtown Avenue` being used to correctly select a residential street.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var nameHint: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV17matchSideOfStreetAA05MatchdeF0OSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-matchSideOfStreet" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV17matchSideOfStreetAA05MatchdeF0OSgvp" class="token"><code>matchSideOfStreet</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies how the location set by <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">`Waypoint.sideOfStreetHint`</a> should be handled. Note that this setting might affect the geometry of the resulting route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var matchSideOfStreet: MatchSideOfStreet?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-matchsideofstreet">MatchSideOfStreet</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV8durationSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-duration" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV8durationSdvp" class="token"><code>duration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-ios-explore-enums-waypointtype#sdk-for-ios-explore-s-7heresdk12WaypointTypeO8stopoveryA2CmF">`WaypointType.stopover`</a>. Impacts time-aware calculations. Ignored for waypoints of type <a href="sdk-for-ios-explore-enums-waypointtype#sdk-for-ios-explore-s-7heresdk12WaypointTypeO11passThroughyA2CmF">`WaypointType.passThrough`</a>. The default duration is 0 seconds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var duration: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV11segmentHintAA16SegmentReferenceVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-segmentHint" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV11segmentHintAA16SegmentReferenceVSgvp" class="token"><code>segmentHint</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional segment hint causes the router to try and match to the specified segment. Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint. This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. Only topology segment id and travel direction are used to define the segment hint

  **Note:** The feature is not supported by the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentHint: SegmentReference?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-segmentreference">SegmentReference</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV23onRoadThresholdInMeterss5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-onRoadThresholdInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV23onRoadThresholdInMeterss5Int32VSgvp" class="token"><code>onRoadThresholdInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional threshold allows specifying a distance within which the waypoint could be considered as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching. Outside the threshold only segments which aren’t one of highway/bridge/tunnel/sliproad can be matched.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var onRoadThresholdInMeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV12chargingStopAA08ChargingD0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-chargingStop" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV12chargingStopAA08ChargingD0VSgvp" class="token"><code>chargingStop</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies of a user-planned charging stop. The resulting <a href="sdk-for-ios-explore-classes-route">`Route`</a> may contain this waypoint as a <a href="sdk-for-ios-explore-structs-routeplace">`RoutePlace`</a> with a non-null <a href="sdk-for-ios-explore-structs-chargingstation">`ChargingStation`</a> member when the provided specifications indicate that a stop is required to charge the EV battery. **Note:** If \[EVCarOptions.ensure_reachability\] is not set as `true` and \[ChargingStop.min_duration\] is not provided, route calculation may suggest a better charging stop instead of this stop.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargingStop: ChargingStop?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-chargingstop">ChargingStop</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV30currentWeightChangeInKilogramss5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-currentWeightChangeInKilograms" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV30currentWeightChangeInKilogramss5Int32VSgvp" class="token"><code>currentWeightChangeInKilograms</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Changes the value of `vehicle[currentWeight]` by this value. Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route. Changes to the configuration of the vehicle, such as adding a trailer, aren’t supported. Relative value in kilograms. Available range: from -40000 to 40000 (inclusive). **Note:**

  - A route request with this parameter requires to set <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">`VehicleSpecification.currentWeightInKilograms`</a> and <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a>.
  - This feature is supported in transport modes of <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a>, or <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var currentWeightChangeInKilograms: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8WaypointV11coordinates4type21transitRadiusInMeters07headingG7Degrees16sideOfStreetHint15displayLocation017minCourseDistancegH004nameN009matchSidelM08duration07segmentN0015onRoadThresholdgH012chargingStop019currentWeightChangeG9KilogramsAcA14GeoCoordinatesV_AA0B4TypeOs5Int32VSdSgASSgAyWSgSSSgAA05MatchvlM0OSgSdAA16SegmentReferenceVSgAzA12ChargingStopVSgAZtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-coordinates-type-transitRadiusInMeters-headingInDegrees-sideOfStreetHint-displayLocation-minCourseDistanceInMeters-nameHint-matchSideOfStreet-duration-segmentHint-onRoadThresholdInMeters-chargingStop-currentWeightChangeInKilograms" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV11coordinates4type21transitRadiusInMeters07headingG7Degrees16sideOfStreetHint15displayLocation017minCourseDistancegH004nameN009matchSidelM08duration07segmentN0015onRoadThresholdgH012chargingStop019currentWeightChangeG9KilogramsAcA14GeoCoordinatesV_AA0B4TypeOs5Int32VSdSgASSgAyWSgSSSgAA05MatchvlM0OSgSdAA16SegmentReferenceVSgAzA12ChargingStopVSgAZtcfc" class="token"><code>init(coordinates:</code><wbr></wbr><code>type:</code><wbr></wbr><code>transitRadiusInMeters:</code><wbr></wbr><code>headingInDegrees:</code><wbr></wbr><code>sideOfStreetHint:</code><wbr></wbr><code>displayLocation:</code><wbr></wbr><code>minCourseDistanceInMeters:</code><wbr></wbr><code>nameHint:</code><wbr></wbr><code>matchSideOfStreet:</code><wbr></wbr><code>duration:</code><wbr></wbr><code>segmentHint:</code><wbr></wbr><code>onRoadThresholdInMeters:</code><wbr></wbr><code>chargingStop:</code><wbr></wbr><code>currentWeightChangeInKilograms:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - coordinates: The waypoint’s geographic coordinates.
    - type: Defines how a waypoint should be considered for route calculation. The default waypoint type is <a href="sdk-for-ios-explore-enums-waypointtype#sdk-for-ios-explore-s-7heresdk12WaypointTypeO8stopoveryA2CmF">`WaypointType.stopover`</a>.
    - transitRadiusInMeters: The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">`Waypoint.sideOfStreetHint`</a> option is ignored if the user sets this option with a value greater than zero.
    - headingInDegrees: Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when `nil` is set, heading is ignored for route calculation.
    - sideOfStreetHint: Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV21transitRadiusInMeterss5Int32Vvp">`Waypoint.transitRadiusInMeters`</a> option with a value greater than zero.
    - displayLocation: Optional coordinates to indicate physical location of the Points of Interest (PoI). It is different from coordinates and <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">`Waypoint.sideOfStreetHint`</a> which are generally expected to to be on the navigable road network and can be different from actual location of the PoI. display_location is used for visualization of the PoI regardless of road network.
    - minCourseDistanceInMeters: Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.
    - nameHint: Optional name hint causes the router to look for the place with the most similar name. This can e.g. include things like: `North` being used to differentiate between interstates `I66 North` and `I66 South, Downtown Avenue` being used to correctly select a residential street.
    - matchSideOfStreet: Specifies how the location set by <a href="sdk-for-ios-explore-structs-waypoint#sdk-for-ios-explore-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">`Waypoint.sideOfStreetHint`</a> should be handled. Note that this setting might affect the geometry of the resulting route.
    - duration: The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-ios-explore-enums-waypointtype#sdk-for-ios-explore-s-7heresdk12WaypointTypeO8stopoveryA2CmF">`WaypointType.stopover`</a>. Impacts time-aware calculations. Ignored for waypoints of type <a href="sdk-for-ios-explore-enums-waypointtype#sdk-for-ios-explore-s-7heresdk12WaypointTypeO11passThroughyA2CmF">`WaypointType.passThrough`</a>. The default duration is 0 seconds.
    - segmentHint: Optional segment hint causes the router to try and match to the specified segment. Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint. This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. Only topology segment id and travel direction are used to define the segment hint

    **Note:** The feature is not supported by the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a>.

    - onRoadThresholdInMeters: Optional threshold allows specifying a distance within which the waypoint could be considered as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching. Outside the threshold only segments which aren’t one of highway/bridge/tunnel/sliproad can be matched.
    - chargingStop: Specifies of a user-planned charging stop. The resulting <a href="sdk-for-ios-explore-classes-route">`Route`</a> may contain this waypoint as a <a href="sdk-for-ios-explore-structs-routeplace">`RoutePlace`</a> with a non-null <a href="sdk-for-ios-explore-structs-chargingstation">`ChargingStation`</a> member when the provided specifications indicate that a stop is required to charge the EV battery. **Note:** If \[EVCarOptions.ensure_reachability\] is not set as `true` and \[ChargingStop.min_duration\] is not provided, route calculation may suggest a better charging stop instead of this stop.
    - currentWeightChangeInKilograms: Changes the value of `vehicle[currentWeight]` by this value. Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route. Changes to the configuration of the vehicle, such as adding a trailer, aren’t supported. Relative value in kilograms. Available range: from -40000 to 40000 (inclusive). **Note:**
      - A route request with this parameter requires to set <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">`VehicleSpecification.currentWeightInKilograms`</a> and <a href="sdk-for-ios-explore-structs-vehiclespecification#sdk-for-ios-explore-s-7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">`VehicleSpecification.grossWeightInKilograms`</a>.
      - This feature is supported in transport modes of <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO3caryA2CmF">`TransportMode.car`</a>, <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a>, or <a href="sdk-for-ios-explore-enums-transportmode#sdk-for-ios-explore-s-7heresdk13TransportModeO5truckyA2CmF">`TransportMode.truck`</a>.

    **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(coordinates: GeoCoordinates, type: WaypointType = WaypointType.stopover, transitRadiusInMeters: Int32 = 0, headingInDegrees: Double? = nil, sideOfStreetHint: GeoCoordinates? = nil, displayLocation: GeoCoordinates? = nil, minCourseDistanceInMeters: Int32? = nil, nameHint: String? = nil, matchSideOfStreet: MatchSideOfStreet? = nil, duration: TimeInterval = 0, segmentHint: SegmentReference? = nil, onRoadThresholdInMeters: Int32? = nil, chargingStop: ChargingStop? = nil, currentWeightChangeInKilograms: Int32? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-enums-waypointtype">WaypointType</a>
  - <a href="sdk-for-ios-explore-enums-matchsideofstreet">MatchSideOfStreet</a>
  - <a href="sdk-for-ios-explore-structs-segmentreference">SegmentReference</a>
  - <a href="sdk-for-ios-explore-structs-chargingstop">ChargingStop</a>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

