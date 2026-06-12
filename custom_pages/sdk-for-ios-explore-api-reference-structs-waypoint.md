---
title: "Waypoint"
slug: "sdk-for-ios-explore-api-reference-structs-waypoint"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Waypoint"></a>
<a title="Waypoint Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        Waypoint Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Waypoint</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Waypoint</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a waypoint, used as input for route calculation.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk8WaypointV11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The waypoint’s geographic coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV4typeAA0B4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk8WaypointV4typeAA0B4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines how a waypoint should be considered for route calculation.
The default waypoint type is <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-waypointtype">WaypointType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV21transitRadiusInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transitRadiusInMeters"></a>
<a class="token" href="#/s:7heresdk8WaypointV21transitRadiusInMeterss5Int32Vvp">transitRadiusInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maximum allowed distance from the waypoint that the calculated
route may pass through. For example, to drive past a city without necessarily going
into the city center, you can specify the coordinates of the center and a transit
radius of 5000m. The default transit radius is zero.
If the route should pass the waypoint as close as possible, the default value
should be kept. Note that the waypoint will be map-matched to a road.
Non-zero values allow a greater tolerance.
Note that <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> option is ignored if the user sets this option with a value
greater than zero.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transitRadiusInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV16headingInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/headingInDegrees"></a>
<a class="token" href="#/s:7heresdk8WaypointV16headingInDegreesSdSgvp">headingInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional heading angle referenced by true North, clockwise specifying
the direction of travel. The heading direction may help the routing algorithm to select
the best direction, for example, when multiple directions are possible at a road junction.
North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees.
The value must be in the range [0, 360] when specified. By default, or when <code>nil</code> is set,
heading is ignored for route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">headingInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sideOfStreetHint"></a>
<a class="token" href="#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">sideOfStreetHint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional coordinates to indicate which side of the street should be used to reach the waypoint.
For example, if the location is to the left of the street, the router will prefer using that side
in case the street has dividers.
Note that this option is ignored if the user sets <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV21transitRadiusInMeterss5Int32Vvp">Waypoint.transitRadiusInMeters</a></code> option with a
value greater than zero.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sideOfStreetHint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV15displayLocationAA14GeoCoordinatesVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/displayLocation"></a>
<a class="token" href="#/s:7heresdk8WaypointV15displayLocationAA14GeoCoordinatesVSgvp">displayLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional coordinates to indicate physical location of the Points of Interest (PoI).
It is different from coordinates and <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> which are generally expected to to be
on the navigable road network and can be different from actual location of the PoI.
display_location is used for visualization of the PoI regardless of road network.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">displayLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV25minCourseDistanceInMeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minCourseDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk8WaypointV25minCourseDistanceInMeterss5Int32VSgvp">minCourseDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional distance in meters during which the user wants to avoid taking actions. For example, if
the origin is set by a moving vehicle, the user might not have time to react to immediate actions such
as a sharp right turn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minCourseDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV8nameHintSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/nameHint"></a>
<a class="token" href="#/s:7heresdk8WaypointV8nameHintSSSgvp">nameHint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional name hint causes the router to look for the place with the most similar name.
This can e.g. include things like: <code>North</code> being used to differentiate between
interstates <code>I66 North</code> and <code>I66 South</code>, <code>Downtown Avenue</code> being used to correctly
select a residential street.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">nameHint</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV17matchSideOfStreetAA05MatchdeF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/matchSideOfStreet"></a>
<a class="token" href="#/s:7heresdk8WaypointV17matchSideOfStreetAA05MatchdeF0OSgvp">matchSideOfStreet</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies how the location set by <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> should be handled. Note that this setting might affect the geometry of the resulting route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">matchSideOfStreet</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-matchsideofstreet">MatchSideOfStreet</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV8durationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk8WaypointV8durationSdvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The duration in seconds that should be spent at a waypoint of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>.
Impacts time-aware calculations.
Ignored for waypoints of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO11passThroughyA2CmF">WaypointType.passThrough</a></code>.
The default duration is 0 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV11segmentHintAA16SegmentReferenceVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentHint"></a>
<a class="token" href="#/s:7heresdk8WaypointV11segmentHintAA16SegmentReferenceVSgvp">segmentHint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional segment hint causes the router to try and match to the specified segment.
Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint.
This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one.
Only topology segment id and travel direction are used to define the segment hint</p>
<p><strong>Note:</strong>
The feature is not supported by the <code>OfflineRoutingEngine</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentHint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-segmentreference">SegmentReference</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV23onRoadThresholdInMeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/onRoadThresholdInMeters"></a>
<a class="token" href="#/s:7heresdk8WaypointV23onRoadThresholdInMeterss5Int32VSgvp">onRoadThresholdInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional threshold allows specifying a distance within which the waypoint could be considered
as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching.
Outside the threshold only segments which aren’t one of highway/bridge/tunnel/sliproad can be matched.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">onRoadThresholdInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV12chargingStopAA08ChargingD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargingStop"></a>
<a class="token" href="#/s:7heresdk8WaypointV12chargingStopAA08ChargingD0VSgvp">chargingStop</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies of a user-planned charging stop.
The resulting <code><a href="sdk-for-ios-explore-api-reference-classes-route">Route</a></code> may contain this waypoint as a <code><a href="sdk-for-ios-explore-api-reference-structs-routeplace">RoutePlace</a></code> with a non-null <code><a href="sdk-for-ios-explore-api-reference-structs-chargingstation">ChargingStation</a></code> member
when the provided specifications indicate that a stop is required to charge the EV battery.
<strong>Note:</strong>
If [EVCarOptions.ensure_reachability] is not set as <code>true</code> and [ChargingStop.min_duration] is not provided,
route calculation may suggest a better charging stop instead of this stop.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">chargingStop</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-chargingstop">ChargingStop</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV30currentWeightChangeInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentWeightChangeInKilograms"></a>
<a class="token" href="#/s:7heresdk8WaypointV30currentWeightChangeInKilogramss5Int32VSgvp">currentWeightChangeInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Changes the value of <code>vehicle[currentWeight]</code> by this value.
Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route.
Changes to the configuration of the vehicle, such as adding a trailer, aren’t supported.
Relative value in kilograms. Available range: from -40000 to 40000 (inclusive).
<strong>Note:</strong></p>
<ul>
<li>A route request with this parameter requires to set <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code> and
<code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>.</li>
<li>This feature is supported in transport modes of <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code>, or
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">currentWeightChangeInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8WaypointV11coordinates4type21transitRadiusInMeters07headingG7Degrees16sideOfStreetHint15displayLocation017minCourseDistancegH004nameN009matchSidelM08duration07segmentN0015onRoadThresholdgH012chargingStop019currentWeightChangeG9KilogramsAcA14GeoCoordinatesV_AA0B4TypeOs5Int32VSdSgASSgAyWSgSSSgAA05MatchvlM0OSgSdAA16SegmentReferenceVSgAzA12ChargingStopVSgAZtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(coordinates:type:transitRadiusInMeters:headingInDegrees:sideOfStreetHint:displayLocation:minCourseDistanceInMeters:nameHint:matchSideOfStreet:duration:segmentHint:onRoadThresholdInMeters:chargingStop:currentWeightChangeInKilograms:)"></a>
<a class="token" href="#/s:7heresdk8WaypointV11coordinates4type21transitRadiusInMeters07headingG7Degrees16sideOfStreetHint15displayLocation017minCourseDistancegH004nameN009matchSidelM08duration07segmentN0015onRoadThresholdgH012chargingStop019currentWeightChangeG9KilogramsAcA14GeoCoordinatesV_AA0B4TypeOs5Int32VSdSgASSgAyWSgSSSgAA05MatchvlM0OSgSdAA16SegmentReferenceVSgAzA12ChargingStopVSgAZtcfc">init(coordinates:<wbr/>type:<wbr/>transitRadiusInMeters:<wbr/>headingInDegrees:<wbr/>sideOfStreetHint:<wbr/>displayLocation:<wbr/>minCourseDistanceInMeters:<wbr/>nameHint:<wbr/>matchSideOfStreet:<wbr/>duration:<wbr/>segmentHint:<wbr/>onRoadThresholdInMeters:<wbr/>chargingStop:<wbr/>currentWeightChangeInKilograms:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>coordinates: The waypoint’s geographic coordinates.</li>
<li>type: Defines how a waypoint should be considered for route calculation.
The default waypoint type is <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>.</li>
<li>transitRadiusInMeters: The maximum allowed distance from the waypoint that the calculated
route may pass through. For example, to drive past a city without necessarily going
into the city center, you can specify the coordinates of the center and a transit
radius of 5000m. The default transit radius is zero.
If the route should pass the waypoint as close as possible, the default value
should be kept. Note that the waypoint will be map-matched to a road.
Non-zero values allow a greater tolerance.
Note that <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> option is ignored if the user sets this option with a value
greater than zero.</li>
<li>headingInDegrees: Optional heading angle referenced by true North, clockwise specifying
the direction of travel. The heading direction may help the routing algorithm to select
the best direction, for example, when multiple directions are possible at a road junction.
North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees.
The value must be in the range [0, 360] when specified. By default, or when <code>nil</code> is set,
heading is ignored for route calculation.</li>
<li>sideOfStreetHint: Optional coordinates to indicate which side of the street should be used to reach the waypoint.
For example, if the location is to the left of the street, the router will prefer using that side
in case the street has dividers.
Note that this option is ignored if the user sets <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV21transitRadiusInMeterss5Int32Vvp">Waypoint.transitRadiusInMeters</a></code> option with a
value greater than zero.</li>
<li>displayLocation: Optional coordinates to indicate physical location of the Points of Interest (PoI).
It is different from coordinates and <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> which are generally expected to to be
on the navigable road network and can be different from actual location of the PoI.
display_location is used for visualization of the PoI regardless of road network.</li>
<li>minCourseDistanceInMeters: Optional distance in meters during which the user wants to avoid taking actions. For example, if
the origin is set by a moving vehicle, the user might not have time to react to immediate actions such
as a sharp right turn.</li>
<li>nameHint: Optional name hint causes the router to look for the place with the most similar name.
This can e.g. include things like: <code>North</code> being used to differentiate between
interstates <code>I66 North</code> and <code>I66 South</code>, <code>Downtown Avenue</code> being used to correctly
select a residential street.</li>
<li>matchSideOfStreet: Specifies how the location set by <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> should be handled. Note that this setting might affect the geometry of the resulting route.</li>
<li>duration: The duration in seconds that should be spent at a waypoint of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>.
Impacts time-aware calculations.
Ignored for waypoints of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO11passThroughyA2CmF">WaypointType.passThrough</a></code>.
The default duration is 0 seconds.</li>
<li>segmentHint: Optional segment hint causes the router to try and match to the specified segment.
Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint.
This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one.
Only topology segment id and travel direction are used to define the segment hint</li>
</ul>
<p><strong>Note:</strong>
  The feature is not supported by the <code>OfflineRoutingEngine</code>.</p>
<ul>
<li>onRoadThresholdInMeters: Optional threshold allows specifying a distance within which the waypoint could be considered
as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching.
Outside the threshold only segments which aren’t one of highway/bridge/tunnel/sliproad can be matched.</li>
<li>chargingStop: Specifies of a user-planned charging stop.
The resulting <code><a href="sdk-for-ios-explore-api-reference-classes-route">Route</a></code> may contain this waypoint as a <code><a href="sdk-for-ios-explore-api-reference-structs-routeplace">RoutePlace</a></code> with a non-null <code><a href="sdk-for-ios-explore-api-reference-structs-chargingstation">ChargingStation</a></code> member
when the provided specifications indicate that a stop is required to charge the EV battery.
<strong>Note:</strong>
If [EVCarOptions.ensure_reachability] is not set as <code>true</code> and [ChargingStop.min_duration] is not provided,
route calculation may suggest a better charging stop instead of this stop.</li>
<li>currentWeightChangeInKilograms: Changes the value of <code>vehicle[currentWeight]</code> by this value.
Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route.
Changes to the configuration of the vehicle, such as adding a trailer, aren’t supported.
Relative value in kilograms. Available range: from -40000 to 40000 (inclusive).
<strong>Note:</strong>
<ul>
<li>A route request with this parameter requires to set <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code> and
<code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>.</li>
<li>This feature is supported in transport modes of <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code>, or
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>.</li>
</ul></li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-waypointtype">WaypointType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-waypointtype">WaypointType</a></span><span class="o">.</span><span class="n">stopover</span><span class="p">,</span> <span class="nv">transitRadiusInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">headingInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">sideOfStreetHint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">displayLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">minCourseDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">nameHint</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">matchSideOfStreet</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-matchsideofstreet">MatchSideOfStreet</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">segmentHint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-segmentreference">SegmentReference</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">onRoadThresholdInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">chargingStop</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-chargingstop">ChargingStop</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">currentWeightChangeInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>
