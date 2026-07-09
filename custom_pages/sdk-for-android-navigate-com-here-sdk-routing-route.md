---
title: "Route (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-route"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Route.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.routing.Route</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Route</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A route is a path through a road network over which someone travels.
 <strong>Note:</strong> Each <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> of a route contains a list of <a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a> objects
 that describe <em>potential issues</em> after the route was calculated. If the list is non-empty,
 it is recommended to evaluate possible violations against the requested route options and
 reject the route if deemed necessary.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="serialize(com.here.sdk.routing.Route)">
<h3>serialize</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type">byte[]</span> <span className="element-name">serialize</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route)</span></div>
<div className="block"><p>Serializes given route to a binary data.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>route</code> - <p>The route which should be serialized.</p></dd>
<dt>Returns:</dt>
<dd><p>The binary data of the route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="deserialize(byte[])">
<h3>deserialize</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a></span> <span className="element-name">deserialize</span><wbr/><span className="parameters">(@NonNull
 byte[] routeData)</span></div>
<div className="block"><p>Creates route from the given binary data.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>routeData</code> - <p>The binary of a serialized route.</p></dd>
<dt>Returns:</dt>
<dd><p>The route object restored from the binary data.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSections()">
<h3>getSections</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing">Section</a>&gt;</span> <span className="element-name">getSections</span>()</div>
<div className="block"><p>Gets the sections that make up this route.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The sections that make up this route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span className="element-name">getGeometry</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this route. It may not contain the original
 coordinates specified in the request for a route.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this route. It may not contain the original
     coordinates specified in the request for a route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getBoundingBox</span>()</div>
<div className="block"><p>Gets the closest rectangular area where this route fits in.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The closest rectangular area where this route fits in.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getLengthInMeters</span>()</div>
<div className="block"><p>Gets the length of this route in meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The length of this route in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLanguage()">
<h3>getLanguage</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></span> <span className="element-name">getLanguage</span>()</div>
<div className="block"><p>Gets the language requested for all textual information related to this route.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Indicates the language requested for all textual information related to this route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOptimizationMode()">
<h3>getOptimizationMode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></span> <span className="element-name">getOptimizationMode</span>()</div>
<div className="block"><p>Gets the optimization mode requested for route calculation.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The optimization mode requested for route calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRequestedTransportMode()">
<h3>getRequestedTransportMode</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a></span> <span className="element-name">getRequestedTransportMode</span>()</div>
<div className="block"><p>Gets the transport mode requested for route calculation.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The transport mode requested for route calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getConsumptionInKilowattHours()">
<h3>getConsumptionInKilowattHours</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span className="element-name">getConsumptionInKilowattHours</span>()</div>
<div className="block"><p>Gets estimated net energy consumption (in kWh) if the transportation mode used for this route
 is an electric vehicle. Note that it can be negative due to energy recuperation.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Estimated net energy consumption (in kWh) if the transportation mode used for this route
     is an electric vehicle. Note that it can be negative due to energy recuperation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRouteHandle()">
<h3>getRouteHandle</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a></span> <span className="element-name">getRouteHandle</span>()</div>
<div className="block"><p>Gets the route handle of this route. Note that it is provided only if
 <a href="sdk-for-android-navigate-routeoptions#enableRouteHandle"><code>RouteOptions.enableRouteHandle</code></a> is set before route calculation.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The route handle of this route. Note that it is provided only if
     <a href="sdk-for-android-navigate-routeoptions#enableRouteHandle"><code>RouteOptions.enableRouteHandle</code></a> is set before route calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDuration()">
<h3>getDuration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getDuration</span>()</div>
<div className="block"><p>Gets the estimated time in seconds needed to travel along this route, including
 real-time traffic delays if available.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The estimated time in seconds needed to travel along this route, including
     real-time traffic delays if available.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficDelay()">
<h3>getTrafficDelay</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">getTrafficDelay</span>()</div>
<div className="block"><p>Gets the estimated time in seconds spent in traffic along this route. Negative values
 indicate that the route can be traversed faster than usual.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The estimated time in seconds spent in traffic along this route. Negative values
     indicate that the route can be traversed faster than usual.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoutingOptions()">
<h3>getRoutingOptions</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a></span> <span className="element-name">getRoutingOptions</span>()</div>
<div className="block"><p>Gets the options used to calculate this route.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The set of options used to calculate the route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRailwayCrossings()">
<h3>getRailwayCrossings</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-routerailwaycrossing" title="class in com.here.sdk.routing">RouteRailwayCrossing</a>&gt;</span> <span className="element-name">getRailwayCrossings</span>()</div>
<div className="block"><p>Gets railway crossings.
 Railway crossing information is only available for routes created with the online <code>RoutingEngine</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Collection of railway crossings along the route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRouteLabels()">
<h3>getRouteLabels</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-routelabel" title="class in com.here.sdk.routing">RouteLabel</a>&gt;</span> <span className="element-name">getRouteLabels</span>()</div>
<div className="block"><p>Gets route labels.
 The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes.
 The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives
 when alternative routes have been quested via <code>RouteOptions</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A collection containing a maximum of 2 <code>RouteLabel</code> instances for the route. It will return an empty list if no labels are available.</p></dd>
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
