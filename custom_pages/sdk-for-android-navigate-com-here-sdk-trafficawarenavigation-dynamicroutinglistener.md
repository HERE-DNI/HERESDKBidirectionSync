---
title: "DynamicRoutingListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- DynamicRoutingListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">DynamicRoutingListener</span></div>
<div class="block"><p>This interface should be implemented in order to
 receive notifications about the new route via the <a href="sdk-for-android-navigate-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onBetterRouteFound(com.here.sdk.routing.Route,int,int)">onBetterRouteFound</a><wbr/>(<a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> newRoute,
 int etaDifferenceInSeconds,
 int distanceDifferenceInMeters)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This event is issued when a better route could be found,
 as defined by <a href="sdk-for-android-navigate-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngineOptions</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onRoutingError(com.here.sdk.routing.RoutingError)">onRoutingError</a><wbr/>(<a href="sdk-for-android-navigate-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a> routingError)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This event is issued when an error occurred.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="onBetterRouteFound(com.here.sdk.routing.Route,int,int)">
<h3>onBetterRouteFound</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onBetterRouteFound</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> newRoute,
 int etaDifferenceInSeconds,
 int distanceDifferenceInMeters)</span></div>
<div class="block"><p>This event is issued when a better route could be found,
 as defined by <a href="sdk-for-android-navigate-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngineOptions</code></a>.
 To find a better route, two routes are calculated.
 The updated current route: A route that is calculated via the route specified.
 The dynamic route: A route that starts at the current position on the route specified
 and passes through the remaining waypoints.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>newRoute</code> - <p>The newly calculated route with the remaining waypoints starting from the
     current location.</p></dd>
<dd><code>etaDifferenceInSeconds</code> - <p>The difference in seconds:
     eta of the current updated route - eta of the dynamic route.</p></dd>
<dd><code>distanceDifferenceInMeters</code> - <p>The difference in meters:
     distance of the current updated route - distance of the dynamic route.
     The value can be negative in case the current updated route has
     a shorter distance, but its now assumed to be longer than the dynamic route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onRoutingError(com.here.sdk.routing.RoutingError)">
<h3>onRoutingError</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onRoutingError</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a> routingError)</span></div>
<div class="block"><p>This event is issued when an error occurred.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routingError</code> - <p>Routing error</p></dd>
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
