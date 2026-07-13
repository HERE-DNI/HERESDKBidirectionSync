---
title: "Waypoint class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-waypoint-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Waypoint-class-sidebar.html">

<div>

# <span class="kind-class">Waypoint</span> class

</div>

<div class="section desc markdown">

Represents a waypoint, used as input for route calculation.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-waypoint">Waypoint</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, \<a href="sdk-for-flutter-navigate-routing-waypointtype"></span><span id="sdk-for-flutter-navigate-param-type" class="parameter"><span class="type-annotation">[WaypointType</a></span> <span class="parameter-name">type</span> = <span class="default-value">WaypointType.stopover</span>, </span><span id="sdk-for-flutter-navigate-param-transitRadiusInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">transitRadiusInMeters</span> = <span class="default-value">0</span>, </span><span id="sdk-for-flutter-navigate-param-headingInDegrees" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">headingInDegrees</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-sideOfStreetHint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> <span class="parameter-name">sideOfStreetHint</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-displayLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> <span class="parameter-name">displayLocation</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-minCourseDistanceInMeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">minCourseDistanceInMeters</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-nameHint" class="parameter"><span class="type-annotation">String?</span> <span class="parameter-name">nameHint</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-matchSideOfStreet" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-matchsideofstreet">MatchSideOfStreet</a>?</span> <span class="parameter-name">matchSideOfStreet</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-duration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">duration</span> = <span class="default-value">const Duration(seconds: 0)</span>, </span><span id="sdk-for-flutter-navigate-param-segmentHint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a>?</span> <span class="parameter-name">segmentHint</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-onRoadThresholdInMeters" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">onRoadThresholdInMeters</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-chargingStop" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>?</span> <span class="parameter-name">chargingStop</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-currentWeightChangeInKilograms" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">currentWeightChangeInKilograms</span> = <span class="default-value">null</span></span>\])</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-waypoint-withdefaults">Waypoint.withDefaults</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withDefaults-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-chargingstop">chargingStop</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>?</span>  
Specifies of a user-planned charging stop. The resulting `Route` may contain this waypoint as a `RoutePlace` with a non-null `ChargingStation` member when the provided specifications indicate that a stop is required to charge the EV battery. **Note:** If `EVCarOptions.ensure_reachability` is not set as `true` and `ChargingStop.min_duration` is not provided, route calculation may suggest a better charging stop instead of this stop.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-coordinates">coordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
The waypoint's geographic coordinates.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-currentweightchangeinkilograms">currentWeightChangeInKilograms</a></span> <span class="signature">↔ int?</span>  
Changes the value of `vehicle[currentWeight]` by this value. Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route. Changes to the configuration of the vehicle, such as adding a trailer, aren't supported. Relative value in kilograms. Available range: from -40000 to 40000 (inclusive). **Note:**

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-displaylocation">displayLocation</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span>  
Optional coordinates to indicate physical location of the Points of Interest (PoI). It is different from coordinates and <a href="sdk-for-flutter-navigate-routing-waypoint-sideofstreethint">Waypoint.sideOfStreetHint</a> which are generally expected to to be on the navigable road network and can be different from actual location of the PoI. display_location is used for visualization of the PoI regardless of road network.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-duration">duration</a></span> <span class="signature">↔ Duration</span>  
The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-flutter-navigate-routing-waypointtype">WaypointType.stopover</a>. Impacts time-aware calculations. Ignored for waypoints of type <a href="sdk-for-flutter-navigate-routing-waypointtype">WaypointType.passThrough</a>. The default duration is 0 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-headingindegrees">headingInDegrees</a></span> <span class="signature">↔ double?</span>  
Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when `null` is set, heading is ignored for route calculation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-matchsideofstreet">matchSideOfStreet</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-matchsideofstreet">MatchSideOfStreet</a>?</span>  
Specifies how the location set by <a href="sdk-for-flutter-navigate-routing-waypoint-sideofstreethint">Waypoint.sideOfStreetHint</a> should be handled. Note that this setting might affect the geometry of the resulting route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-mincoursedistanceinmeters">minCourseDistanceInMeters</a></span> <span class="signature">↔ int?</span>  
Optional distance in meters during which the user wants to avoid taking actions. For example, if the origin is set by a moving vehicle, the user might not have time to react to immediate actions such as a sharp right turn.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-namehint">nameHint</a></span> <span class="signature">↔ String?</span>  
Optional name hint causes the router to look for the place with the most similar name. This can e.g. include things like: `North` being used to differentiate between interstates `I66 North` and `I66 South`, `Downtown Avenue` being used to correctly select a residential street.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-onroadthresholdinmeters">onRoadThresholdInMeters</a></span> <span class="signature">↔ int?</span>  
Optional threshold allows specifying a distance within which the waypoint could be considered as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching. Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-segmenthint">segmentHint</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a>?</span>  
Optional segment hint causes the router to try and match to the specified segment. Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint. This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one. Only topology segment id and travel direction are used to define the segment hint

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-sideofstreethint">sideOfStreetHint</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span>  
Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets <a href="sdk-for-flutter-navigate-routing-waypoint-transitradiusinmeters">Waypoint.transitRadiusInMeters</a> option with a value greater than zero.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-transitradiusinmeters">transitRadiusInMeters</a></span> <span class="signature">↔ int</span>  
The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that <a href="sdk-for-flutter-navigate-routing-waypoint-sideofstreethint">Waypoint.sideOfStreetHint</a> option is ignored if the user sets this option with a value greater than zero.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-waypointtype">WaypointType</a></span>  
Defines how a waypoint should be considered for route calculation. The default waypoint type is <a href="sdk-for-flutter-navigate-routing-waypointtype">WaypointType.stopover</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-waypoint-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

