---
title: "RoutePlace (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routeplace"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RoutePlace.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.RoutePlace</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RoutePlace</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The location information.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#chargeInKilowattHours">chargeInKilowattHours</a></code></div>
<div className="col-last even-row-color">
<div className="block">Estimated battery charge in kWh for electric vehicles when leaving this place.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation" title="class in com.here.sdk.routing">ChargingStation</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#chargingStation">chargingStation</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Charging station data for electric vehicles.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#displayCoordinates">displayCoordinates</a></code></div>
<div className="col-last even-row-color">
<div className="block">Location of the Points of Interest (PoI) to be displayed in the visualization.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#id">id</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Identifier of a public transit place if available.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#mapMatchedCoordinates">mapMatchedCoordinates</a></code></div>
<div className="col-last even-row-color">
<div className="block">Map-matched geographic coordinates.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#name">name</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Name of a public transit place if available.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#originalCoordinates">originalCoordinates</a></code></div>
<div className="col-last even-row-color">
<div className="block">User-defined geographic coordinates.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#platform">platform</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Platform name or number of a public transit place if available.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-sideofdestination" title="enum class in com.here.sdk.routing">SideOfDestination</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#sideOfDestination">sideOfDestination</a></code></div>
<div className="col-last even-row-color">
<div className="block">Side of destination: left, right or undefined.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#type">type</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The type of the route place.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#waypointIndex">waypointIndex</a></code></div>
<div className="col-last even-row-color">
<div className="block">If available, this index corresponds to the waypoint in the original
 user-defined waypoint list.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routeplace#%3Cinit%3E(com.here.sdk.routing.RoutePlaceType,com.here.sdk.core.GeoCoordinates)">RoutePlace</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a> type,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> mapMatchedCoordinates)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>The type of the route place.</p></div>
</section>
</li>
<li>
<section className="detail" id="waypointIndex">
<h3>waypointIndex</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span className="element-name">waypointIndex</span></div>
<div className="block"><p>If available, this index corresponds to the waypoint in the original
 user-defined waypoint list. Otherwise, this waypoint was added during
 route calculation by the system.</p></div>
</section>
</li>
<li>
<section className="detail" id="originalCoordinates">
<h3>originalCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">originalCoordinates</span></div>
<div className="block"><p>User-defined geographic coordinates. If not available, it means this place
 was added during route calculation.</p></div>
</section>
</li>
<li>
<section className="detail" id="mapMatchedCoordinates">
<h3>mapMatchedCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">mapMatchedCoordinates</span></div>
<div className="block"><p>Map-matched geographic coordinates.</p></div>
</section>
</li>
<li>
<section className="detail" id="displayCoordinates">
<h3>displayCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">displayCoordinates</span></div>
<div className="block"><p>Location of the Points of Interest (PoI) to be displayed in the visualization.
 In the map data, PoI have a set of display coordinates as well as a set of access/routing coordinates.
 While the access/routing coordinates specify the nearest accessible road network location
 that can be apart from actual location of the PoI,
 the display coordinates specify the location of the PoI to be displayed accurately in the visualization.</p></div>
</section>
</li>
<li>
<section className="detail" id="chargeInKilowattHours">
<h3>chargeInKilowattHours</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">chargeInKilowattHours</span></div>
<div className="block"><p>Estimated battery charge in kWh for electric vehicles when leaving this place.
 Available only if the route was calculated with <a href="sdk-for-android-navigate-electricvehicleoptions#ensureReachability"><code>ElectricVehicleOptions.ensureReachability</code></a> = <code>true</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="chargingStation">
<h3>chargingStation</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-chargingstation" title="class in com.here.sdk.routing">ChargingStation</a></span> <span className="element-name">chargingStation</span></div>
<div className="block"><p>Charging station data for electric vehicles.</p></div>
</section>
</li>
<li>
<section className="detail" id="name">
<h3>name</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">name</span></div>
<div className="block"><p>Name of a public transit place if available.</p></div>
</section>
</li>
<li>
<section className="detail" id="id">
<h3>id</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">id</span></div>
<div className="block"><p>Identifier of a public transit place if available.</p></div>
</section>
</li>
<li>
<section className="detail" id="platform">
<h3>platform</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">platform</span></div>
<div className="block"><p>Platform name or number of a public transit place if available.</p></div>
</section>
</li>
<li>
<section className="detail" id="sideOfDestination">
<h3>sideOfDestination</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-sideofdestination" title="enum class in com.here.sdk.routing">SideOfDestination</a></span> <span className="element-name">sideOfDestination</span></div>
<div className="block"><p>Side of destination: left, right or undefined.
 <code>null</code> for transit sections and for origin points.
 <code>UNDEFINED</code> if <code>originalCoordinates</code> are not identified or too close to the road.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.routing.RoutePlaceType,com.here.sdk.core.GeoCoordinates)">
<h3>RoutePlace</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RoutePlace</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplacetype" title="enum class in com.here.sdk.routing">RoutePlaceType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> mapMatchedCoordinates)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isOffRoad()">
<h3>isOffRoad</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isOffRoad</span>()</div>
<div className="block"><p>Checks whether the <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing"><code>RoutePlace</code></a> is off-road or not.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><code>true</code> if the <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing"><code>RoutePlace</code></a> is off-road, <code>false</code> otherwise.</p></dd>
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
</div>



</div>
`
}</HTMLBlock>
