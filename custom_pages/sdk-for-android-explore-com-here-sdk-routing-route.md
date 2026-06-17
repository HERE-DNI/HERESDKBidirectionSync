---
title: "Route (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-route"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Route.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.Route</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Route</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A route is a path through a road network over which someone travels.
 </p><p><strong>Note:</strong> Each <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-section" title="class in com.here.sdk.routing"><code>Section</code></a> of a route contains a list of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a> objects
 that describe <em>potential issues</em> after the route was calculated. If the list is non-empty,
 it is recommended to evaluate possible violations against the requested route options and
 reject the route if deemed necessary.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#deserialize(byte%5B%5D)">deserialize</a><wbr/>(byte[] routeData)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates route from the given binary data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getBoundingBox()">getBoundingBox</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the closest rectangular area where this route fits in.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getConsumptionInKilowattHours()">getConsumptionInKilowattHours</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets estimated net energy consumption (in kWh) if the transportation mode used for this route
 is an electric vehicle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getDuration()">getDuration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the estimated time in seconds needed to travel along this route, including
 real-time traffic delays if available.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getGeometry()">getGeometry</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getLanguage()">getLanguage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the language requested for all textual information related to this route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getLengthInMeters()">getLengthInMeters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the length of this route in meters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getOptimizationMode()">getOptimizationMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the optimization mode requested for route calculation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routerailwaycrossing" title="class in com.here.sdk.routing">RouteRailwayCrossing</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getRailwayCrossings()">getRailwayCrossings</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets railway crossings.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getRequestedTransportMode()">getRequestedTransportMode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the transport mode requested for route calculation.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getRouteHandle()">getRouteHandle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the route handle of this route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routelabel" title="class in com.here.sdk.routing">RouteLabel</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getRouteLabels()">getRouteLabels</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets route labels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getRoutingOptions()">getRoutingOptions</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the options used to calculate this route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-section" title="class in com.here.sdk.routing">Section</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getSections()">getSections</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the sections that make up this route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#getTrafficDelay()">getTrafficDelay</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the estimated time in seconds spent in traffic along this route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static byte[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#serialize(com.here.sdk.routing.Route)">serialize</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a> route)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Serializes given route to a binary data.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="serialize(com.here.sdk.routing.Route)">
<h3>serialize</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type">byte[]</span> <span class="element-name">serialize</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a> route)</span></div>
<div class="block"><p>Serializes given route to a binary data.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>route</code> - <p>The route which should be serialized.</p></dd>
<dt>Returns:</dt>
<dd><p>The binary data of the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="deserialize(byte[])">
<h3>deserialize</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a></span> <span class="element-name">deserialize</span><wbr/><span class="parameters">(@NonNull
 byte[] routeData)</span></div>
<div class="block"><p>Creates route from the given binary data.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeData</code> - <p>The binary of a serialized route.</p></dd>
<dt>Returns:</dt>
<dd><p>The route object restored from the binary data.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSections()">
<h3>getSections</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-section" title="class in com.here.sdk.routing">Section</a>&gt;</span> <span class="element-name">getSections</span>()</div>
<div class="block"><p>Gets the sections that make up this route.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The sections that make up this route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span class="element-name">getGeometry</span>()</div>
<div class="block"><p>Gets the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this route. It may not contain the original
 coordinates specified in the request for a route.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this route. It may not contain the original
     coordinates specified in the request for a route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">getBoundingBox</span>()</div>
<div class="block"><p>Gets the closest rectangular area where this route fits in.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The closest rectangular area where this route fits in.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()</div>
<div class="block"><p>Gets the length of this route in meters.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The length of this route in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLanguage()">
<h3>getLanguage</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a></span> <span class="element-name">getLanguage</span>()</div>
<div class="block"><p>Gets the language requested for all textual information related to this route.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Indicates the language requested for all textual information related to this route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOptimizationMode()">
<h3>getOptimizationMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-optimizationmode" title="enum class in com.here.sdk.routing">OptimizationMode</a></span> <span class="element-name">getOptimizationMode</span>()</div>
<div class="block"><p>Gets the optimization mode requested for route calculation.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The optimization mode requested for route calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRequestedTransportMode()">
<h3>getRequestedTransportMode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a></span> <span class="element-name">getRequestedTransportMode</span>()</div>
<div class="block"><p>Gets the transport mode requested for route calculation.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The transport mode requested for route calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConsumptionInKilowattHours()">
<h3>getConsumptionInKilowattHours</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getConsumptionInKilowattHours</span>()</div>
<div class="block"><p>Gets estimated net energy consumption (in kWh) if the transportation mode used for this route
 is an electric vehicle. Note that it can be negative due to energy recuperation.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Estimated net energy consumption (in kWh) if the transportation mode used for this route
     is an electric vehicle. Note that it can be negative due to energy recuperation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteHandle()">
<h3>getRouteHandle</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a></span> <span class="element-name">getRouteHandle</span>()</div>
<div class="block"><p>Gets the route handle of this route. Note that it is provided only if
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routeoptions#enableRouteHandle"><code>RouteOptions.enableRouteHandle</code></a> is set before route calculation.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The route handle of this route. Note that it is provided only if
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routeoptions#enableRouteHandle"><code>RouteOptions.enableRouteHandle</code></a> is set before route calculation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDuration()">
<h3>getDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getDuration</span>()</div>
<div class="block"><p>Gets the estimated time in seconds needed to travel along this route, including
 real-time traffic delays if available.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The estimated time in seconds needed to travel along this route, including
     real-time traffic delays if available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficDelay()">
<h3>getTrafficDelay</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getTrafficDelay</span>()</div>
<div class="block"><p>Gets the estimated time in seconds spent in traffic along this route. Negative values
 indicate that the route can be traversed faster than usual.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The estimated time in seconds spent in traffic along this route. Negative values
     indicate that the route can be traversed faster than usual.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoutingOptions()">
<h3>getRoutingOptions</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a></span> <span class="element-name">getRoutingOptions</span>()</div>
<div class="block"><p>Gets the options used to calculate this route.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The set of options used to calculate the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRailwayCrossings()">
<h3>getRailwayCrossings</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routerailwaycrossing" title="class in com.here.sdk.routing">RouteRailwayCrossing</a>&gt;</span> <span class="element-name">getRailwayCrossings</span>()</div>
<div class="block"><p>Gets railway crossings.
 </p><p>Railway crossing information is only available for routes created with the online <code>RoutingEngine</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Collection of railway crossings along the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRouteLabels()">
<h3>getRouteLabels</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-routelabel" title="class in com.here.sdk.routing">RouteLabel</a>&gt;</span> <span class="element-name">getRouteLabels</span>()</div>
<div class="block"><p>Gets route labels.
 </p><p>The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes.
 The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives
 when alternative routes have been quested via <code>RouteOptions</code>.</p></div>
<dl class="notes">
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
</main>





</div>
`
}</HTMLBlock>
