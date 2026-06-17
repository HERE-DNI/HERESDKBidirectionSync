---
title: "IndoorRoutingEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutingengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- IndoorRoutingEngine.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.venue.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.routing.IndoorRoutingEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">IndoorRoutingEngine</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Use the IndoorRoutingEngine to calculate a route inside a venue.
 <br/>
 Route calculation is done asynchronously and requires an
 internet connection. The resulting route contains various
 information such as the polyline, route length in meters,
 estimated time to traverse along the route and maneuver data.
 <br/>
 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.
 Currently, the indoor route calculation may not be accurate so that e.g. a pedestrian
 end user might be routed via a vehicle access and route or similar. Therefore end users
 must use this feature with caution and always be aware of the surroundings. The signs
 and instructions given at the premises must be observed. You are required to inform
 the end user about this in an appropriate manner, whether in the UI of your application,
 your end user terms or similar.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.venue.service.VenueService)">IndoorRoutingEngine</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venueservice" title="class in com.here.sdk.venue.service">VenueService</a> venueService)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(com.here.sdk.venue.routing.IndoorWaypoint,com.here.sdk.venue.routing.IndoorWaypoint,com.here.sdk.venue.routing.IndoorRouteOptions,com.here.sdk.venue.routing.CalculateIndoorRouteCallback)">calculateRoute</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-indoorwaypoint" title="class in com.here.sdk.venue.routing">IndoorWaypoint</a> from,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-indoorwaypoint" title="class in com.here.sdk.venue.routing">IndoorWaypoint</a> to,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-indoorrouteoptions" title="class in com.here.sdk.venue.routing">IndoorRouteOptions</a> routeOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateindoorroutecallback" title="interface in com.here.sdk.venue.routing">CalculateIndoorRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously calculates a route inside a venue.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.venue.service.VenueService)">
<h3>IndoorRoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IndoorRoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venueservice" title="class in com.here.sdk.venue.service">VenueService</a> venueService)</span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueService</code> - <p>A venue service instance.</p></dd>
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
<section class="detail" id="calculateRoute(com.here.sdk.venue.routing.IndoorWaypoint,com.here.sdk.venue.routing.IndoorWaypoint,com.here.sdk.venue.routing.IndoorRouteOptions,com.here.sdk.venue.routing.CalculateIndoorRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-indoorwaypoint" title="class in com.here.sdk.venue.routing">IndoorWaypoint</a> from,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-indoorwaypoint" title="class in com.here.sdk.venue.routing">IndoorWaypoint</a> to,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-indoorrouteoptions" title="class in com.here.sdk.venue.routing">IndoorRouteOptions</a> routeOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateindoorroutecallback" title="interface in com.here.sdk.venue.routing">CalculateIndoorRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously calculates a route inside a venue.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>from</code> - <p>A starting position of the route to calculate.</p></dd>
<dd><code>to</code> - <p>A destination position of the route to calculate.</p></dd>
<dd><code>routeOptions</code> - <p>Options specific for indoor route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
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
