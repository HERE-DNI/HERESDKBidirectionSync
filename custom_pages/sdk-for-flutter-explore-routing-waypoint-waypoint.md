---
title: "Waypoint constructor"
slug: "sdk-for-flutter-explore-routing-waypoint-waypoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Waypoint.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-waypoint-class</li>
<li class="self-crumb">Waypoint constructor</li>
</ol>
<div class="self-name">Waypoint</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>Waypoint constructor</h1></div>
<section class="multi-line-signature">
Waypoint(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-core-geocoordinates-class coordinates, [</li>
<li>/sdk-for-flutter-explore-routing-waypointtype type = WaypointType.stopover, </li>
<li>int transitRadiusInMeters = 0, </li>
<li>double? headingInDegrees = null, </li>
<li>/sdk-for-flutter-explore-core-geocoordinates-class? sideOfStreetHint = null, </li>
<li>/sdk-for-flutter-explore-core-geocoordinates-class? displayLocation = null, </li>
<li>int? minCourseDistanceInMeters = null, </li>
<li>String? nameHint = null, </li>
<li>/sdk-for-flutter-explore-routing-matchsideofstreet? matchSideOfStreet = null, </li>
<li>Duration duration = const Duration(seconds: 0), </li>
<li>/sdk-for-flutter-explore-routing-segmentreference-class? segmentHint = null, </li>
<li>int? onRoadThresholdInMeters = null, </li>
<li>/sdk-for-flutter-explore-routing-chargingstop-class? chargingStop = null, </li>
<li>int? currentWeightChangeInKilograms = null, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>coordinates</code> The waypoint's geographic coordinates.</li>
<li><code>type</code> Defines how a waypoint should be considered for route calculation.
The default waypoint type is /sdk-for-flutter-explore-routing-waypointtype.</li>
<li><code>transitRadiusInMeters</code> The maximum allowed distance from the waypoint that the calculated
route may pass through. For example, to drive past a city without necessarily going
into the city center, you can specify the coordinates of the center and a transit
radius of 5000m. The default transit radius is zero.
If the route should pass the waypoint as close as possible, the default value
should be kept. Note that the waypoint will be map-matched to a road.
Non-zero values allow a greater tolerance.
Note that /sdk-for-flutter-explore-routing-waypoint-sideofstreethint option is ignored if the user sets this option with a value
greater than zero.</li>
<li><code>headingInDegrees</code> Optional heading angle referenced by true North, clockwise specifying
the direction of travel. The heading direction may help the routing algorithm to select
the best direction, for example, when multiple directions are possible at a road junction.
North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees.
The value must be in the range [0, 360] when specified. By default, or when <code>null</code> is set,
heading is ignored for route calculation.</li>
<li><code>sideOfStreetHint</code> Optional coordinates to indicate which side of the street should be used to reach the waypoint.
For example, if the location is to the left of the street, the router will prefer using that side
in case the street has dividers.
Note that this option is ignored if the user sets /sdk-for-flutter-explore-routing-waypoint-transitradiusinmeters option with a
value greater than zero.</li>
<li><code>displayLocation</code> Optional coordinates to indicate physical location of the Points of Interest (PoI).
It is different from coordinates and /sdk-for-flutter-explore-routing-waypoint-sideofstreethint which are generally expected to to be
on the navigable road network and can be different from actual location of the PoI.
<code>display_location</code> is used for visualization of the PoI regardless of road network.</li>
<li><code>minCourseDistanceInMeters</code> Optional distance in meters during which the user wants to avoid taking actions. For example, if
the origin is set by a moving vehicle, the user might not have time to react to immediate actions such
as a sharp right turn.</li>
<li><code>nameHint</code> Optional name hint causes the router to look for the place with the most similar name.
This can e.g. include things like: <code>North</code> being used to differentiate between
interstates <code>I66 North</code> and <code>I66 South</code>, <code>Downtown Avenue</code> being used to correctly
select a residential street.</li>
<li><code>matchSideOfStreet</code> Specifies how the location set by /sdk-for-flutter-explore-routing-waypoint-sideofstreethint should be handled. Note that this setting might affect the geometry of the resulting route.</li>
<li><code>duration</code> The duration in seconds that should be spent at a waypoint of type /sdk-for-flutter-explore-routing-waypointtype.
Impacts time-aware calculations.
Ignored for waypoints of type /sdk-for-flutter-explore-routing-waypointtype.
The default duration is 0 seconds.</li>
<li><code>segmentHint</code> Optional segment hint causes the router to try and match to the specified segment.
Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint.
This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one.
Only topology segment id and travel direction are used to define the segment hint</li>
</ul>
<p><strong>Note:</strong>
The feature is not supported by the <code>OfflineRoutingEngine</code>.</p>
<ul>
<li><code>onRoadThresholdInMeters</code> Optional threshold allows specifying a distance within which the waypoint could be considered
as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching.
Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.</li>
<li><code>chargingStop</code> Specifies of a user-planned charging stop.
The resulting <code>Route</code> may contain this waypoint as a <code>RoutePlace</code> with a non-null <code>ChargingStation</code> member
when the provided specifications indicate that a stop is required to charge the EV battery.
<strong>Note:</strong>
If <code>EVCarOptions.ensure_reachability</code> is not set as <code>true</code> and <code>ChargingStop.min_duration</code> is not provided,
route calculation may suggest a better charging stop instead of this stop.</li>
<li><code>currentWeightChangeInKilograms</code> Changes the value of <code>vehicle[currentWeight]</code> by this value.
Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route.
Changes to the configuration of the vehicle, such as adding a trailer, aren't supported.
Relative value in kilograms. Available range: from -40000 to 40000 (inclusive).
<strong>Note:</strong></li>
</ul>
<ul>
<li>A route request with this parameter requires to set /sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms and
/sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms.</li>
<li>This feature is supported in transport modes of /sdk-for-flutter-explore-transport-transportmode, /sdk-for-flutter-explore-transport-transportmode, or
/sdk-for-flutter-explore-transport-transportmode.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Waypoint(GeoCoordinates coordinates, [WaypointType type = WaypointType.stopover, int transitRadiusInMeters = 0, double? headingInDegrees = null, GeoCoordinates? sideOfStreetHint = null, GeoCoordinates? displayLocation = null, int? minCourseDistanceInMeters = null, String? nameHint = null, MatchSideOfStreet? matchSideOfStreet = null, Duration duration = const Duration(seconds: 0), SegmentReference? segmentHint = null, int? onRoadThresholdInMeters = null, ChargingStop? chargingStop = null, int? currentWeightChangeInKilograms = null])
  : coordinates = coordinates, type = type, transitRadiusInMeters = transitRadiusInMeters, headingInDegrees = headingInDegrees, sideOfStreetHint = sideOfStreetHint, displayLocation = displayLocation, minCourseDistanceInMeters = minCourseDistanceInMeters, nameHint = nameHint, matchSideOfStreet = matchSideOfStreet, duration = duration, segmentHint = segmentHint ?? null, onRoadThresholdInMeters = onRoadThresholdInMeters, chargingStop = chargingStop ?? null, currentWeightChangeInKilograms = currentWeightChangeInKilograms;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-waypoint-class</li>
<li class="self-crumb">Waypoint constructor</li>
</ol>
<h5>Waypoint class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
