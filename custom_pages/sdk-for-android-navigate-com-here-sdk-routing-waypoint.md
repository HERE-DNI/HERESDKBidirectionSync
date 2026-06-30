---
title: "Waypoint (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-waypoint"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Waypoint.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.Waypoint</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Waypoint</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents a waypoint, used as input for route calculation.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstop" title="class in com.here.sdk.routing">ChargingStop</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#chargingStop">chargingStop</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies of a user-planned charging stop.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#coordinates">coordinates</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The waypoint's geographic coordinates.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#currentWeightChangeInKilograms">currentWeightChangeInKilograms</a></code></div>
<div class="col-last even-row-color">
<div class="block">Changes the value of <code>vehicle[currentWeight]</code> by this value.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#displayLocation">displayLocation</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional coordinates to indicate physical location of the Points of Interest (PoI).</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#duration">duration</a></code></div>
<div class="col-last even-row-color">
<div class="block">The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#headingInDegrees">headingInDegrees</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional heading angle referenced by true North, clockwise specifying
 the direction of travel.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-matchsideofstreet" title="enum class in com.here.sdk.routing">MatchSideOfStreet</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#matchSideOfStreet">matchSideOfStreet</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies how the location set by <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#sideOfStreetHint"><code>sideOfStreetHint</code></a> should be handled.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#minCourseDistanceInMeters">minCourseDistanceInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional distance in meters during which the user wants to avoid taking actions.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#nameHint">nameHint</a></code></div>
<div class="col-last even-row-color">
<div class="block">Optional name hint causes the router to look for the place with the most similar name.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#onRoadThresholdInMeters">onRoadThresholdInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional threshold allows specifying a distance within which the waypoint could be considered
 as being on a highway/bridge/tunnel/sliproad.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#segmentHint">segmentHint</a></code></div>
<div class="col-last even-row-color">
<div class="block">Optional segment hint causes the router to try and match to the specified segment.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#sideOfStreetHint">sideOfStreetHint</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional coordinates to indicate which side of the street should be used to reach the waypoint.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#transitRadiusInMeters">transitRadiusInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The maximum allowed distance from the waypoint that the calculated
 route may pass through.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype" title="enum class in com.here.sdk.routing">WaypointType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#type">type</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines how a waypoint should be considered for route calculation.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#%3Cinit%3E(com.here.sdk.core.GeoCoordinates)">Waypoint</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,com.here.time.Duration)">Waypoint</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype" title="enum class in com.here.sdk.routing">WaypointType</a> type,
 int transitRadiusInMeters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> headingInDegrees,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> sideOfStreetHint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> minCourseDistanceInMeters,
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,java.lang.String,com.here.time.Duration)">Waypoint</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype" title="enum class in com.here.sdk.routing">WaypointType</a> type,
 int transitRadiusInMeters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> headingInDegrees,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> sideOfStreetHint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> minCourseDistanceInMeters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> nameHint,
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="coordinates">
<h3>coordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">coordinates</span></div>
<div class="block"><p>The waypoint's geographic coordinates.</p></div>
</section>
</li>
<li>
<section class="detail" id="type">
<h3>type</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype" title="enum class in com.here.sdk.routing">WaypointType</a></span> <span class="element-name">type</span></div>
<div class="block"><p>Defines how a waypoint should be considered for route calculation.
 The default waypoint type is <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="transitRadiusInMeters">
<h3>transitRadiusInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">transitRadiusInMeters</span></div>
<div class="block"><p>The maximum allowed distance from the waypoint that the calculated
 route may pass through. For example, to drive past a city without necessarily going
 into the city center, you can specify the coordinates of the center and a transit
 radius of 5000m. The default transit radius is zero.
 If the route should pass the waypoint as close as possible, the default value
 should be kept. Note that the waypoint will be map-matched to a road.
 Non-zero values allow a greater tolerance.
 Note that <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#sideOfStreetHint"><code>sideOfStreetHint</code></a> option is ignored if the user sets this option with a value
 greater than zero.</p></div>
</section>
</li>
<li>
<section class="detail" id="headingInDegrees">
<h3>headingInDegrees</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">headingInDegrees</span></div>
<div class="block"><p>Optional heading angle referenced by true North, clockwise specifying
 the direction of travel. The heading direction may help the routing algorithm to select
 the best direction, for example, when multiple directions are possible at a road junction.
 North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees.
 The value must be in the range [0, 360] when specified. By default, or when <code>null</code> is set,
 heading is ignored for route calculation.</p></div>
</section>
</li>
<li>
<section class="detail" id="sideOfStreetHint">
<h3>sideOfStreetHint</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">sideOfStreetHint</span></div>
<div class="block"><p>Optional coordinates to indicate which side of the street should be used to reach the waypoint.
 For example, if the location is to the left of the street, the router will prefer using that side
 in case the street has dividers.
 Note that this option is ignored if the user sets <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#transitRadiusInMeters"><code>transitRadiusInMeters</code></a> option with a
 value greater than zero.</p></div>
</section>
</li>
<li>
<section class="detail" id="displayLocation">
<h3>displayLocation</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">displayLocation</span></div>
<div class="block"><p>Optional coordinates to indicate physical location of the Points of Interest (PoI).
 It is different from coordinates and <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#sideOfStreetHint"><code>sideOfStreetHint</code></a> which are generally expected to to be
 on the navigable road network and can be different from actual location of the PoI.
 display_location is used for visualization of the PoI regardless of road network.</p></div>
</section>
</li>
<li>
<section class="detail" id="minCourseDistanceInMeters">
<h3>minCourseDistanceInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">minCourseDistanceInMeters</span></div>
<div class="block"><p>Optional distance in meters during which the user wants to avoid taking actions. For example, if
 the origin is set by a moving vehicle, the user might not have time to react to immediate actions such
 as a sharp right turn.</p></div>
</section>
</li>
<li>
<section class="detail" id="nameHint">
<h3>nameHint</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">nameHint</span></div>
<div class="block"><p>Optional name hint causes the router to look for the place with the most similar name.
 This can e.g. include things like: <code>North</code> being used to differentiate between
 interstates <code>I66 North</code> and <code>I66 South</code>, <code>Downtown Avenue</code> being used to correctly
 select a residential street.</p></div>
</section>
</li>
<li>
<section class="detail" id="matchSideOfStreet">
<h3>matchSideOfStreet</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-matchsideofstreet" title="enum class in com.here.sdk.routing">MatchSideOfStreet</a></span> <span class="element-name">matchSideOfStreet</span></div>
<div class="block"><p>Specifies how the location set by <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#sideOfStreetHint"><code>sideOfStreetHint</code></a> should be handled. Note that this setting might affect the geometry of the resulting route.</p></div>
</section>
</li>
<li>
<section class="detail" id="duration">
<h3>duration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">duration</span></div>
<div class="block"><p>The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.
 Impacts time-aware calculations.
 Ignored for waypoints of type <a href="sdk-for-android-navigate-waypointtype#PASS_THROUGH"><code>WaypointType.PASS_THROUGH</code></a>.
 The default duration is 0 seconds.</p></div>
</section>
</li>
<li>
<section class="detail" id="segmentHint">
<h3>segmentHint</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">segmentHint</span></div>
<div class="block"><p>Optional segment hint causes the router to try and match to the specified segment.
 Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint.
 This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one.
 Only topology segment id and travel direction are used to define the segment hint
 <strong>Note:</strong>
 The feature is not supported by the <code>OfflineRoutingEngine</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="onRoadThresholdInMeters">
<h3>onRoadThresholdInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">onRoadThresholdInMeters</span></div>
<div class="block"><p>Optional threshold allows specifying a distance within which the waypoint could be considered
 as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching.
 Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.</p></div>
</section>
</li>
<li>
<section class="detail" id="chargingStop">
<h3>chargingStop</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstop" title="class in com.here.sdk.routing">ChargingStop</a></span> <span class="element-name">chargingStop</span></div>
<div class="block"><p>Specifies of a user-planned charging stop.
 The resulting <code>Route</code> may contain this waypoint as a <code>RoutePlace</code> with a non-null <code>ChargingStation</code> member
 when the provided specifications indicate that a stop is required to charge the EV battery.
 <strong>Note:</strong>
 If [EVCarOptions.ensure_reachability] is not set as <code>true</code> and [ChargingStop.min_duration] is not provided,
 route calculation may suggest a better charging stop instead of this stop.</p></div>
</section>
</li>
<li>
<section class="detail" id="currentWeightChangeInKilograms">
<h3>currentWeightChangeInKilograms</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">currentWeightChangeInKilograms</span></div>
<div class="block"><p>Changes the value of <code>vehicle[currentWeight]</code> by this value.
 Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route.
 Changes to the configuration of the vehicle, such as adding a trailer, aren't supported.
 Relative value in kilograms. Available range: from -40000 to 40000 (inclusive).
 <strong>Note:</strong>
<ul>
<li>A route request with this parameter requires to set <a href="sdk-for-android-navigate-vehiclespecification#currentWeightInKilograms"><code>VehicleSpecification.currentWeightInKilograms</code></a> and
 <a href="sdk-for-android-navigate-vehiclespecification#grossWeightInKilograms"><code>VehicleSpecification.grossWeightInKilograms</code></a>.</li>
<li>This feature is supported in transport modes of <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>, <a href="sdk-for-android-navigate-transportmode#TAXI"><code>TransportMode.TAXI</code></a>, or
 <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>.</li>
</ul>
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates)">
<h3>Waypoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Waypoint</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The waypoint's geographic coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,com.here.time.Duration)">
<h3>Waypoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Waypoint</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype" title="enum class in com.here.sdk.routing">WaypointType</a> type,
 int transitRadiusInMeters,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> headingInDegrees,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> sideOfStreetHint,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> minCourseDistanceInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The waypoint's geographic coordinates.</p></dd>
<dd><code>type</code> - <p>Defines how a waypoint should be considered for route calculation.
 The default waypoint type is <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>transitRadiusInMeters</code> - <p>The maximum allowed distance from the waypoint that the calculated
 route may pass through. For example, to drive past a city without necessarily going
 into the city center, you can specify the coordinates of the center and a transit
 radius of 5000m. The default transit radius is zero.
 If the route should pass the waypoint as close as possible, the default value
 should be kept. Note that the waypoint will be map-matched to a road.
 Non-zero values allow a greater tolerance.
 Note that <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#sideOfStreetHint"><code>sideOfStreetHint</code></a> option is ignored if the user sets this option with a value
 greater than zero.</p></dd>
<dd><code>headingInDegrees</code> - <p>Optional heading angle referenced by true North, clockwise specifying
 the direction of travel. The heading direction may help the routing algorithm to select
 the best direction, for example, when multiple directions are possible at a road junction.
 North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees.
 The value must be in the range [0, 360] when specified. By default, or when <code>null</code> is set,
 heading is ignored for route calculation.</p></dd>
<dd><code>sideOfStreetHint</code> - <p>Optional coordinates to indicate which side of the street should be used to reach the waypoint.
 For example, if the location is to the left of the street, the router will prefer using that side
 in case the street has dividers.
 Note that this option is ignored if the user sets <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#transitRadiusInMeters"><code>transitRadiusInMeters</code></a> option with a
 value greater than zero.</p></dd>
<dd><code>minCourseDistanceInMeters</code> - <p>Optional distance in meters during which the user wants to avoid taking actions. For example, if
 the origin is set by a moving vehicle, the user might not have time to react to immediate actions such
 as a sharp right turn.</p></dd>
<dd><code>duration</code> - <p>The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.
 Impacts time-aware calculations.
 Ignored for waypoints of type <a href="sdk-for-android-navigate-waypointtype#PASS_THROUGH"><code>WaypointType.PASS_THROUGH</code></a>.
 The default duration is 0 seconds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.routing.WaypointType,int,java.lang.Double,com.here.sdk.core.GeoCoordinates,java.lang.Integer,java.lang.String,com.here.time.Duration)">
<h3>Waypoint</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Waypoint</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype" title="enum class in com.here.sdk.routing">WaypointType</a> type,
 int transitRadiusInMeters,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> headingInDegrees,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> sideOfStreetHint,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> minCourseDistanceInMeters,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> nameHint,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The waypoint's geographic coordinates.</p></dd>
<dd><code>type</code> - <p>Defines how a waypoint should be considered for route calculation.
 The default waypoint type is <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>transitRadiusInMeters</code> - <p>The maximum allowed distance from the waypoint that the calculated
 route may pass through. For example, to drive past a city without necessarily going
 into the city center, you can specify the coordinates of the center and a transit
 radius of 5000m. The default transit radius is zero.
 If the route should pass the waypoint as close as possible, the default value
 should be kept. Note that the waypoint will be map-matched to a road.
 Non-zero values allow a greater tolerance.
 Note that <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#sideOfStreetHint"><code>sideOfStreetHint</code></a> option is ignored if the user sets this option with a value
 greater than zero.</p></dd>
<dd><code>headingInDegrees</code> - <p>Optional heading angle referenced by true North, clockwise specifying
 the direction of travel. The heading direction may help the routing algorithm to select
 the best direction, for example, when multiple directions are possible at a road junction.
 North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees.
 The value must be in the range [0, 360] when specified. By default, or when <code>null</code> is set,
 heading is ignored for route calculation.</p></dd>
<dd><code>sideOfStreetHint</code> - <p>Optional coordinates to indicate which side of the street should be used to reach the waypoint.
 For example, if the location is to the left of the street, the router will prefer using that side
 in case the street has dividers.
 Note that this option is ignored if the user sets <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint#transitRadiusInMeters"><code>transitRadiusInMeters</code></a> option with a
 value greater than zero.</p></dd>
<dd><code>minCourseDistanceInMeters</code> - <p>Optional distance in meters during which the user wants to avoid taking actions. For example, if
 the origin is set by a moving vehicle, the user might not have time to react to immediate actions such
 as a sharp right turn.</p></dd>
<dd><code>nameHint</code> - <p>Optional name hint causes the router to look for the place with the most similar name.
 This can e.g. include things like: <code>North</code> being used to differentiate between
 interstates <code>I66 North</code> and <code>I66 South</code>, <code>Downtown Avenue</code> being used to correctly
 select a residential street.</p></dd>
<dd><code>duration</code> - <p>The duration in seconds that should be spent at a waypoint of type <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.
 Impacts time-aware calculations.
 Ignored for waypoints of type <a href="sdk-for-android-navigate-waypointtype#PASS_THROUGH"><code>WaypointType.PASS_THROUGH</code></a>.
 The default duration is 0 seconds.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
