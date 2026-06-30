---
title: "RoutePlace (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routeplace"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoutePlace.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.RoutePlace</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoutePlace</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The location information.</p></div>
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
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#chargeInKilowattHours">chargeInKilowattHours</a></code></div>
<div class="col-last even-row-color">
<div class="block">Estimated battery charge in kWh for electric vehicles when leaving this place.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation" title="class in com.here.sdk.routing">ChargingStation</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#chargingStation">chargingStation</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Charging station data for electric vehicles.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#displayCoordinates">displayCoordinates</a></code></div>
<div class="col-last even-row-color">
<div class="block">Location of the Points of Interest (PoI) to be displayed in the visualization.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#id">id</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Identifier of a public transit place if available.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#mapMatchedCoordinates">mapMatchedCoordinates</a></code></div>
<div class="col-last even-row-color">
<div class="block">Map-matched geographic coordinates.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#name">name</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Name of a public transit place if available.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#originalCoordinates">originalCoordinates</a></code></div>
<div class="col-last even-row-color">
<div class="block">User-defined geographic coordinates.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#platform">platform</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Platform name or number of a public transit place if available.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-routing-sideofdestination" title="enum class in com.here.sdk.routing">SideOfDestination</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#sideOfDestination">sideOfDestination</a></code></div>
<div class="col-last even-row-color">
<div class="block">Side of destination: left, right or undefined.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-explore-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#type">type</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The type of the route place.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#waypointIndex">waypointIndex</a></code></div>
<div class="col-last even-row-color">
<div class="block">If available, this index corresponds to the waypoint in the original
 user-defined waypoint list.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#%3Cinit%3E(com.here.sdk.routing.RoutePlaceType,com.here.sdk.core.GeoCoordinates)">RoutePlace</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a> type,
 <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> mapMatchedCoordinates)</code></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#hashCode()">hashCode</a>()</code></div>

<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routeplace#isOffRoad()">isOffRoad</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks whether the <a href="sdk-for-android-explore-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing"><code>RoutePlace</code></a> is off-road or not.</div>
</div>
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
<section class="detail" id="type">
<h3>type</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a></span> <span class="element-name">type</span></div>
<div class="block"><p>The type of the route place.</p></div>
</section>
</li>
<li>
<section class="detail" id="waypointIndex">
<h3>waypointIndex</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">waypointIndex</span></div>
<div class="block"><p>If available, this index corresponds to the waypoint in the original
 user-defined waypoint list. Otherwise, this waypoint was added during
 route calculation by the system.</p></div>
</section>
</li>
<li>
<section class="detail" id="originalCoordinates">
<h3>originalCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">originalCoordinates</span></div>
<div class="block"><p>User-defined geographic coordinates. If not available, it means this place
 was added during route calculation.</p></div>
</section>
</li>
<li>
<section class="detail" id="mapMatchedCoordinates">
<h3>mapMatchedCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">mapMatchedCoordinates</span></div>
<div class="block"><p>Map-matched geographic coordinates.</p></div>
</section>
</li>
<li>
<section class="detail" id="displayCoordinates">
<h3>displayCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">displayCoordinates</span></div>
<div class="block"><p>Location of the Points of Interest (PoI) to be displayed in the visualization.
 In the map data, PoI have a set of display coordinates as well as a set of access/routing coordinates.
 While the access/routing coordinates specify the nearest accessible road network location
 that can be apart from actual location of the PoI,
 the display coordinates specify the location of the PoI to be displayed accurately in the visualization.</p></div>
</section>
</li>
<li>
<section class="detail" id="chargeInKilowattHours">
<h3>chargeInKilowattHours</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">chargeInKilowattHours</span></div>
<div class="block"><p>Estimated battery charge in kWh for electric vehicles when leaving this place.
 Available only if the route was calculated with <a href="sdk-for-android-explore-electricvehicleoptions#ensureReachability"><code>ElectricVehicleOptions.ensureReachability</code></a> = <code>true</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="chargingStation">
<h3>chargingStation</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-chargingstation" title="class in com.here.sdk.routing">ChargingStation</a></span> <span class="element-name">chargingStation</span></div>
<div class="block"><p>Charging station data for electric vehicles.</p></div>
</section>
</li>
<li>
<section class="detail" id="name">
<h3>name</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">name</span></div>
<div class="block"><p>Name of a public transit place if available.</p></div>
</section>
</li>
<li>
<section class="detail" id="id">
<h3>id</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">id</span></div>
<div class="block"><p>Identifier of a public transit place if available.</p></div>
</section>
</li>
<li>
<section class="detail" id="platform">
<h3>platform</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">platform</span></div>
<div class="block"><p>Platform name or number of a public transit place if available.</p></div>
</section>
</li>
<li>
<section class="detail" id="sideOfDestination">
<h3>sideOfDestination</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-routing-sideofdestination" title="enum class in com.here.sdk.routing">SideOfDestination</a></span> <span class="element-name">sideOfDestination</span></div>
<div class="block"><p>Side of destination: left, right or undefined.
 <code>null</code> for transit sections and for origin points.
 <code>UNDEFINED</code> if <code>originalCoordinates</code> are not identified or too close to the road.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.RoutePlaceType,com.here.sdk.core.GeoCoordinates)">
<h3>RoutePlace</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoutePlace</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a> type,
 @NonNull
 <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> mapMatchedCoordinates)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - <p>The type of the route place.</p></dd>
<dd><code>mapMatchedCoordinates</code> - <p>Map-matched geographic coordinates.</p></dd>
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
<li>
<section class="detail" id="isOffRoad()">
<h3>isOffRoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOffRoad</span>()</div>
<div class="block"><p>Checks whether the <a href="sdk-for-android-explore-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing"><code>RoutePlace</code></a> is off-road or not.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><code>true</code> if the <a href="sdk-for-android-explore-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing"><code>RoutePlace</code></a> is off-road, <code>false</code> otherwise.</p></dd>
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
