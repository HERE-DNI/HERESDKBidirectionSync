---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-waypoint-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Waypoint-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">Waypoint class</li>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Waypoint-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Waypoint class</h1></div>
<section class="desc markdown">
<p>Represents a waypoint, used as input for route calculation.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Waypoint">
/sdk-for-flutter-explore-routing-waypoint-waypoint(/sdk-for-flutter-explore-core-geocoordinates-class coordinates, [/sdk-for-flutter-explore-routing-waypointtype type = WaypointType.stopover, int transitRadiusInMeters = 0, double? headingInDegrees = null, /sdk-for-flutter-explore-core-geocoordinates-class? sideOfStreetHint = null, /sdk-for-flutter-explore-core-geocoordinates-class? displayLocation = null, int? minCourseDistanceInMeters = null, String? nameHint = null, /sdk-for-flutter-explore-routing-matchsideofstreet? matchSideOfStreet = null, Duration duration = const Duration(seconds: 0), /sdk-for-flutter-explore-routing-segmentreference-class? segmentHint = null, int? onRoadThresholdInMeters = null, /sdk-for-flutter-explore-routing-chargingstop-class? chargingStop = null, int? currentWeightChangeInKilograms = null])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="Waypoint.withDefaults">
/sdk-for-flutter-explore-routing-waypoint-waypoint-withdefaults(/sdk-for-flutter-explore-core-geocoordinates-class coordinates)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="chargingStop">
/sdk-for-flutter-explore-routing-waypoint-chargingstop
↔ /sdk-for-flutter-explore-routing-chargingstop-class?
</dt>
<dd>
  Specifies of a user-planned charging stop.
The resulting <code>Route</code> may contain this waypoint as a <code>RoutePlace</code> with a non-null <code>ChargingStation</code> member
when the provided specifications indicate that a stop is required to charge the EV battery.
<strong>Note:</strong>
If <code>EVCarOptions.ensure_reachability</code> is not set as <code>true</code> and <code>ChargingStop.min_duration</code> is not provided,
route calculation may suggest a better charging stop instead of this stop.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="coordinates">
/sdk-for-flutter-explore-routing-waypoint-coordinates
↔ /sdk-for-flutter-explore-core-geocoordinates-class
</dt>
<dd>
  The waypoint's geographic coordinates.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="currentWeightChangeInKilograms">
/sdk-for-flutter-explore-routing-waypoint-currentweightchangeinkilograms
↔ int?
</dt>
<dd>
  Changes the value of <code>vehicle[currentWeight]</code> by this value.
Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route.
Changes to the configuration of the vehicle, such as adding a trailer, aren't supported.
Relative value in kilograms. Available range: from -40000 to 40000 (inclusive).
<strong>Note:</strong>
<div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="displayLocation">
/sdk-for-flutter-explore-routing-waypoint-displaylocation
↔ /sdk-for-flutter-explore-core-geocoordinates-class?
</dt>
<dd>
  Optional coordinates to indicate physical location of the Points of Interest (PoI).
It is different from coordinates and /sdk-for-flutter-explore-routing-waypoint-sideofstreethint which are generally expected to to be
on the navigable road network and can be different from actual location of the PoI.
display_location is used for visualization of the PoI regardless of road network.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="duration">
/sdk-for-flutter-explore-routing-waypoint-duration
↔ Duration
</dt>
<dd>
  The duration in seconds that should be spent at a waypoint of type /sdk-for-flutter-explore-routing-waypointtype.
Impacts time-aware calculations.
Ignored for waypoints of type /sdk-for-flutter-explore-routing-waypointtype.
The default duration is 0 seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-waypoint-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="headingInDegrees">
/sdk-for-flutter-explore-routing-waypoint-headingindegrees
↔ double?
</dt>
<dd>
  Optional heading angle referenced by true North, clockwise specifying
the direction of travel. The heading direction may help the routing algorithm to select
the best direction, for example, when multiple directions are possible at a road junction.
North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees.
The value must be in the range [0, 360] when specified. By default, or when <code>null</code> is set,
heading is ignored for route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="matchSideOfStreet">
/sdk-for-flutter-explore-routing-waypoint-matchsideofstreet
↔ /sdk-for-flutter-explore-routing-matchsideofstreet?
</dt>
<dd>
  Specifies how the location set by /sdk-for-flutter-explore-routing-waypoint-sideofstreethint should be handled. Note that this setting might affect the geometry of the resulting route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minCourseDistanceInMeters">
/sdk-for-flutter-explore-routing-waypoint-mincoursedistanceinmeters
↔ int?
</dt>
<dd>
  Optional distance in meters during which the user wants to avoid taking actions. For example, if
the origin is set by a moving vehicle, the user might not have time to react to immediate actions such
as a sharp right turn.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="nameHint">
/sdk-for-flutter-explore-routing-waypoint-namehint
↔ String?
</dt>
<dd>
  Optional name hint causes the router to look for the place with the most similar name.
This can e.g. include things like: <code>North</code> being used to differentiate between
interstates <code>I66 North</code> and <code>I66 South</code>, <code>Downtown Avenue</code> being used to correctly
select a residential street.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="onRoadThresholdInMeters">
/sdk-for-flutter-explore-routing-waypoint-onroadthresholdinmeters
↔ int?
</dt>
<dd>
  Optional threshold allows specifying a distance within which the waypoint could be considered
as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching.
Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-waypoint-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segmentHint">
/sdk-for-flutter-explore-routing-waypoint-segmenthint
↔ /sdk-for-flutter-explore-routing-segmentreference-class?
</dt>
<dd>
  Optional segment hint causes the router to try and match to the specified segment.
Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint.
This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one.
Only topology segment id and travel direction are used to define the segment hint
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="sideOfStreetHint">
/sdk-for-flutter-explore-routing-waypoint-sideofstreethint
↔ /sdk-for-flutter-explore-core-geocoordinates-class?
</dt>
<dd>
  Optional coordinates to indicate which side of the street should be used to reach the waypoint.
For example, if the location is to the left of the street, the router will prefer using that side
in case the street has dividers.
Note that this option is ignored if the user sets /sdk-for-flutter-explore-routing-waypoint-transitradiusinmeters option with a
value greater than zero.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="transitRadiusInMeters">
/sdk-for-flutter-explore-routing-waypoint-transitradiusinmeters
↔ int
</dt>
<dd>
  The maximum allowed distance from the waypoint that the calculated
route may pass through. For example, to drive past a city without necessarily going
into the city center, you can specify the coordinates of the center and a transit
radius of 5000m. The default transit radius is zero.
If the route should pass the waypoint as close as possible, the default value
should be kept. Note that the waypoint will be map-matched to a road.
Non-zero values allow a greater tolerance.
Note that /sdk-for-flutter-explore-routing-waypoint-sideofstreethint option is ignored if the user sets this option with a value
greater than zero.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-explore-routing-waypoint-type
↔ /sdk-for-flutter-explore-routing-waypointtype
</dt>
<dd>
  Defines how a waypoint should be considered for route calculation.
The default waypoint type is /sdk-for-flutter-explore-routing-waypointtype.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-waypoint-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-waypoint-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-explore-routing-waypoint-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
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
<li class="self-crumb">Waypoint class</li>
</ol>
<h5>routing library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
